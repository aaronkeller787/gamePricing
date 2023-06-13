# gamePricing
Using the API from Isthereanydeal.com to check pricing of games within the games.txt file.
The script reads in data, converts the names to match the URL convention for the Isthereanydeal.com website, and stores that information
After generating the necessary URLs, current prices are checked, and game name + current price is emailed out


Schedule cron using virtualenv
0 7 * * * /path/to/directory/bin/pythonversion /path/to/directory/example.py
