from textnode import *

def main():
    a = TextNode('fuck you', 'italic', 'http://....')
    b = TextNode('fuck you', 'italic', 'http://....')
    c = TextNode('hello', 'bold', '')
    print(a==b, a==c)

if __name__ == "__main__":
    main()