import unittest
from ..pubmed import search_articles, fetch_article, search_fetch_articles, search_print_articles


class MyTestCase(unittest.TestCase):
    def test_search_articles(self):
        # TODO: melhor testes, neste momento testa se corre
        self.assertTrue(search_articles("ORF7a"))
        self.assertTrue(search_articles("ORF7a", ["generic", "function", "sars-cov-2"]))

    def test_fetch_article(self):
        # TODO: melhor testes, neste momento testa se corre
        self.assertTrue(fetch_article(32511297))

    def test_search_fetch_articles(self):
        # TODO: melhor testes, neste momento testa se corre
        self.assertTrue(search_fetch_articles("ORF7a"))
        self.assertTrue(search_fetch_articles("ORF7a", ["generic", "function", "sars-cov-2"]))

    def test_search_print_articles(self):
        # TODO: Better Test output
        # TODO: Filter only articles and reviews not letters
        # self.assertTrue(search_print_articles("ORF7a"))
        self.assertTrue(search_print_articles("ORF7a", ["generic", "function", "sars-cov-2"], file="scripts/tests_data/ORF7a2.md"))

if __name__ == '__main__':
    unittest.main()
