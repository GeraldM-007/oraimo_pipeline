import pandas as pd

def transform_products(raw_products):
    
    df = pd.DataFrame(raw_products)
    
    #drop dublicates(if any)
    df.drop_duplicates(subset="item_id", inplace=True)
    
    #clean price column - remove "ksh" and commas then convert to float
    for col in ["current_price"]:
        df[col] = df[col].str.replace("KES", "").str.replace(",", "").str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce') #invalid errors if any, become NaN
        
        #drop rows where critical field are missing
        df.dropna(subset=["item_id", "item_name", "current_price"], inplace=True)
    
    return df


    