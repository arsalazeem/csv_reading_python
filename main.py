import csv
import json
import chardet
import io


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def show_data(data, data_type=None):
        if data_type is None:
            print(data)
        elif data_type == 'json':
            print(json.dumps(data, indent=4))

    def read_data(self):
        data = []
        try:
            with open(self.file_path, 'rb') as csv_file:
                raw_data = csv_file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
                csv_file.seek(0)
                reader = csv.reader(io.TextIOWrapper(csv_file, encoding=encoding))
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", str(e))
        self.show_data(data)
        return data

    @staticmethod
    def dump_json_data(data, filename):
        with open(f'{filename}.json', 'w') as infile:
            json.dump(data, infile, indent=4)

    def read_data_as_json_string(self):
        self.show_data(self.read_data(), 'json')
        return json.dumps(self.read_data(), indent=4)

    def read_csv_data_and_dump_as_json_file(self, filename=None):
        if filename is None:
            filename = self.file_path.replace('.csv', '')
        if '.json' in filename:
            filename = filename.replace('json', '')
        self.dump_json_data(self.read_data(), filename)


if __name__ == '__main__':
    file_path = "csv_files/Sample-Spreadsheet-100-rows.csv"
    reader = CSVReader(file_path)
    reader.read_data()
    reader.read_data_as_json_string()
    reader.read_csv_data_and_dump_as_json_file()
