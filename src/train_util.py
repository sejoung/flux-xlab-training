import json
import os


def create_json_files(directory, script_data: str):
    file_names = os.listdir(directory)
    caption = {"caption": script_data}
    for idx, item in enumerate(file_names):
        filename, fileExtension = os.path.splitext(item)
        with open(f"{directory}/{filename}.json", "w", encoding="utf-8") as json_file:
            print(f"Creating {filename}.json")
            json.dump(caption, json_file, indent=4)
