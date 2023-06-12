import requests
import smtplib
import os
from email.message import EmailMessage

from constants import key, sender, recipients

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

    count = 0

    for u in urlList:

        response = requests.get(u)
        data = response.json()
        currentPrice = (data['data'][games[count]]['list'][0]['price_new'])
        allPrices = {originalNames[count]: currentPrice}
        count+=1
        
        writeToFile(allPrices)

def writeToFile(allPrices):

    with open('gameprices.txt', 'a') as f:
        for k, v in allPrices.items(): 
            f.write(f'{k}: {v}\n')

def sendEmail():

    with open('gameprices.txt') as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
        
    msg['Subject'] = 'Game Prices'
    msg['From'] = sender
    msg['To'] = recipients

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

    cleanup()

def cleanup():
    
    if os.path.exists('gameprices.txt'):
        os.remove('gameprices.txt')
    else:
        pass

if __name__ == "__main__":
    gameUrls()
    sendEmail()
