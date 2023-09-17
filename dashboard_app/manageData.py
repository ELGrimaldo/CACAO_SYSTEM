from pathlib import Path
import os
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = str(BASE_DIR) + '\\dashboard\\Data\\'

def list_files() -> list[str]:
    csv_files = os.listdir(DATA_DIR)
    return csv_files


class CacaoData:

    def __init__(self, file_name:str) -> None:
        self.file_name = file_name
        

    def validate_csv(self):
        if self.file_name in list_files():
            return True

    def get_features(self):
        if self.validate_csv():
            data_frame = pd.read_csv(f'{DATA_DIR+self.file_name}')
            data_frame_dict = data_frame.to_dict()
            return list(data_frame_dict.keys())

    def get_data(self) -> dict:
        if self.validate_csv():
            data_frame = pd.read_csv(f'{DATA_DIR+self.file_name}')
            return data_frame.to_dict()



if __name__ =='__main__':

    context = {}

    for file in list_files():
        data = CacaoData(file)
        data = data.get_data()
        print(data)