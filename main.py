from extract import oraimo_scrape
from config import url, pages, headers
from transform import transform_products
from load import load_data

def main():
    raw_products = oraimo_scrape(url, pages, headers)
        
    products_df = transform_products(raw_products)
    
    load_data(products_df)
    

if __name__ == "__main__":
    main()
