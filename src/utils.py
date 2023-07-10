import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        logging.info(f'Saving the object to : {file_path}')
        
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        
        logging.info('Object successfully saved')

    except Exception as e:
        logging.info('Exception occured while saving object in utils.py file')
        raise CustomException(e, sys)