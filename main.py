import requests, bs4

response = requests.get('http://rss.slashdot.org/Slashdot/slashdot')
responsesoup = bs4.BeautifulSoup(response.text)

linksoups = []
linktexts = []
linkimageurls = []

for link in responsesoup.find_all('link'):
    url = link.text
    linkresponse = requests.get(url) # add support for relative urls with urlparse
    soup = bs4.BeautifulSoup(linkresponse.text)
    linksoups.append(soup)

    linktexts.append(soup.find('body').text)
    # Append all text between tags inside of the body tag to the second list

    images = soup.find_all('img')
    imageurls = []
    # get the src attribute of each <img> tag and append it to imageurls
    for image in images:
        imageurls.append(image['src'])
    linkimageurls.append(imageurls)
print linkimageurls

