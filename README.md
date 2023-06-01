# Using CSV Reader Class
- You can use read_data method CSVReader to read data from a csv file.
- When creating an instance of CSVReader you need to provide filepath there.
# Dumping CSV file data into json
- After Creating instace of class CSVReader you can call ```` read_csv_data_and_dump_as_json_file ```` and you can provide any filename.
- By default it will a json file with same name as your csv file if you provide no name for your json file.
````
    file_path = "csv_files/Sample-Spreadsheet-100-rows.csv"
    reader = CSVReader(file_path)
    reader.read_csv_data_and_dump_as_json_file(file_path)