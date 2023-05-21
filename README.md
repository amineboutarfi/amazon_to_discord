# Amazon To Discord Bot

This is simple scraper that uses Playwright to extract data from Amazon.com and send it to a Discord server via a Webhook. 

This example is made for educational purposese.

This script is easy to customize.

Note that amazon shows prices in multiple HTML/CSS tags depending on the product's state (availability, has discount...etc), and this requires to add all these cases' XPATHs. Which for now the bot don't have. and might throw erros in some cases.

Also note that the product I used in the products_links.txt file might not be available on amazon when you try the bot, use your own products links.

Important: Use your own Discord Webhook. Mine is already deleted and you will get an error. 

## To Install:
- (Optional: create & activate a virtual environment) `virtualenv venv`, then `source venv/bin/activate`

- `pip install -r requirements.txt`
- `playwright install chromium`

## to Run:
- `python3 main.py`
