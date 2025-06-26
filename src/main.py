from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextType
from functions import *

def main():
    print("Running main.py \n ...")
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node.__repr__())
    # print_node = TextNode("This is a test text with a ' in betweent to make sure ' it works", "text")
    # print(split_nodes_delimiter(print_node, "'", TextType.TEXT))
    

# 
main()
