import requests, bs4, lxml

base_url = 'http://quotes.toscrape.com/page/{}'

quote_class = '.text'
top_tag_parent = '.tag-item'

authors = set()
quotes = []
top_tags = []

page = 1
while True:
    url = base_url.format(page)
    res = requests.get(url)
    if 'No quotes found!' in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    auth_tmp = soup.select('.author')
    for i in auth_tmp:
        authors.update(i.contents)

    quotes_tmp = soup.select(quote_class)
    for q in quotes_tmp:
        quotes.append(q.text)
    page += 1


tags_tmp = soup.select(top_tag_parent)
for t in tags_tmp:
    for item in t.select('a'):
        top_tags.append(item.text)

print('\nAUTHORS:\n', authors)
print('\nQUOTES:\n', quotes)
print('\nTOP TAGS:\n', top_tags)
