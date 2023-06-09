import requests
from constants import key

def gameUrls():

    games = []
    urlList = []
    originalNames = []

    file = open('games.txt', 'r')
    for f in file:
        names = f.strip()
        originalNames.append(names)
        gameName = ''.join(f.split()).strip().lower()
        games.append(gameName)

    for g in games:
        url = "https://api.isthereanydeal.com/v01/game/prices/?key=bb30d49c555921023d021eb8c8f5a314ca37655e&plains={}&country=US&shops=steam".format(g) 
        urlList.append(url)

    checkPrices(games, urlList, originalNames) 

def checkPrices(games, urlList, originalNames):

    allPrices = {}
    count = 0

    for u in urlList:
        
        response = requests.get(u)
        data = response.json()
        currentPrice = (data['data'][games[count]]['list'][0]['price_new'])
            
        allPrices = {originalNames[count]: currentPrice}

        count+=1

        print(allPrices)

gameUrls()