from urllib.request import urlopen
from typing import List
import re


def scrape_quotes(urls: List[str]) -> List[str]:
    """
    Takes in a list of goodreads urls. Uses urllib to pull html
    and then uses regex to scrape quotes along with their authors.
    Returns list of strings of format: "<AUTHOR>  |  <QUOTE>"
    """
    quotes: List[str] = []
    authors: List[str] = []
    finale: List[str] = []
    for url in urls:
        page = urlopen(url)
        html = page.read().decode("UTF-8")
        quotes += re.findall(".*&ldquo.*", html)
        authors += re.findall("<span class=\"authorOrTitle\">\n.*", html)
    quotes = parse_quotes(quotes)
    authors = parse_authors(authors)
    for i in range(len(quotes)):
        finale.append(authors[i] + "  |  " + quotes[i])
    return finale


def parse_quotes(quotes: List[str]) -> List[str]:
    """
    Takes in a list of unformatted quote strings and pulls out the html jargon.
    """
    for i in range(len(quotes)):
        quotes[i] = re.split(".*&ldquo;", quotes[i])[1]
        quotes[i] = re.split("&rdquo;", quotes[i])[0]
        quotes[i] = re.sub("<br />", " ", quotes[i])
        quotes[i] = re.sub("&#39;", "\'", quotes[i])
    return quotes


def parse_authors(authors: List[str]) -> List[str]:
    """
    Takes in a list of unformatted author strs and pulls out the html jargon.
    """
    for i in range(len(authors)):
        authors[i] = re.split(".*\n *", authors[i], 1)[1]
        authors[i] = re.sub(",", "", authors[i])
    return authors


def main():
    """
    Optional driver for the program.
    Takes in urls from input.txt and outputs to output.txt.
    """
    urls = []
    fp = open("input.txt", "r", newline="\n")
    lines = fp.readlines()
    fp.close()
    [urls.append(line) for line in lines if len(line) > 0]
    quotes = scrape_quotes(urls)
    fp = open("output.txt", "w", newline="\n")
    for quote in quotes:
        try:
            fp.write(quote)
            fp.write("\n")
        except UnicodeEncodeError:
            pass
    fp.close()


if __name__ == "__main__":
    main()
