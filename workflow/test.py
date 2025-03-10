from config import *
from utility import *
from datetime import datetime
import pandas as pd



request = youtube.playlistItems().list(part='contentDetails',playlistId = "UUhaRiZ3h9JlLCeO2pdWkxMw",maxResults = 50)
response = request.execute()

print(response)

