# USAGE:
# python presentaciones.py EXCEL_FILE_PATH OUTPUT_FOLDER_LOCATION OUTPUT_FOLDER_NAME
# 
# 
# 
# command line arguments:
# - excel file path: required
# - output folder location: required
# - output folder name: required required

# EXAMPLE
# python presentaciones.py /Users/Noelia/something.xlxs /Users/Noelia/Accounts accounts_20201

# PSEUDO CODE
# Step 1: Obtain Input from Excel File
# Step 2: Convert Input into JSON
# Step 3: Group Accounts by Opportunities
# Step 4: Write folders based on groupings!

import os
import json
import sys
import pandas
from datetime import datetime

current_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

path_to_excel_file = sys.argv[1]
path_to_output = sys.argv[2]

output_directory_name = "accounts-" + current_date if len(sys.argv) == 2 else sys.argv[3]



# data = {
#   "Nombre de la cuenta": {
#     "1": "Google",
#     "2": "safari",
#     "3": "explorer",
#     "4": "Google",
#     "5": "safari"
#   },
#   "Nombre de la oportunidad": {
#     "1": "Developer",
#     "2": "Intern",
#     "3": "Janitor",
#     "4": "Manager",
#     "5": "Idiota"
#   }
# }

def convertExcelToJson(path_to_excel_file):
  print("Converting excel file " + path_to_excel_file + " to JSON")
  excel_data_df = pandas.read_excel(path_to_excel_file)
  json_str = excel_data_df.to_json()
  return json.loads(json_str)


# data is in the form { [column]: { 1: row, 2: row} }
# there is an assumption the first column of the xls sheet is the grouped value
# column A is accounts, column B is opportunities
def groupOpportunitiesByAccount(data):
  print("Grouping opportunities by account")
  columns = data.keys()
  accounts = columns[0]
  opportunities = columns[1]
  grouped_accounts = {}

  accounts_data = data[accounts]
  opportunities_data = data[opportunities]
  for account_row in accounts_data:

    account_name = accounts_data[account_row]
    if account_name not in grouped_accounts:
      # add account name to grouped accounts 
      grouped_accounts[account_name] = []

    opportunity = opportunities_data[account_row]

    # push opportunity into the list 
    grouped_accounts[account_name].append(opportunity)

  return grouped_accounts





# take transformed data and it needs to:
# for every key in transformed data create a directory at  OUTPUT_FILE_PATH 
# for every item in list create a directory at OUTPUT_FILE_PATH/<account>/<opportunity>

def createDirectoryTree(grouped_accounts):
  # create a directory to store accounts 
  root_directory_path = os.path.join(path_to_output, output_directory_name) 
  print("Creating directory tree at " + root_directory_path)
  os.mkdir(root_directory_path)

  # loop over accounts and create dirs
  for account in grouped_accounts:
    # "Google"
    # "Safari"
    account_path = os.path.join(root_directory_path, account)
    os.mkdir(account_path)
    # loop over opportunites in account
    opportunities = grouped_accounts[account]
    for opportunity in opportunities:
      opportunity_path = os.path.join(account_path, opportunity)
      os.mkdir(opportunity_path)



data = convertExcelToJson(path_to_excel_file)
opportunities_grouped_by_account = groupOpportunitiesByAccount(data)
createDirectoryTree(opportunities_grouped_by_account)

print("Complete!")
print(path_to_output + "/" + output_directory_name)