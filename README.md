## Noelia First Professional Code

Yay! Me Encantaaa :fire:
## Requires:

python 3

## Limitations:

This program can only process `.xls` files. `.xlsx` files are __not processable__. 

- references: [XLSX not supported](https://stackoverflow.com/questions/65254535/xlrd-biffh-xlrderror-excel-xlsx-file-not-supported)

## How to Run

1. Install packages `pip install pandas xlrd json`

2. Run the main script to convert json into directories `python presentaciones.py path_to_xls_file path_to_write_output name_of_output_folder`


## Assumptions

There is a big assumption that the excel table is formatted like:

| Nombre de la cuenta | Nombre de la oportunidad | 
|----------|---------------|
| google   | manager       | 
| google   | intern        |
| safari   | intern        |
| explorer | developer     |
| opera    | admin         |