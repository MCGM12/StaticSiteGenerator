from textnode import TextNode

def main():
    print("Running main.py \n ...")
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node.__repr__())


main()
