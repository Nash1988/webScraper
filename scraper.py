import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
hacker_soup = BeautifulSoup(res.text, 'html.parser')
links = hacker_soup.select('.titleline > a')
subtext = hacker_soup.select('.subtext')

#Sort the articles in a descending order by number of votes.
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['Votes'], reverse=True)

#Get article titles and subtext, return a dict of article with votes above 100.
def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.get_text()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].get_text().replace(' points', ''))
            if points > 99:
                hn.append({"Title": title, "Link": href, "Votes": points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))