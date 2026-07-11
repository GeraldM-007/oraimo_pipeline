# Oraimo Kenya e-commerce Pipeline
A Python ETL pipeline that scrapes newly added products from oraimo Kenya and loads everything into a cloud (aiven) PostgreSQL database for analysis.

## What it does
- Scrapes newly added (new arrivals) products from oraimo Kenya's e-commerce plarform across multiple pages
- Loads the dataset into structured table in acloud-hosted PostgreSQL database on Aiven
- The result is a products table ready for SQL analysis or dashboarding. 

## Project structure
```text
oraimo-pipeline/
│
├── extract.py        # Scrapes oraimo kenya website
├── transform.py      # Cleans data
├── load.py           # Creates schema/tables, loads to PostgreSQL
├── main.py           # Runs the full pipeline end to end
├── config.py         # Non-secret config (URLs, page count, etc.)
├── .env              # DB credentials
├── requirements.txt  
└── README.md
```
## How to run it locally
1. Clone the repo
```bash
git clone https://github.com/GeraldM-007/oraimo_pipeline.git
cd oraimo_pipeline
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Set up your .env file

Create a .env file in the root folder:
```bash
db_uri=postgresql://user:password@host:port/dbname
```
You can use a free Aiven, Supabase, or local PostgreSQL instance.

4. Run the pipeline
```bash
python main.py
```
The pipeline will:
- Scrape 15 pages from oraimo ke
- Pull newly added products labeled with the tag new arrival
- Create the schema and tables if they don't exist
- Load everything into PostgreSQL

## Known limitations
Only scrapes newly added products labeled with the tag new arrival 
Oraimo's HTML structure can change without notice — if scraping breaks, the CSS class selectors in extract.py likely need updating
No retry logic yet for failed page requests beyond skipping and logging

## Tech stack
Python — core language
BeautifulSoup + Requests — HTML scraping
Pandas — data cleaning and transformation
SQLAlchemy — database connection and loading
PostgreSQL on Aiven — cloud database
python-dotenv — secrets management

## Sample Loaded data in the database
<img width="1619" height="1001" alt="image" src="https://github.com/user-attachments/assets/bc6bba03-2e01-4aa4-a8a5-b44c65aaadf8" />
