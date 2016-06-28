import requests 
import json 

def get_one_url_from_wiki_search(word='Monty Python'):
    url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + word + "&limit=1&namespace=0&format=json"
    r = requests.get(url)
    content = json.loads(r.content)
    try:
        search = str(content[3][0])
    except:
        return 'https://en.wikipedia.org/wiki/Monty_Python' 

    return search 