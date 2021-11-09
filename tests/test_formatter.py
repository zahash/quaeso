import unittest
from yeet.visual import formatter


class TestFormatter(unittest.TestCase):
    def test_format_metadata(self):
        metadata = '{"const1": "const2"}'
        formatted = formatter.format_metadata(metadata)
        self.assertEqual(formatted, 'const1: const2')

    def test_format_json_string(self):
        json_string = '{"const1": "const2"}'
        formatted = formatter.format_json_string(json_string, indent=3)
        self.assertEqual(formatted, (
            '{\n'
            '   "const1": "const2"\n'
            '}'
        ))

    def test_format_xml_string(self):
        xml_string = '<const1><const2>const3</const2></const1>'
        formatted = formatter.format_xml_string(xml_string, indent=3)
        self.assertEqual(formatted, (
            '<const1>\n'
            '   <const2>const3</const2>\n'
            '</const1>'
        ))

    def test_format_html_string(self):
        html_string = '<html><body><p>const1</p></body></html>'
        formatted = formatter.format_html_string(html_string, indent=3)
        self.assertEqual(formatted, (
            '<html>\n'
            '   <body>\n'
            '      <p>const1</p>\n'
            '   </body>\n'
            '</html>'
        ))
