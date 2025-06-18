from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        if not self.children or any(child is None for child in self.children):
            raise ValueError("All children must be valid nodes.")
        for child in self.children:
            # For LeafNode, check for missing value
            if hasattr(child, "value") and child.value is None:
                raise ValueError("Child node is missing a value.")
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"