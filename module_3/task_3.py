from utils.file_utils import FileUtils


class CsvAndJson:
    """
    Read text from file [/resources/module_3/cars.csv]
    Use [csv] library to read file content.
    Convert data to [json] and save it in cars.json
    Use csv.DictReader, json.dump with indent=2, [with] for file creation
    """

    def convert_csv_to_json(self, file_path: str):
        data_from_csv: list = FileUtils.read_csv_file(file_path)
        FileUtils.write_json_file("module_3/cars.json", data_from_csv)


if __name__ == '__main__':
    csv_file_path: str = "module_3/cars.csv"
    CsvAndJson().convert_csv_to_json(csv_file_path)
