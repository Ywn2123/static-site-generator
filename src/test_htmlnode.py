import unittest
from htmlnode import HTMLNode

test_dict = {
    "href" : "https://www.google.com",
    "target" : "_blank"
}

class TestTextNode(unittest.TestCase):
    def test1(self):
        case1 = HTMLNode('tag', 'value', 'children', test_dict)
        return case1.props_to_html()
    def test2(self):
        case1 = HTMLNode('b', 'text in a node', 'ABC')



if __name__ == "__main__":
    unittest.main()