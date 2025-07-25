import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD, url="https://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_url_none(self):
        node = TextNode("Sample text", TextType.TEXT)
        node2 = TextNode("Sample text", TextType.TEXT)
        self.assertEqual(node.url, None)
        self.assertEqual(node2.url, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()