import json
from lxml import etree, html


def format_metadata(text: str) -> str:
    json_obj: dict = json.loads(text)
    lines = [
        f"{key}: {value}"
        for key, value in sorted(json_obj.items(), key=_by_key_lower)
    ]
    formatted = "\n".join(lines)
    return formatted


def format_json_string(text: str, indent=4) -> str:
    json_obj: dict = json.loads(text)
    formatted = json.dumps(json_obj, indent=indent)
    return formatted


def format_xml_string(text: str, indent=2) -> str:
    xml_obj = etree.fromstring(text)
    etree.indent(xml_obj, space=" " * indent)
    formatted = etree.tostring(xml_obj, encoding="unicode")
    return formatted


def format_html_string(text: str, indent=2) -> str:
    html_obj = html.fromstring(text)
    etree.indent(html_obj, space=" " * indent)
    formatted = html.tostring(html_obj, encoding="unicode")
    return formatted


def no_format(text: str):
    return text


def _by_key_lower(dict_item: tuple): key, val = dict_item; return key.lower()
