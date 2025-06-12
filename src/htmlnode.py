

class HTMLNode():

    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props # testing testing

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __repr__(self):
        # This is for printing the HTMLNode object to see all of its values.
        print(f"HTMLNode: ")
        print(f" - Tag: {self.tag}")
        print(f" - Value: {self.value}")
        print(f" - Children: {self.children}")
        print(f" - Props: {self.props}")