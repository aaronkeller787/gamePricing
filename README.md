gamePricing

A Python script that uses the IsThereAnyDeal.com API to monitor current game prices and email price updates.

Overview

gamePricing reads a list of game names from games.txt, converts those names into the URL format required by IsThereAnyDeal.com, and generates the necessary URLs to retrieve pricing information.

The script then checks the current price of each game and emails the game name along with its current price.

The project is designed to run automatically on a schedule using cron.

How It Works

The workflow is:

Read game names from games.txt.
Convert game names into the URL convention used by IsThereAnyDeal.com.
Generate the required API/website URLs.
Query the current pricing information.
Extract the game name and current price.
Email the results.
Run automatically on a scheduled cron job.
Requirements
Python 3
IsThereAnyDeal.com API access
Python virtual environment
Email/SMTP configuration
Linux system with cron for scheduled execution
Running Manually

The script can be run manually using the Python interpreter from the virtual environment:

/path/to/gamePricing/.venv/bin/python /path/to/gamePricing/example.py
Scheduling

The script can be scheduled to run every day at 7:00 AM using cron.

Open the user's crontab:

crontab -e

Add:

0 7 * * * /path/to/directory/bin/pythonversion /path/to/directory/example.py

For a virtual environment, this would typically look similar to:

0 7 * * * /path/to/gamePricing/.venv/bin/python /path/to/gamePricing/example.py

This runs the script every day at 7:00 AM.

Example Output

The resulting email contains the current price for each monitored game.

Example:

Cyberpunk 2077 - $XX.XX
Baldur's Gate 3 - $XX.XX
Stardew Valley - $XX.XX
Purpose

This project demonstrates using a web API, processing external data, automating repetitive tasks, and delivering the resulting information through email.

It also demonstrates how a Python script can be combined with Linux cron to create a scheduled automation workflow.
