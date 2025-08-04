from datetime import datetime
from config import *
from utility import *


df = read_from_sql("video_header_stage")
video_id_list = df['video_id'].tolist()

video_id_list = ["g3qMaKz_PK4","6vrNQ1mxmHc","69bCP0XhAkk","XC22G-5TM24","2JzaTCVNaB4","ptEn_JBQ-sQ","UZzCpYIM5yA","qpuvNboIHUA","87QF7dyoVVQ"]


