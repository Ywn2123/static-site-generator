import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_case2(self):
        a = TextNode('This is a text node', 'italic', 'http...')
        b = TextNode('This is a text node', 'bold', 'http...')
        self.assertNotEqual(a,b)
    def test_case3(self):
        a = TextNode('This is a text node', 'bold', 'http...')
        b = TextNode('This is a text node', 'bold',)
        self.assertNotEqual(a,b)
    def test_case4(self):
        a = TextNode('This is a text node', 'bold', 'http...')
        b = TextNode('', 'bold', 'http...')
        self.assertNotEqual(a,b)


if __name__ == "__main__":
    unittest.main()