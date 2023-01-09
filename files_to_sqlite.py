import os
import zipfile
import pandas as pd
import sqlite3

# create a connection to the sqlite databases
conn_retail = sqlite3.connect("retail.db")
conn_wholesale = sqlite3.connect("wholesale.db")

# initialize a counter
i = 0

# create a flag to control the loop
flag = True

# create the while loop
while flag:
    # create the file name
    file_name = "file_{}.zip".format(i)

    # check if the file exists
    if os.path.exists(file_name):
        # open the zip file
        with zipfile.ZipFile(file_name) as zip_file:
            # extract the excel files
            zip_file.extractall()

            # try to read the retail excel file into a dataframe
            try:
                retail_df = pd.read_excel("retail.xlsx")
            except:
                # set the dataframe to None if the file is corrupt
                retail_df = None

            # try to read the wholesale excel file into a dataframe
            try:
                wholesale_df = pd.read_excel("wholesale.xlsx")
            except:
                # set the dataframe to None if the file is corrupt
                wholesale_df = None

            # get the sheet names
            sheet_names = retail_df.sheet_names

            # loop through the sheet names
            for sheet_name in sheet_names:
                # check if the retail dataframe is not None
                if retail_df is not None:
                    # save the sheet as a csv file
                    retail_df.parse(sheet_name).to_csv("{}.csv".format(sheet_name))

                    # read the csv file into a dataframe
                    retail_df = pd.read_csv("{}.csv".format(sheet_name))

                    # save the dataframe to the sqlite database
                    retail_df.to_sql("{}".format(sheet_name), conn_retail, if_exists="replace")

                    # delete the csv file
                    os.remove("{}.csv".format(sheet_name))

                # check if the wholesale dataframe is not None
                if wholesale_df is not None:
                    # save the sheet as a csv file
                    wholesale_df.parse(sheet_name).to_csv("{}.csv".format(sheet_name))

                    # read the csv file into a dataframe
                    wholesale_df = pd.read_csv("{}.csv".format(sheet_name))

                    # save the dataframe to the sqlite database
                    wholesale_df.to_sql("{}".format(sheet_name), conn_wholesale, if_exists="replace")

                    # delete the csv file
                    os.remove("{}.csv".format(sheet_name))

        # increment the counter
        i += 1
    else:
        # set the flag to False to exit the loop
        flag = False

# close the database connections
conn_retail.close()
conn_wholesale.close()
