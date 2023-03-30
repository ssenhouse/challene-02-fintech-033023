# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
   
# This function creates a csv output file for the loans

# name of the cvs output csv file
output_csvpath = Path("./loan_qualifier_app/data/qualifiying_loans.csv")

#header names for csv file
output_header = ['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']

# Commented Out for Debugging
#output list to csv file
def save_csv(output_csvpath):
    
    with open(output_csvpath, "w") as output_csvfile:
        output_data =[]
        csvwriter = csv.writer(output_csvfile, delimiter=",")
        csvwriter = csv.writerow(output_header)

        for row in csvwriter:
            output_data.append(row)
    return output_data


      





