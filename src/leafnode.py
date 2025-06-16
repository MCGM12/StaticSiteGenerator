from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, **kwargs):
        super().__init__(tag=tag, **kwargs)
        self.value = value


    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    