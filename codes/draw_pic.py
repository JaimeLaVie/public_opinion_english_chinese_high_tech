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
    plt.plot(lenx, y, linewidth = 1, color = 'blue')
    plt.xticks(lenx, x, rotation = 45)
    plt.tick_params(axis='x', labelsize = 8)
    plt.tick_params(axis='y', labelsize = 10)
    # plt.ylim(Ylim)
    font_x = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 10}
    font_y = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 10}
    # font_title = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 40}
    plt.xlabel(xname, font_x)
    plt.ylabel(yname, font_y)
    # plt.title(picname, font_title)
    # for a, b in zip(lenh, y):
    #     plt.text(a, b, b, ha='center', va='bottom', fontsize=20)
    plt.savefig(file_target + "/{}.png".format(picname))
    plt.clf()

current_path = os.getcwd()
path = current_path + '/data_count.jsonl'
file_target = current_path + '/pictures_countries_companies'
months = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
dates = []
x_axis_number = 20
for month in months:
    if month == 'Mar':
        for day in range(4, 32):
            if day < 10:
                date = month + ' 0' + str(day)
            else:
                date = month + ' ' + str(day)
            dates.append(date)
    elif month == 'May' or month == 'Jul' or month == 'Aug':
        for day in range(1, 32):
            if day < 10:
                date = month + ' 0' + str(day)
            else:
                date = month + ' ' + str(day)
            dates.append(date)
    elif month == 'Apr' or month == 'Jun':
        for day in range(1, 31):
            if day < 10:
                date = month + ' 0' + str(day)
            else:
                date = month + ' ' + str(day)
            dates.append(date)
    elif month == 'Sep':
        for day in range(1, 15):
            if day < 10:
                date = month + ' 0' + str(day)
            else:
                date = month + ' ' + str(day)
            dates.append(date)
point = math.floor(len(dates) / x_axis_number)
x_axis = dates.copy()
for day in range(len(dates)):
    if day % point != 0:
        x_axis[day] = ''
# print (dates)

relevant_countries = ['us', 'uk', 'ca', 'au', 'nz', 'in', 'pk']
relevant_companies = ['h', 't', 'b']
pairs = []
for state in relevant_countries:
    for business in relevant_companies:
        pair = state + '_' + business
        pairs.append(pair)

with open ('data_count.jsonl', 'r') as f:
    for line in jsonlines.Reader(f):
        data = line
# print (data)

for pair in pairs:
    record = []
    for date in dates:
        record.append(data[date][pair])
    drawpic(x_axis, record, pair, 'date', 'number of tweets', 0, (0, 0), file_target)