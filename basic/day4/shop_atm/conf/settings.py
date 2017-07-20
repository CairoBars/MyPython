#Author:Cairo Li
import os
import sys
import logging

#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DATABASE={
    'engin':'file_storage',
    'name':'accounts',
    'path':'%s/db'%BASE_DIR
}

LOG_LEVEL=logging.INFO