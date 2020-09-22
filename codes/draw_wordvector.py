# -*- coding: utf-8 -*-
import os
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import pandas as pd
pd.options.mode.chained_assignment = None
from sklearn.manifold import TSNE
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"simfang.ttf", size=14)
font_ko = FontProperties(fname=r"NanumGothic.ttf", size=14)
import matplotlib.patches as mpatches
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

basic_path = os.getcwd()
data_path = basic_path + '/' + 'pictures_countries_companies/for_draw_word_vector/'
save_path = basic_path + '/' + 'pictures_countries_companies/'
doc = "full_text"

country = 'in'   # 选择范围：'us', 'uk', 'ca', 'au', 'nz', 'in', 'pk'
words_frequency_b = "words_frequency_no_stopwords_{}_b.txt".format(country)
words_frequency_h = "words_frequency_no_stopwords_{}_h.txt".format(country)
words_frequency_t = "words_frequency_no_stopwords_{}_t.txt".format(country)

def getword(text):
    index = text.rfind("'")
    return text[1:index]

def pickwords(file_path, num):
    with open (file_path, "r") as f:
        str = f.read()
    wordlist = []
    str = str[2:]
    str = str.split("), (")
    i = 0
    for words in str:
        word = getword(words)
        # if word.lower() not in stopwords and word.find('\x00') is -1:
        wordlist.append(word)
        i += 1
        if i == num:
            break
        # with open (file_result, "a") as file:
        #     file.write(word + '\n')
    return wordlist

""" def getkeywords(keywordpath):
    word_list = []
    with open(keywordpath, 'r', encoding="utf-8") as f:
        for line in f:
            keyword = line.replace('\n', '')
            word_list.append(keyword)

    return word_list """

def makewordvector(docpath, min_count):
    text = open(data_path + docpath + '.txt', 'r',encoding='utf-8')
    model = Word2Vec(LineSentence(text), sg=0,size=200, window=5, min_count=min_count, workers=6)
    print(docpath + 'model训练完成')
    model.save(data_path + '{}.word2vec'.format(docpath))

makewordvector(doc, 1000)     # 注意第二个参数！中文语段较少，相应地最小计数词频也应小，不然没几个词会出现在图中

def testtheresult(modelpath):
    model = gensim.models.Word2Vec.load(modelpath)
    print(model.similarity('中国','韩国'))  #相似度为0.60256344
    print(model.similarity('繁荣富强','国泰民安'))  #相似度为0.49495476

    result1 = pd.Series(model.most_similar(u'中共')) #查找近义相关词
    print(result1)
    result2 = pd.Series(model.most_similar(u'国庆'))
    print(result2)
    print(model.wv['中国']) #查看中国的词向量（单个词语的词向量）
    with open('testtheresult.txt', 'w') as f:
        f.write("model.similarity('中国','韩国') = " + str(model.similarity('中国','韩国')) + '\n')
        f.write("model.similarity('繁荣富强','国泰民安') = " + str(model.similarity('繁荣富强','国泰民安')) + '\n')
        f.write("model.most_similar(u'中共') = " + str(result1) + '\n')
        f.write("model.most_similar(u'国庆') = " + str(result2) + '\n')
        f.write("model.wv['中国'] = " + str(model.wv['中国']))

# testtheresult('data_zh.word2vec')

model = gensim.models.Word2Vec.load(data_path + doc + '.word2vec')

def tsne_plot(model, chosen_words_1, chosen_words_2, chosen_words_3, country, picname):
    "Creates and TSNE model and plots it"
    print ("开始画图：" + picname)
    labels = []
    tokens = []
    
    for word in model.wv.vocab:
        # for word in chosen_words_zh:
        tokens.append(model[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)
    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    print ('len(x) = ', len(x))
    for i in range(len(x)):
        if labels[i] in chosen_words_1:
            dot1 = plt.scatter(x[i], y[i], s = 40, c = 'b', marker = 'o', edgecolors = 'none')
            plt.annotate(labels[i],
                        fontproperties=font,
                        xy=(x[i], y[i]),
                        xytext=(5, 2),
                        fontsize = 'xx-large',
                        textcoords='offset points',
                        color='b',
                        ha='right',
                        va='bottom')
    for i in range(len(x)):
        if labels[i] in chosen_words_2:
            dot2 = plt.scatter(x[i], y[i], s = 40 , c = 'g', marker = '^', edgecolors = 'none')
            plt.annotate(labels[i],
                        fontproperties=font,
                        xy=(x[i], y[i]),
                        xytext=(5, 2),
                        fontsize = 'xx-large',
                        textcoords='offset points',
                        color='g',
                        ha='right',
                        va='bottom')
    for i in range(len(x)):
        if labels[i] in chosen_words_3:
            dot3 = plt.scatter(x[i], y[i], s = 40 , c = 'r', marker = 's', edgecolors = 'none')
            plt.annotate(labels[i],
                        fontproperties=font,
                        xy=(x[i], y[i]),
                        xytext=(5, 2),
                        fontsize = 'xx-large',
                        textcoords='offset points',
                        color='r',
                        ha='right',
                        va='bottom')
    countries = {'us': 'U.S.', 'uk': 'U.K.', 'ca': 'Canada', 'au': 'Australia', 'nz': 'New Zealand', 'in': 'India', 'pk': 'Pakistan'}
    plt.legend([dot1, dot2, dot3], ['Frequently used words about {} and ByteDance'.format(countries[country]), 'Frequently used words about {} and Huawei'.format(countries[country]), 'Frequently used words about {} and Tencent'.format(countries[country])], fontsize = 'xx-large')
    # plt.title('Word Vectors')
    plt.savefig(save_path + '{}.jpg'.format(picname))
    plt.clf()

chosen_words_b = pickwords(data_path + words_frequency_b, 400)
print ("chosen_words_b")
chosen_words_h = pickwords(data_path + words_frequency_h, 400)
print ("chosen_words_h")
chosen_words_t = pickwords(data_path + words_frequency_t, 400)
print ("chosen_words_t")

tsne_plot(model, chosen_words_b, chosen_words_h, chosen_words_t, country, 'chosen_word_vector_{}'.format(country))
# tsne_plot(model, chosen_words_us_t, 'chosen_word_vector_us_t')