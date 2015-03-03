from random import randint

import bs4

from scraper import find_term


def make_fake_soup(term):
    lists = ['<ul></ul>' for i in xrange(31)]

    # Subtract one since xrange isn't inclusive
    index = randint(0, 30)

    lists[index] = '<ul><li>%s</li></ul>' % term

    html_list = ['<html><body>']
    html_list.extend(lists)
    html_list.extend(['</body></html>'])

    html = ''.join(html_list)

    soup = bs4.BeautifulSoup(html)

    return soup, index

def test_find_term():
    term = 'Thing'
    soup, index = make_fake_soup(term)

    returned_index = find_term(soup, term)
    assert returned_index == index
