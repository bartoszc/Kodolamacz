import os
import datetime

folder_name = input('Enter path to the folder: ')
day = datetime.datetime(2018, 2, 22)

for file in os.listdir(folder_name):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(os.path.join(folder_name, file))
    if datetime.date.fromtimestamp(mtime) < day and size > 1000000:
        os.remove(os.path.join(folder_name, file))



