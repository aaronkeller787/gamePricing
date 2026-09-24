# gamePricing

This project uses the **IsThereAnyDeal.com API** to extract game pricing data from an external source, transform game names into a format compatible with the API, and deliver the resulting pricing information through email.

The script is designed to run automatically using Linux `cron`.

## 🚀 Project Approach

### 📚 1. Information Gathering

```text
Created a list of games to monitor and stored them in a text file.

The script reads each game name from games.txt and prepares the
information for use with the IsThereAnyDeal.com API.
```

### 🧩 2. Data Transformation

```text
Game names are transformed into the URL convention required by
IsThereAnyDeal.com.

The formatted names are then used to generate the URLs required
to retrieve pricing information for each game.
```

### 🛠️ 3. Data Extraction

```text
Generated URLs are used to retrieve current pricing information
from IsThereAnyDeal.com.

The script extracts the relevant game name and current price
from the returned data.
```

### 📧 4. Output

```text
The extracted pricing information is formatted into a simple
report containing the game name and current price.

The report is then sent via email.
```

### ⏰ 5. Automation

```text
The script is executed automatically each morning using Linux cron.

Cron Schedule:
0 7 * * * /path/to/directory/bin/pythonversion /path/to/directory/example.py

This runs the script daily at 7:00 AM.
```

## 🔧 Python Libraries Used

```text
requests — for communicating with the IsThereAnyDeal.com API.
```

## 📄 Input

Game names are stored in `games.txt`, with one game per line.

```text
Cyberpunk 2077
Baldur's Gate 3
Stardew Valley
```

## 📤 Output

The script emails the current pricing information for the games being monitored.

```text
Cyberpunk 2077 - $XX.XX
Baldur's Gate 3 - $XX.XX
Stardew Valley - $XX.XX
```

## 🐧 Environment

The project uses a Python virtual environment to isolate its dependencies.

The script can be executed manually with:

```bash
/path/to/directory/bin/pythonversion /path/to/directory/example.py
```
