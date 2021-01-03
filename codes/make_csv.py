import os
import csv
import jsonlines

current_path = os.getcwd()
file_name = 'in_b'

# 1. 创建文件对象
f = open(current_path + '/' + file_name + '.csv','w', newline='', encoding='utf-8')

# 2. 基于文件对象构建 csv写入对象
csv_writer = csv.writer(f)

# 3. 构建列表头
csv_writer.writerow(["TweetText"])

# 4. 写入csv文件内容
with open (current_path + '/retrived_data_merged/' + file_name + '.jsonl', 'r') as json_f:
    for tweets in jsonlines.Reader(json_f):
        csv_writer.writerow([tweets['text']])

# 5. 关闭文件
f.close()