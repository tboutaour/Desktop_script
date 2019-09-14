import os
from datetime import datetime


FOLDER_TO_TRACK = "/Users/tonibous/Desktop"
BASE_FOLDER = "/Users/tonibous/Documents/Desktop_reminder/"

today = datetime.now()
folder_to_create = BASE_FOLDER+(str(today.strftime("%Y")+'-'+today.strftime("%B")))

if not os.path.exists(folder_to_create):
    os.makedirs(folder_to_create)

for filename in os.listdir(FOLDER_TO_TRACK):
    if not filename.startswith('.') or not not filename.startswith('$') or not filename.endswith('.ini'):
        print(filename)
        folder_destination = folder_to_create
        src = FOLDER_TO_TRACK + "/" + filename
        new_destination = folder_destination + "/" + filename
        os.rename(src, new_destination)

try:
    os.rmdir(folder_to_create)
except OSError:
    pass
