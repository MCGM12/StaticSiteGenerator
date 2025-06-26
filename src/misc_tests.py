import unittest
from functions import *
from textnode import TextNode, TextType

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



    def test_split_simple(self):
        nodes = [TextNode("a,b,c", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(
            result,
            [
                TextNode("a", TextType.TEXT),
                TextNode("b", TextType.TEXT),
                TextNode("c", TextType.TEXT),
            ]
        )

    def test_split_no_delimiter(self):
        nodes = [TextNode("abc", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(result, [TextNode("abc", TextType.TEXT)])

    def test_split_multiple_nodes(self):
        nodes = [
            TextNode("a,b", TextType.TEXT),
            TextNode("x|y|z", TextType.BOLD),
        ]
        result = split_nodes_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(
            result,
            [
                TextNode("a", TextType.TEXT),
                TextNode("b", TextType.TEXT),
                TextNode("x|y|z", TextType.BOLD),
            ]
        )

    def test_split_multiple_delimiters(self):
        nodes = [TextNode("a|b|c|d", TextType.BOLD)]
        result = split_nodes_delimiter(nodes, "|", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("a", TextType.BOLD),
                TextNode("b", TextType.BOLD),
                TextNode("c", TextType.BOLD),
                TextNode("d", TextType.BOLD),
            ]
        )

    def test_non_textnode_raises(self):
        nodes = [TextNode("abc", TextType.TEXT), "not_a_textnode"]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, ",", TextType.TEXT)

    def test_different_text_type_not_split(self):
        nodes = [TextNode("a,b,c", TextType.BOLD)]
        result = split_nodes_delimiter(nodes, ",", TextType.TEXT)
        self.assertEqual(result, [TextNode("a,b,c", TextType.BOLD)])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)