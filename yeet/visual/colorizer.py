from pygments import highlight
from pygments.lexers.data import JsonLexer, YamlLexer
from pygments.lexers.html import HtmlLexer, XmlLexer
from pygments.formatters.terminal256 import TerminalTrueColorFormatter
from pygments.formatters.terminal import TerminalFormatter


def colorize_metadata_string(text) -> str:
    colorized = highlight(text, YamlLexer(), TerminalTrueColorFormatter())
    return colorized


def colorize_json_string(text) -> str:
    colorized = highlight(text, JsonLexer(), TerminalFormatter())
    return colorized


def colorize_xml_string(text) -> str:
    colorized = highlight(text, XmlLexer(), TerminalFormatter())
    return colorized


def colorize_html_string(text) -> str:
    colorized = highlight(text, HtmlLexer(), TerminalFormatter())
    return colorized


def no_colorizer(text) -> str:
    return text
