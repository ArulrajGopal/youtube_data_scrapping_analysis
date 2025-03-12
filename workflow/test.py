
from config import *
from utility import *
from datetime import datetime
import pandas as pd

channel_playlist_dict = {'UCKTWY-rVwUqCxrVmPOlJyjA': 'UUKTWY-rVwUqCxrVmPOlJyjA',}


video_response_lst = get_video_header("UUKTWY-rVwUqCxrVmPOlJyjA")

dic = {}

for i in range(len(video_response_lst)):
    response = video_response_lst[i]["items"]
    # print(response)
   
    for j in range(len(response)):
        key = response[j]["contentDetails"]["videoId"]
        value = response[j]
        dic[key] = value


print(dic)






