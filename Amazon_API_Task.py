import mysql.connector
from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
from paapi5_python_sdk.rest import ApiException
import streamlit as st
import pandas as pd

db_config = {
    'host': 'localhost',          
    'user': 'root',               
    'password': '',              
    'database': 'amazon_data_scraping'     
}

def save_to_mysql(data):
    """
    Save Amazon product data into the MySQL database.
    """
    connection = None
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Insert Query
        query = """
        INSERT INTO amazon_datas (ITEM_NUMBER, PRODUCT_TITLE, URL, PRICE,CATEGORY_NAME)
        VALUES (%s, %s, %s, %s, %s )
        """
        cursor.execute(query, data)
        connection.commit()
        st.success(f"Data inserted for ASIN: {data[0]}")
    except mysql.connector.Error as e:
        st.error(f"Error inserting into MySQL: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def fetch_from_mysql():
    """
    Retrieve data from the MySQL database.
    """
    connection = None
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Select Query
        query = "SELECT * FROM amazon_datas"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Return data as a list of dictionaries
        return rows
    except mysql.connector.Error as e:
        st.error(f"Error retrieving from MySQL: {e}")
        return []
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def search_items(keywords):
    """
    Search items on Amazon using the specified keywords and save to MySQL.
    """
    access_key = ""
    secret_key = ""
    partner_tag = ""
    host = "webservices.amazon.in"
    region = "eu-west-1"
    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )
    search_index = "All"
    item_count = 5
    search_items_resource = [
        SearchItemsResource.ITEMINFO_TITLE,
        SearchItemsResource.OFFERS_LISTINGS_PRICE,
    ]

    try:
        search_items_request = SearchItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            keywords=keywords,
            search_index=search_index,
            item_count=item_count,
            resources=search_items_resource,
        )
    except ValueError as exception:
        st.error(f"Error in forming SearchItemsRequest: {exception}")
        return

    try:
        response = default_api.search_items(search_items_request)

        if response.search_result is not None:
            for item in response.search_result.items:
                asin = item.asin if item.asin else "N/A"
                title = (
                    item.item_info.title.display_value
                    if item.item_info and item.item_info.title
                    else "N/A"
                )
                detail_page_url = item.detail_page_url if item.detail_page_url else "N/A"
                buying_price = (
                    item.offers.listings[0].price.display_amount
                    if item.offers and item.offers.listings and item.offers.listings[0].price
                    else "N/A"
                )
                category_name = keywords.capitalize()
                
            
                save_to_mysql((asin, title, detail_page_url, buying_price,category_name))

    except ApiException as exception:
        st.error("Error calling PA-API 5.0!")
        st.error(f"Status code: {exception.status}")
        st.error(f"Errors: {exception.body}")

    except Exception as exception:
        st.error(f"Exception: {exception}")


st.title("Amazon Product Search and Data Viewer")


keywords = st.text_input("Enter keywords for search:")
if st.button("Search"):
    if keywords.strip():
        st.info(f"Searching for: {keywords}")
        search_items(keywords.strip())
    else:
        st.warning("Please enter keywords to search.")


if st.button("Show Saved Data"):
    data = fetch_from_mysql()
    if data:
        df = pd.DataFrame(data, columns=["ID", "ITEM_NUMBER", "PRODUCT_TITLE", "URL", "PRICE","CATEGORY_NAME"])
        
        # Modify the URL column to make links clickable
        df["URL"] = df["URL"].apply(lambda url: f"[View Product]({url})" if url != "N/A" else "N/A")

        st.subheader(f"Results for: {keywords}")
        
        st.write("Saved Data:")
        # Use Streamlit's st.markdown for clickable links
        st.write(df.to_markdown(index=False), unsafe_allow_html=True)
    else:
        st.info("No data found in the database.")