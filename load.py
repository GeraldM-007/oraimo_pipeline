import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

def get_engine():
    db_uri = os.getenv("db_uri")
    
    return create_engine(db_uri)

def create_schema_and_tables(engine):

    with engine.begin() as conn:
        conn.execute(text("""
            CREATE SCHEMA IF NOT EXISTS oraimo_data
        """))

        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS oraimo_data.new_oraimo_products (
                item_id VARCHAR(30) PRIMARY KEY,
                item_name TEXT NOT NULL,
                item_category VARCHAR(50),
                current_price NUMERIC(10,2) NOT NULL
            )
        """))

    print("Schema and table are ready!")
    
def load_data(products_df):
    engine = get_engine()
    
    #create the schema and tables first
    create_schema_and_tables(engine)
    
    #load the products
    try:
        products_df.to_sql(name="new_oraimo_products", con=engine, schema = "oraimo_data", if_exists="replace", index=False)
        print("Product loaded successfully")
        
    except Exception as e:
        print(f"Failed to load products: {e}")