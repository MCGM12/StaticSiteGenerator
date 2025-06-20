import unittest
from functions import *

class miscTextStuff(unittest.TestCase):

    def test_text_node_to_html_node(self):
        text_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.text, "This is some anchor text")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")

    def test_invalid_text_type(self):
        text_node = TextNode("Invalid type", "invalid_type", None)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(text_node)
        self.assertTrue('Invalid text type' in str(context.exception))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")