'''Returns list containing id's and names of Chambers profiles'''
import requests
from lxml.html import fromstring
import settings as settings

IDS_LIST = settings.IDS_LIST

def create_url(id):
    return f"https://chambers.com/law-firm/-2:{id}"

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
    url = create_url(id)

    print(url)

    title = format_title(get_title(url))
    FIRMS_DICT.update({id : title})

FIRMS_DICT = {key:val for key, val in FIRMS_DICT.items() if val != "Not found"}


with open('firms_dict.csv', 'w') as file:
    for key in FIRMS_DICT.keys():
        file.write("%s, %s\n"%(key, FIRMS_DICT[key]))
