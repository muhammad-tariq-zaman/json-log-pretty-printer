import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestPretty(unittest.TestCase):
    def test_filter_by_level(self):
        text = '{"level": "INFO", "msg": "ok"}\n{"level": "ERROR", "msg": "fail"}\nnot json\n'
        self.assertEqual(len(main.parse_lines(text)), 2)
        errors = main.parse_lines(text, "ERROR")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["msg"], "fail")

    def test_render_is_indented(self):
        self.assertIn("\n  ", main.render([{"a": 1}]))


if __name__ == "__main__":
    unittest.main()
