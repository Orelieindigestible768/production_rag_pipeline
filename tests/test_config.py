import os
import tempfile
import textwrap
import unittest

from production_rag_pipeline.config import DEFAULT_CONFIG, load_config


class ConfigTests(unittest.TestCase):
    def test_load_config_from_yaml(self):
        with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as handle:
            handle.write(
                textwrap.dedent(
                    """
                    top_n_fetch: 8
                    fetch_timeout: 9
                    """
                ).strip()
            )
            path = handle.name

        try:
            config = load_config(path=path)
            self.assertEqual(config.top_n_fetch, 8)
            self.assertEqual(config.fetch_timeout, 9)
        finally:
            os.unlink(path)

    def test_environment_overrides_take_precedence(self):
        old_fetch = os.environ.get("RAG_TOP_N_FETCH")
        os.environ["RAG_TOP_N_FETCH"] = "7"
        try:
            config = load_config()
            self.assertEqual(config.top_n_fetch, 7)
            self.assertEqual(config.num_per_engine, DEFAULT_CONFIG.num_per_engine)
        finally:
            if old_fetch is None:
                os.environ.pop("RAG_TOP_N_FETCH", None)
            else:
                os.environ["RAG_TOP_N_FETCH"] = old_fetch


if __name__ == "__main__":
    unittest.main()
