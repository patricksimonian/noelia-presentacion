# INPUT:

#  {
#   accounts: {
#    1: account1, 
#   2: account2,
# },
#  opportunities: {
#   1: opportunity1,
#  2: opportunity2
#}
# } 
# ]
# OUTPUT
# {
#   account: [ opportunities ],
#   account: [ opportunities ],
#   account: [ opportunities ],
#   account: [ opportunities ],
# }
# 
# 
# 
# FOLDER LOCATION
# EXCEL FILE NAME
# python presentaciones.py EXCEL_FILE_NAME FOLDER_LOCATION
# 
# 

# INPUT goes into function and makes OUTPUT
# when output is complete, make a new folder at FOLDER_LOCATION
# 
# OUTPUT goes into function and does:
# for every key in dictionary create folder KEY 
# for every value in key, create folder with name VALUE

import os
import pandas

excel_data_df = pandas.read_excel('/Users/noelia.parada/Documents/Pyhton/pres.xlsx', sheet_name='uno')

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)


"accounts" : []