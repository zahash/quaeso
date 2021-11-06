import sys
import argparse
import json
import yaml
from functools import partial
from requests.api import request
from lxml import etree, html
from pygments import highlight
from pygments.lexers.data import JsonLexer, YamlLexer
from pygments.lexers.html import HtmlLexer, XmlLexer
from pygments.formatters.terminal256 import TerminalTrueColorFormatter
from pygments.formatters.terminal import TerminalFormatter


def bout(x): sys.stdout.buffer.write(x)
def out(x): return sys.stdout.write(str(x)+"\n")
def err(x): return sys.stderr.write(str(x)+"\n")
def by_key_lower(item: tuple): key, val = item; return key.lower()


def yeet(req): return request(**req)


def output_formatted(res):
    content_type = res.headers.get("content-type", "")
    handle_metadata_out(res)

    if content_type.startswith("application/json"):
        handle_json_out(res.text)
    elif content_type.startswith("text/xml"):
        handle_xml_out(res.text)
    elif content_type.startswith("text/html"):
        handle_html_out(res.text)
    elif content_type.startswith("text"):
        handle_plain_out(res.text)
    else:
        handle_binary_out(res.content)


def handle_metadata_out(res):
    metadata = []
    metadata.append(f"Status: {res.status_code}")
    for k, v in sorted(res.headers.items(), key=by_key_lower):
        metadata.append(f"{k}: {v}")

    text = "\n".join(metadata)
    if sys.stderr.isatty():
        text = highlight(text, YamlLexer(), TerminalTrueColorFormatter())
    err(text)


def handle_json_out(text):
    text = json.dumps(json.loads(text), indent=4)
    if sys.stdout.isatty():
        text = highlight(text, JsonLexer(), TerminalFormatter())
    out(text)


def handle_xml_out(text):
    data = etree.fromstring(text)
    etree.indent(data, space=" "*2)
    text = etree.tostring(data, encoding="unicode")
    if sys.stdout.isatty():
        text = highlight(text, XmlLexer(), TerminalFormatter())
    out(text)


def handle_html_out(text):
    data = html.fromstring(text)
    etree.indent(data, space=" "*2)
    text = html.tostring(data, encoding="unicode")
    if sys.stdout.isatty():
        text = highlight(text, HtmlLexer(), TerminalFormatter())
    out(text)


def handle_plain_out(text):
    out(text)


def handle_binary_out(content):
    bout(content)


def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "requestfile",
        type=str,
        help="Request file in .json or .yaml or .yml format",
    )
    return ap.parse_args()


def read_file(filepath):
    if filepath.endswith(".yml") or filepath.endswith(".yaml"):
        loader = partial(yaml.load, Loader=yaml.FullLoader)
    elif filepath.endswith(".json"):
        loader = json.load
    else:
        raise Exception("Unsupported file type")

    with open(filepath, "r") as f:
        file_data = loader(f)

    return file_data
