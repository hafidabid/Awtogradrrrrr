from os import *
from shutil import *
from settings import FOLDER_SUBMISI_PRAKTIKUM


'''
default_flname = "submission"
c = 1
while(path.isdir(default_flname)):
    if c==1 :default_flname=default_flname[0:len(default_flname):]+str(c)
    else : default_flname=default_flname[0:len(default_flname)-len(str(c)):]+str(c)
    c=c+1
makedirs(default_flname,mode=0o777)
'''
global list_all_files
list_all_files = []
for djF in FOLDER_SUBMISI_PRAKTIKUM:
    n = walk(djF)
    directory_list = []
    flag = False
    count = 1
    for root, dir, files in n:
        if (not flag):
            flag = True
        else:
            directory_list.append(root)

    for x in range(len(directory_list)):
        repetitif_flag = False
        y = x + 1
        while (not repetitif_flag and y < len(directory_list)):
            if (directory_list[x] in directory_list[y]): repetitif_flag = True
            y = y + 1
            if (y - x > 3): y = len(directory_list)
        if repetitif_flag: directory_list[x] = "rept"

    count = 0
    while (count < len(directory_list)):
        if (directory_list[count] == "rept"): directory_list.remove("rept")
        count = count + 1

    for xay in directory_list:
        onFolder = listdir(xay)
        for filee in onFolder:
            try:
                # copyfile(default_flname, xay + "\\" + filee)
                #if(".py" in filee): copy(xay + "\\" + filee, default_flname)
                if(".py" in filee): list_all_files.append(xay + "\\" + filee)
                # print(xay)
                # print(xay + "\\" + filee)
            except Exception as e:
                print(e)