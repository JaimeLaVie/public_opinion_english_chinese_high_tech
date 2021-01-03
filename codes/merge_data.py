""" 本程序合并同名文件 """
import os
import jsonlines
import json
import langid
import re

current_path = os.getcwd()
paths = ['/retrived_data_20200304_0514', '/retrived_data_20200515_0604', '/retrived_data_20200605_0624', '/retrived_data_20200625_0804', '/retrived_data_20200805_0914'] 
targetdir = current_path + '/retrived_data_merged'

for path in paths:
    print (path)
    filedir = current_path + path
    filenames = os.listdir(filedir)

    for filename in filenames:
        print (filename)
        filepath = filedir + '/' + filename
        # print (filepath)
        with open (filepath, 'r') as f:
            try:
                for tweets in jsonlines.Reader(f):
                    with open ('{}/{}'.format(targetdir, filename), "a") as file:
                        file.write(json.dumps(tweets)+'\n')
            except:
                print ("文件内没有内容！文件名：" + filename)
                continue