import unittest
from parentnode import ParentNode
class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_parent_to_html(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_parent_to_html_with_children(self):
        child1 = ParentNode("span", [])
        child2 = ParentNode("p", [])
        node = ParentNode("div", [child1, child2])
        self.assertEqual(node.to_html(), "<div><span></span><p></p></div>")

    def test_parent_to_html_with_props(self):
        node = ParentNode("div", [], {"class": "container"})
        self.assertEqual(node.to_html(), "<div class='container'></div>")

    def test_parent_to_html_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode("", []).to_html()

    def test_parent_to_html_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_parent_to_html_invalid_child(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [None]).to_html()