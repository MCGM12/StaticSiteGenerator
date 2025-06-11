

class HTMLNode():

    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        formatted = " ".join(f'{k}="{v}"' for k, v in self.props.items())
        return (f'( {formatted} )')
    
    def __repr__(self):
        # This is for printing the HTMLNode object to see all of its values.
        print(f"HTMLNode: ")
        print(f" - Tag: {self.tag}")
        print(f" - Value: {self.value}")
        print(f" - Children: {self.children}")
        print(f" - Props: {self.props}")