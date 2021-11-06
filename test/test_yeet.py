import unittest
from .util import FakeResponse, captured_output, captured_binary_output


class TestNONColorized(unittest.TestCase):
    def setUp(self):
        # monkey patch isatty to return false before importing yeet
        # this is done to prevent colorized output from being written to stdout and stderr
        import sys
        sys.stdout.isatty = lambda: False
        sys.stderr.isatty = lambda: False
        global yeet
        from yeet import yeet

    def test_metadata(self):
        status_code = 123
        headers = {'B': 'const2', 'a': 'const1'}
        response = FakeResponse(status_code, headers)
        with captured_output() as (stdout, stderr):
            yeet.handle_metadata_output(response)

        self.assertEqual(stdout.getvalue().strip(), "")
        self.assertEqual(stderr.getvalue().strip(),
                         (f"Status: {status_code}\n"
                         "a: const1\n"
                          "B: const2"))

    def test_json(self):
        indent = 4
        json = '{"const1":"const2"}'
        with captured_output() as (stdout, stderr):
            yeet.handle_json_output(json)

        self.assertEqual(stdout.getvalue().strip(),
                         ('{\n'
                         f'{" "*indent}"const1": "const2"\n'
                          '}'))
        self.assertEqual(stderr.getvalue().strip(), '')

    def test_xml(self):
        indent = 2
        xml = "<xml><body>const1</body></xml>"
        with captured_output() as (stdout, stderr):
            yeet.handle_xml_output(xml)

        self.assertEqual(stdout.getvalue().strip(),
                         ("<xml>\n"
                          f"{' '*indent}<body>const1</body>\n"
                          "</xml>"))
        self.assertEqual(stderr.getvalue().strip(), '')

    def test_html(self):
        indent = 2
        html = "<html><body>const1</body></html>"
        with captured_output() as (stdout, stderr):
            yeet.handle_html_output(html)
        self.assertEqual(stdout.getvalue().strip(),
                         ("<html>\n"
                          f"{' '*indent}<body>const1</body>\n"
                          "</html>"))
        self.assertEqual(stderr.getvalue().strip(), '')

    def test_plain(self):
        text = "const1"
        with captured_output() as (stdout, stderr):
            yeet.handle_plain_output(text)

        self.assertEqual(stdout.getvalue().strip(), text)
        self.assertEqual(stderr.getvalue().strip(), '')

    def test_binary(self):
        content = b"const1"
        with captured_binary_output() as (stdout, stderr):
            yeet.handle_binary_output(content)

        stdout.seek(0)
        stderr.seek(0)
        self.assertEqual(stdout.buffer.read(), content)
        self.assertEqual(stderr.read().strip(), '')
