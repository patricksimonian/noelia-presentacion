# HOW TO 
# python excel2json.py <PATH TO EXCEL FILE>

import excel2json
import sys

excel_file_path = sys.argv[1]
print (excel_file_path)
excel2json.convert_from_file(excel_file_path)

