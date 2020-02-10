import requests
from bs4 import BeautifulSoup


#search words
def search(word):
    #global r 
    url = 'https://trends.google.com/trends/explore?q=' + word
    r = requests.get(url)
    get = BeautifulSoup(r.text, "html.parser")
    finder(word, get)

def finder(word, s):
    print('Word Searched : ' + word)
    print(s)
    points_tag = s.find(class_='progress-value')
    print(points_tag)
    points = points_tag['content']
    print('Points Got : ' + points)


#get input
def getter():
    print('Enter any words just make sure it is popular, so it gains some nice points...\n')
    word = input('ENTER A WORD : ')
    search(word)


if __name__ == '__main__':
    players = input('NO. OF PLAYERS : ')
    while(players):
        getter()
        players -= 1



