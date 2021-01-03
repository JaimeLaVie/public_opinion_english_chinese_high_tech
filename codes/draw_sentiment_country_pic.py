""" 本程序画时序图 """
import os
import jsonlines
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def drawpic(x, y, picname, xname, yname, Ylim, picsize, file_target):
    # y = []
    # for t in x:
    #     y.append(float(record[t]))
    lenx = range(len(x))
    # print ('h = ', h)
    # print ('y = ', y)
    # plt.figure(figsize = picsize)
    # plt.plot(lenx, y, linewidth = 1, color = 'blue')
    plt.bar(lenx, y, color='steelblue')
    plt.xticks(lenx, x, rotation = 0)
    plt.tick_params(axis='x', labelsize = 10)
    plt.tick_params(axis='y', labelsize = 12)
    # plt.ylim(Ylim)
    font_x = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 15}
    font_y = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 15}
    # font_title = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 40}
    plt.xlabel(xname, font_x)
    plt.ylabel(yname, font_y)
    # plt.title(picname, font_title)
    # for a, b in zip(lenh, y):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
    plt.savefig(file_target + "/{}.png".format(picname))
    plt.clf()

current_path = os.getcwd()
path = current_path + '/sentiment_jsonl'
file_target = current_path + '/pictures_countries_companies'
filenames = os.listdir(path)

countries = ['au', 'ca', 'in', 'nz', 'pk', 'uk', 'us']
countries_full = ['Australia', 'Canada', 'India', 'New Zealand', 'Pakistan', 'UK', 'US']
companies = ['b', 'h', 't']
companies_full = ['ByteDance', 'Huawei', 'Tencent']
sentiments = ['Positive', 'Neutral', 'Negative']
count_country = {}
count_company = {}
for country in countries:
    count_country[country] = {}
    for sentiment in sentiments:
        count_country[country][sentiment] = 0
for company in companies:
    count_company[company] = {}
    for sentiment in sentiments:
        count_company[company][sentiment] = 0

for filename in filenames:
    filepath = path + '/' + filename
    print (filename)
    with open (filepath, 'r') as f:
        for tweets in jsonlines.Reader(f):
            [country, company, no_use] = filename.split('_')
            if tweets['sentiment'] == 1:
                count_country[country]['Positive'] += 1
                count_company[company]['Positive'] += 1
            elif tweets['sentiment'] == -1:
                count_country[country]['Negative'] += 1
                count_company[company]['Negative'] += 1
            elif tweets['sentiment'] == 0:
                count_country[country]['Neutral'] += 1
                count_company[company]['Neutral'] += 1

for sentiment in sentiments:
    record = []
    for country in countries:
        record.append(count_country[country][sentiment])
    drawpic(countries_full, record, sentiment + '_tweets of countries', 'Country', 'Number of tweets', 0, (0, 0), file_target)

for sentiment in sentiments:
    record = []
    for company in companies:
        record.append(count_company[company][sentiment])
    drawpic(companies_full, record, sentiment + '_tweets of companies', 'Company', 'Number of tweets', 0, (0, 0), file_target)