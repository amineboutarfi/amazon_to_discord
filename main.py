from playwright.sync_api import sync_playwright
from discord import SyncWebhook
from discord import Embed

from datetime import datetime
import sys

# This webhook is just an example that was already deleted. Use yours. 
# https://discord.com/api/webhooks/1109518884131835984/y5afluDw7XU34cDTWflvuc71maNfvxIN4qr_vkmB02jaaAquHlWdEpaUSVh-ULI5_np_

def send_to_discord(embed):
    webhook = SyncWebhook.partial('1109518884131835984', 
                              'y5afluDw7XU34cDTWflvuc71maNfvxIN4qr_vkmB02jaaAquHlWdEpaUSVh-ULI5_np_')
    webhook.send(username='Amazon BOT', embed=embed)

def main():
   
    for link_index, link in enumerate(products_links):
        
        print(f'Scraping Product: {link_index}')

        page.goto(link, wait_until='domcontentloaded')
        page.wait_for_timeout(5_000) 

        title_xpath = '//span[@id="productTitle"]'
        original_price_xpath = '//span[contains(@class, "a-price a-text-price")]//span[@class="a-offscreen"]'
        discounted_price_xpath = '//span[contains(@class, "priceToPay")]//span[@class="a-offscreen"]'

        title = page.locator(title_xpath).inner_text()
        original_price = page.locator(original_price_xpath).all()[0].inner_text()
        discounted_price = page.locator(discounted_price_xpath).all()[0].inner_text()
        
        print(f'Title: {title}\nOriginal Price: {original_price}\nDiscounted Price: {discounted_price}\nLink: {link}')

        em = Embed(title=title, description='', color=242424)
        em.add_field(name='URL', value= link, inline=False)
        em.add_field(name='Original Price', value=original_price, inline=False)
        em.add_field(name='Discounted Price', value=discounted_price, inline=False)
        em.timestamp = datetime.now()
        em.set_footer(text='Powered by Amazon Bot')
        
        send_to_discord(em)

if __name__ == '__main__':
    
    with open('products_links.txt') as f:
        products_links = f.readlines()

    if len(products_links) == 0:
        print('No links found in products_links.txt')
        sys.exit()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) 
        context = browser.new_context()
        page = context.new_page()

        main()
