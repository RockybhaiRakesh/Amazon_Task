
# Amazon_API_Task

This script interacts with an API to fetch and display key information about items, including ASIN, URLs, titles, and prices
Use Amazon's Search API to search for a product based on variable inputs 

## Features
Search Amazon Products: Uses the Amazon Product Advertising API (PA-API 5.0) to fetch product details based on keywords.

Save to MySQL Database: Stores product information such as ASIN, title, URL, price, category, and images in a database.

View Saved Data: Displays the saved data in a tabular format using Streamlit, with clickable product URLs.



## Prerequisites
Python 3.7+ (jupyter notebook)

MySQL database setup

Amazon PA-API 5.0 credentials (Access Key, Secret Key, Partner Tag)
## Installation

Install Amazon_API_Task with pip

Configure the database:

Ensure a MySQL database is running and create a database named amazon_data_scraping.

Create the amazon_datas table with the following schema:

```bash
  pip install paapi5-python-sdk
  pip install paAPI
  pip install pandas
  pip install streamlit

  database:
  CREATE TABLE amazon_datas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ITEM_NUMBER VARCHAR(50),
    PRODUCT_TITLE VARCHAR(255),
    URL TEXT,
    PRICE VARCHAR(50),
    CATEGORY_NAME VARCHAR(50),
    IMAGES TEXT
);

```
    
## Key Dependencies

mysql-connector-python: For database interaction.

streamlit: For building the web interface.

pandas: For handling and displaying tabular data.

paapi5-python-sdk: For Amazon PA-API 5.0 integration.
## Run Locally with Screenshot

Run command prompt

```bash
  jupyter notebook
```
Enter cmd for  jupyter notebook
![Screenshot 2024-12-17 172417](https://github.com/user-attachments/assets/9bacf311-b5bc-467f-b945-7792b3b91346)

Click the File
![Screenshot 2024-12-17 174052](https://github.com/user-attachments/assets/b33d9f60-ad02-4f6c-9c88-fa616597d4af)

create Database table

![Screenshot 2024-12-17 174936](https://github.com/user-attachments/assets/b67372e5-d351-4b29-baf5-fe60de77cf86)



how to open Streamlit for UI

```bash
  streamlit run Amazon_API_Task.py
```
![Screenshot 2024-12-17 174109](https://github.com/user-attachments/assets/0953ac89-1348-4962-8172-743154e73b8b)

UI Streamlit has bee views and search the products what do you want
click Search Button

![Screenshot 2024-12-17 175042](https://github.com/user-attachments/assets/f7739ae1-d019-4c3e-85fd-f236c5b3649d)

![Screenshot 2024-12-17 175653](https://github.com/user-attachments/assets/688bf877-0b78-4ac2-ae5e-79168e2db53d)

Datas has been added in Database

![Screenshot 2024-12-17 175824](https://github.com/user-attachments/assets/2a0133f2-7809-4457-aca7-3b6093608115)

Click the ``` Show Saved Data ``` button show all the datas from the database - Retrivedata

![Screenshot 2024-12-17 175959](https://github.com/user-attachments/assets/ac4cd0ff-a543-463d-b40a-1098ab4dabdc)




## Demo

Search API to search for a product Demo Video

https://github.com/user-attachments/assets/770b1bce-7bc1-4f65-8d20-4a90c8ee6e70

