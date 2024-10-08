class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ''
        for n in self.props:
            output = output + (f'{n}="{self.props[n]}" ') 
        return output

test_dict = {
    "href" : "https://google.com",
    "target" : "_blank"
}

a = HTMLNode('<p>','this is text','child B', test_dict)
print(a.props_to_html())