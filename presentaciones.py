
# FOLDER LOCATION
# JSON FILE NAME
# python presentaciones.py JSON_FILE_NAME EXCEL_SHEET_NAME FOLDER_LOCATION
# 
# 
# python presentaciones.py /Users/Noelia/something.xlxs /Users/Noelia/Accounts
# INPUT goes into function and makes OUTPUT
# when output is complete, make a new folder at FOLDER_LOCATION
# 
# OUTPUT goes into function and does:
# for every key in dictionary create folder KEY 
# for every value in key, create folder with name VALUE

import os
import json
import sys
from datetime import datetime

current_date = datetime.today().strftime('%Y-%m-%d')

path_to_json_file = sys.argv[1]
path_to_output = sys.argv[2]
output_directory_name = "accounts-" + current_date
f = open(path_to_json_file,)

data = json.load(f)
# data = {
#   "accounts": {
#     "1": "Google",
#     "2": "safari",
#     "3": "explorer",
#     "4": "Google",
#     "5": "safari"
#   },
#   "opportunities": {
#     "1": "Developer",
#     "2": "Intern",
#     "3": "Janitor",
#     "4": "Manager",
#     "5": "Idiota"
#   }
# }
print("Grouping accounts from " + path_to_json_file + " to " + path_to_output + "/" + output_directory_name)

def groupOpportunitiesByAccount(accounts, opportunities):
  grouped_accounts = {}
  for account_row in accounts: 
    account_name = accounts[account_row]
    if account_name not in grouped_accounts:
      # add account name to grouped accounts 
      grouped_accounts[account_name] = []

    opportunity = opportunities[account_row]

    # push opportunity into the list 
    grouped_accounts[account_name].append(opportunity)

  return grouped_accounts





# take transformed data and it needs to:
# for every key in transformed data create a directory at  OUTPUT_FILE_PATH 
# for every item in list create a directory at OUTPUT_FILE_PATH/<account>/<opportunity>

def createDirectoryTree(grouped_accounts):
  # create a directory to store accounts 
  root_directory_path = os.path.join(path_to_output, output_directory_name) 
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


opportunities_grouped_by_account = groupOpportunitiesByAccount(data["accounts"], data["opportunities"])
createDirectoryTree(opportunities_grouped_by_account)

print("Complete!")
print(path_to_output + "/" + output_directory_name)