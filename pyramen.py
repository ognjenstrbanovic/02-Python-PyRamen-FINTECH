# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('csv_data/menu_data.csv')
sales_filepath = Path('csv_data/sales_data.csv')


# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []


# @TODO: Read in the menu data into the menu list

# Open the csv file as an object
with open(menu_filepath, 'r') as menu_csv_file:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    menu_csv_reader = csv.reader(menu_csv_file, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    menu_csv_header = next(menu_csv_reader)

    for row in menu_csv_reader:
        menu.append(row)


# @TODO: Read in the sales data into the sales list

# Open the csv file as an object
with open(sales_filepath, 'r') as sales_csv_file:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    sales_csv_reader = csv.reader(sales_csv_file, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    sales_csv_header = next(sales_csv_reader)

    for row in sales_csv_reader:
        sales.append(row)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

for row in sales:
    print(row)

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(row[3])
    menu_item = row[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
