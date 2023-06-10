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
        url = f"https://api.isthereanydeal.com/v01/game/prices/?key={key}&plains={g}&country=US&shops=steam"
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

if __name__ == "__main__":
    gameUrls()