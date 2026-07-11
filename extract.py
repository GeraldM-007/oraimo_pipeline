import requests
from bs4 import BeautifulSoup
from config import url, pages, headers

def oraimo_scrape(url, pages, headers):
    
    products = []
    
    for page in range(1, pages + 1):
        
        html_response = requests.get(f"{url}?page={page}", headers=headers)
        #print(type(html_response))
        
        #handle error when encountered then continue without breaking program
        if html_response.status_code != 200:
            print(f"Extraction failed for this page: {url}?page={page}")
            continue
        
        #parse the raw html into python objects
        soup = BeautifulSoup(html_response.text, 'html.parser')
        #print(type(soup))
        
        #find all products cards
        product_cards = soup.find_all("div", class_ = 'js_product site-product')
        
        for card in product_cards:
            #find the prices for products
            product_tag = card.find("span", class_ = "product-tag-new")
            
            #get only dicounted products
            if product_tag:
                products.append(
                    {
                        "item_id": card.find("a").get("data-id"),
                        "item_name": card.find("a").get("data-name"),
                        "item_category": card.find("a").get("data-category"),
                        "current_price": card.find("p", class_ = "product-price").find("span").get_text(strip=True)
                    }
                )
            
    
    return products