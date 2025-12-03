import csv
import json

class CSVMixin:
    @staticmethod
    def load(file):
        try:
            data = []
            with open(file, 'r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    data.append(row)
            return data
        except FileNotFoundError as e:
            raise FileNotFoundError(f"{e}: CSV file not found.")
        except csv.Error as e:
            raise csv.Error(f"CSV reading error: {e}")

    @staticmethod
    def write(result, file_name):
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

class JsonMixin():
    @staticmethod
    def load(file):
        try:
            with open(file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
           raise FileNotFoundError(f"{e}: JSON file not found.")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"{e}: Invalid JSON format in the file.")
        except Exception as e:
            raise Exception(f"{e}")

    @staticmethod
    def write(result, file_name):
        with open(file_name, 'w') as f:
            json.dump(result, f, indent=4)