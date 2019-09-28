import logging
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

logging.basicConfig(filename=dir_path+'/../example.log',level=logging.DEBUG)
