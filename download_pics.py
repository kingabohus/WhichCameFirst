import wikipedia
import requests
import json
import urllib.request


WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='

def get_wiki_image(search_term):
    try:
        result = wikipedia.search(search_term, results = 1)
        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title = result[0])
        title = wkpage.title
        response  = requests.get(WIKI_REQUEST+title)
        json_data = json.loads(response.text)
        img_link = list(json_data['query']['pages'].values())[0]['original']['source']
        return img_link
    except:
        return 0

with open("dataset.txt", 'r') as file:
    links = [line.split('\t')[2] for line in file]

for i in range(len(links)):
    link = links[i]
    link = link.split("/")[2]
    link = link.replace('_'," ")
    print(link)

    wiki_image_url = get_wiki_image(link)
    if wiki_image_url != 0:
        # img_data = requests.get(wiki_image_url).content
        # with open('images/image_{}'.format(i), 'wb') as handler:
        #     handler.write(img_data)
        print(wiki_image_url)
        urllib.request.urlretrieve(wiki_image_url, 'images/image_{}.jpg'.format(i))
    else:
        try:
            wikipage = wikipedia.page(link)
            for wiki_image_url in wikipage.images:
                if wiki_image_url.split('.')[-1] == "jpg":
                    print("special case")
                    print(wiki_image_url)
                    urllib.request.urlretrieve(wiki_image_url, 'images/image_{}.jpg'.format(i))
                    break
        except:
            pass


