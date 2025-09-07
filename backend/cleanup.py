from config import *
from config import *
from utility import *


table_name = "comment_details_raw"

if table_exists(table_name) is not None:
    delete_table(table_name)
    



