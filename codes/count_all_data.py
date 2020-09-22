""" 本程序计数，全部 """
# 输出结果格式：{'Jul 05':{'us_h': 35, 'uk_t': 56}}
import os
import jsonlines
import json

current_path = os.getcwd()
path = current_path + '/retrived_data_merged'
target = current_path + '/data_count.jsonl'
filenames = os.listdir(path)

# count = {}
# relevant_countries = ['us', 'uk', 'ca', 'au', 'nz', 'in', 'pk']
# relevant_companies = ['h', 't', 'b']
# # pairs = {}
# # for state in relevant_countries:
# #     for business in relevant_companies:
# #         pair = state + '_' + business
# #         pairs[pair] = 0
# # print (pairs)
# registered_dates = []

n = 0
for filename in filenames:
    print (filename)
    # countries_companies = filename.split('.')[0]
    # # print (countries_companies)
    # [countries, companies] = countries_companies.split('_')
    # countries = countries.split('-')
    # companies = companies.split('-')
    # # print (countries, companies)
    filepath = path + '/' + filename
    # print (filepath)
    with open (filepath, 'r') as f:
        try:
            for tweets in jsonlines.Reader(f):
                n = n + 1
        except:
            print ("文件内没有内容！文件名：" + filename)
            continue

print (n)

# with open (target, "a") as file:
#     file.write(json.dumps(count)+'\n')