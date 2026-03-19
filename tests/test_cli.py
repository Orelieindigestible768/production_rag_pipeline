import unittest

from production_rag_pipeline.cli import _detect_lang, build_parser


class CLITests(unittest.TestCase):
    def test_detect_lang_uses_cyrillic_for_russian(self):
        self.assertEqual(_detect_lang("новости ИИ"), "ru")

    def test_detect_lang_defaults_to_english(self):
        self.assertEqual(_detect_lang("latest AI news"), "en")

    def test_build_parser_accepts_modes(self):
        parser = build_parser()
        args = parser.parse_args(["bitcoin rate", "--mode", "search"])
        self.assertEqual(args.query, "bitcoin rate")
        self.assertEqual(args.mode, "search")


if __name__ == "__main__":
    unittest.main()
