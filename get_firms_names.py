'''Returns list containing id's and names of Chambers profiles'''
import requests
from lxml.html import fromstring
import settings as settings

IDS_LIST = settings.IDS_LIST
PUBLICATION_ID = settings.PUBLICATION_ID

def create_url(id, publication_id):
    return f"https://chambers.com/law-firm/-{publication_id}:{id}"

def get_title(url):
    try:
        page = requests.get(url)
    except Exception:
        pass
    return fromstring(page.content).findtext('.//title')


def format_title(title):
    title = title[0:title.find("|")-1]
    return title


FIRMS_DICT = {"id": "name"}
for id in IDS_LIST:
    id = id
    publication_id = PUBLICATION_ID
    url = create_url(id, publication_id)

    title = format_title(get_title(url))
    FIRMS_DICT.update({id : title})

    print(f"{url} --- {title}")

FIRMS_DICT = {key:val for key, val in FIRMS_DICT.items() if val != "Not found"}


with open('firms_dict.csv', 'w') as file:
    for key in FIRMS_DICT.keys():
        file.write("%s, %s\n"%(key, FIRMS_DICT[key]))
