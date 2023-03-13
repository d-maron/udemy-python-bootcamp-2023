import requests, bs4, lxml

base_url = 'http://quotes.toscrape.com/page/{}'

quote_parent = '.quote'
quote_class = '.text'
top_tag_parent = '.tag-item'

authors = set()
quotes = []
top_tags = []

page = 1
while True:
    url = base_url.format(page)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content, 'lxml')
    if 'No quotes found!' in soup.text:
        break

    auth_tmp = soup.select('.author')
    for i in auth_tmp:
        authors.update(i.contents)

    quotes_tmp = soup.select(quote_parent)
    for q in quotes_tmp:
        for item in q.select(quote_class):
            quotes.append(item.text)
    page += 1


tags_tmp = soup.select(top_tag_parent)
for t in tags_tmp:
    for item in t.select('a'):
        top_tags.append(item.contents[0])

print('\nAUTHORS:\n', authors)
print('\nQUOTES:\n', quotes)
print('\nTOP TAGS:\n', top_tags)
