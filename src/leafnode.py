from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)  # Do not pass children
        self.value = value


    def to_html(self):