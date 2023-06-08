import requests
from constants import key
from pprint import pprint


def getGames():

    allPrices = {}

    game = input('Please enter in the game name to check pricing: ')
    gameName = ''.join(game.split()).lower()

    url = f"https://api.isthereanydeal.com/v01/game/prices/?key={key}&plains={gameName}&country=US&shops=steam"

    response = requests.get(url)

    data = response.json()
    currentPrice = (data['data'][gameName]['list'][0]['price_new'])
    print(game.title() + " is currently: " + f"${currentPrice}")


    allPrices[game.title()] = currentPrice

    print(allPrices)


#pprint(data)

getGames()