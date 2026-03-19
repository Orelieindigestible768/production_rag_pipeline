import unittest

from production_rag_pipeline.pipeline import build_llm_context


class PipelineContextTests(unittest.TestCase):
    def test_build_llm_context_returns_empty_message_for_no_chunks(self):
        context, mapping, grouped = build_llm_context([], [])
        self.assertEqual(context, "No relevant content found.")
        self.assertEqual(mapping, {})
        self.assertEqual(grouped, {})

    def test_build_llm_context_filters_unfetched_sources(self):
        ranked_chunks = [
            {
                "text": "Bitcoin trades near 67000 USD with strong market volume.",
                "source_idx": 0,
                "source_url": "https://example.com/a",
                "source_title": "Source A",
                "chunk_idx": 0,
                "relevance": 0.91,
            },
            {
                "text": "Ghost source should be removed because fetch failed.",
                "source_idx": 1,
                "source_url": "https://example.com/b",
                "source_title": "Source B",
                "chunk_idx": 0,
                "relevance": 0.95,
            },
        ]

        context, mapping, grouped = build_llm_context(
            ranked_chunks,
            [],
            fetched_urls={"https://example.com/a"},
            renumber_sources=True,
        )

        self.assertIn("[1] Source A", context)
        self.assertNotIn("Source B", context)
        self.assertEqual(mapping, {0: 1})
        self.assertIn(0, grouped)
        self.assertNotIn(1, grouped)


if __name__ == "__main__":
    unittest.main()
