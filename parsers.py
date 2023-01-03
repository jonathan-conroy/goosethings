## Parsers for:
# - Washington Post     (+)
# - New York Times      (+)
#   * Some headers may be incorrectly removed, but they
#     will probably be noted as "Removed"
# - Wall Street Journal (-)
#   * This one has some issues with the article end
# - The Hill            (?)

# Key:
# (+) Probably works
# (?) Seems like it works, from limited testing
# (-) Has issues

from bs4 import BeautifulSoup

def parse(domain, html_input):
    soup = BeautifulSoup(html_input, 'html.parser')
    if domain == "www.nytimes.com":
        return parse_nyt(soup)
    elif domain == "www.washingtonpost.com":
        return parse_washpost(soup)
    elif domain == "www.wsj.com":
        return parse_wsj(soup)
    elif domain == "thehill.com":
        return parse_hill(soup)
    else:
        return None, None


POSSIBLE_TAGS = ["p", "h1", "h2", "h3", "h4", "h5", "h6"]
def parse_washpost(soup):
    pars = soup.select(".article-body")

    valid = []
    removed = []
    for p in pars:
        if p.get_text() == "":
            continue
        to_remove = (len(p.find_parents(class_="hide-for-print"))) > 0 or \
                    (len(p.find_all(class_="hide-for-print")) > 0)
        if to_remove:
            removed.append(p.get_text())
        else:
            valid.append(p.get_text())

    return (valid, removed)

def parse_nyt(soup):
    select_str = ", ".join([f"section[name=articleBody] {x}" for x in POSSIBLE_TAGS])
    pars = soup.select(select_str)
    NORMAL_NYT = "css-at9mc1 evys1bk0"
    HEADER_NYT = "css-1bxm55 eoo0vm40"

    valid = []
    removed = []
    for p in pars:
        if 'class' not in p.attrs or \
            " ".join(p.attrs['class']) not in {NORMAL_NYT, HEADER_NYT}:
            removed.append(p.get_text().replace("\n", ""))
        else:
            valid.append(p.get_text().replace("\n", ""))

    return (valid, removed)

def parse_wsj(soup):
    select_str = ", ".join([f".article {x}" for x in POSSIBLE_TAGS])
    pars = soup.select(select_str)
    NORMAL_WSJ = "css-xbvutc-Paragraph e3t0jlg0"
    # Note: WJS appears to just use bold text for headers?
    #   Very few seem to exist...

    valid = []
    removed = []
    for p in pars:
        # I am not sure why there are sometimes random "\n"
        #  in the middle of the text. HTML should ignore them,
        #  anyway.
        if " ".join(p.attrs['class']) != NORMAL_WSJ:
            removed.append(p.get_text().replace("\n", ""))
        else:
            valid.append(p.get_text().replace("\n", ""))

    return (valid, removed)

def parse_hill(soup):
    select_str = ", ".join([f".article__text {x}" for x in POSSIBLE_TAGS])
    pars = soup.select(select_str)
    valid, removed = [], []
    for p in pars:
        if 'class' in p.attrs:
            removed.append(p.get_text().replace("\n", "").strip())
        else:
            valid.append(p.get_text().replace("\n", "").strip())

    return (valid, removed)

def parse_politico(soup):
    ...
    select_str = "p.story-text__paragraph"