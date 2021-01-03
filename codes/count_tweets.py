""" 本程序点数 """
import os
import jsonlines

current_path = os.getcwd()
dir = current_path + '/in_b_sentiment.jsonl'

number = 0

with open (dir, 'r') as f:
    for tweets in jsonlines.Reader(f):
        number += 1

print (number)