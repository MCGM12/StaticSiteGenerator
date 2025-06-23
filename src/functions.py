from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode
from textnode import TextType


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception(f"Invalid text type: {text_node.text_type}")
    if text_node.text_type == TextType.TEXT:
        return_node = LeafNode(None, text_node.text)
        return return_node
    elif text_node.text_type == TextType.BOLD:
        return_node = LeafNode("b", text_node.text)
        return return_node
    elif text_node.text_type == TextType.ITALIC:
        return_node = LeafNode("i", text_node.text)
        return return_node
    elif text_node.text_type == TextType.CODE:
        return_node = LeafNode("code", text_node.text)
        return return_node
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise Exception("Link text node must have a URL")
        return_node = LeafNode("a", text_node.text, props={"href": text_node.url})
        return return_node
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise Exception("Image text node must have a URL")
        return_node = LeafNode("img", "", props={"src": text_node.url})
        return return_node


def split_nodes_delimiter(old_nodes: TextNode, delimiter, text_type):
    #old_nodes is the input, delimiter is the string character to split on, text_type is the type of text node to create.
    new_string = old_nodes.text.split(delimiter)
    return new_string
