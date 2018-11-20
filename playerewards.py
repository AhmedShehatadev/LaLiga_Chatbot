import requests
from bs4 import BeautifulSoup
from collections import defaultdict
'''
This function crawls wiki reward page to fetch tables
get rewards and players in dectionary
'''

def get_via_crawling_info_about_rewards(name=None):
    website_url = requests.get("https://en.wikipedia.org/wiki/La_Liga_Awards").text
    soup = BeautifulSoup(website_url,'lxml')
    My_tables = soup.findAll("table",{"class":"multicol"})
    playerandhisaward = ""
    returneddict = defaultdict(list)
    for table in My_tables:
        eachtable = table.find("table",{"class":"wikitable"})
        rowsoneachtable = eachtable.findAll("tr")
        eachtableheader = eachtable.find("th") 
        for onerow in rowsoneachtable:
            childofeachrow = onerow.findChildren(recursive=False)
            for text in childofeachrow:
                ## to be modified by slicing
                if "best " in text.get_text().lower():
                        continue         
                returneddict[eachtableheader.get_text()].append(text.get_text().lower()) 
                break
    for key, val in returneddict.items():
       newlist = list(map(str.strip, val))
       for playername in newlist: 
         if name in playername:
           playerandhisaward = key + "|" + playername
    return playerandhisaward
'''
if __name__ == "__main__":
    response = get_via_crawling_info_about_rewards("alex")
    print(response.split("|")[0])
'''    