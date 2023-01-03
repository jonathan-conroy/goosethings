from goose3 import Goose
from requests_html import HTMLSession
from parsers import parse

URL = "https://www.nytimes.com/2022/12/30/business/gate-gourmet-airline-food.html"

file = "/Users/jonathanconroy/Downloads/test-wsj-2.html"
def main():
    session = HTMLSession()
    r = session.get(URL)
    # r.html.render()
    # print(r.html.html)

    input = r.html.html #open(file).read()

    a = parse(URL, input)
    pretty_print(*a)

def pretty_print(article, removed, show_removed = True):
    print(article)
    if show_removed:
        print("---")
        for p in removed:
            print(f"REMOVED: {p}\n")
        print("---")

main()