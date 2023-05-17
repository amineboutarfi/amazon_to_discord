from playwright.sync_api import sync_playwright
import sys


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
