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
        return case1.props_to_html()
    def test3(self):
        case1 = HTMLNode('tag', 'value', 'children', test_dict).props_to_html()
        case2 = HTMLNode('tag', 'value', 'children', test_dict).props_to_html()
        self.assertEqual(case1, case2)




if __name__ == "__main__":
    unittest.main()