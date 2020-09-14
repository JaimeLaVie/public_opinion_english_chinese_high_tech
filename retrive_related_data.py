""" 本程序筛选提及制定国家和公司的英语推文 """
import os
import jsonlines
import json
# from langdetect import detect    # 检测正确率惨不忍睹
import langid
import re

# 大小写无所谓，后面的程序中会全部lower()
countries_all = ['the us', 'UnitedStates', 'United States', 'the states', 'America', ' uk ', 'UnitedKingdom', 'United Kingdom', 'Britain', 'Canada', 'Australia', 'aussie',
                'NewZealand', 'New Zealand', 'India', 'Pakistan']
companies_all = ['huawei', 'hua wei', 'bytedance', 'byte dance', 'zijietiaodong', 'zi jie tiao dong', 'tiktok', 'tik tok', 'douyin', 'dou yin', 'tencent', 'tengxun',
                'teng xun', 'wechat', 'weixin', 'wei xin']
dictionary = {'the us': 'us', 'UnitedStates': 'us', 'United States': 'us', 'the states': 'us', 'America': 'us',
            ' uk ': 'uk', 'UnitedKingdom': 'uk', 'United Kingdom': 'uk', 'Britain': 'uk', 
            'Canada': 'ca', 
            'Australia': 'au', 'aussie': 'au',
            'NewZealand': 'nz', 'New Zealand': 'nz',
            'India': 'in', 
            'Pakistan': 'pk',
            'huawei': 'h', 'hua wei': 'h',
            'bytedance': 'b', 'byte dance': 'b', 'zijietiaodong': 'b', 'zi jie tiao dong': 'b', 'tiktok': 'b', 'tik tok': 'b', 'douyin': 'b', 'dou yin': 'b', 
            'tencent': 't', 'tengxun': 't', 'teng xun': 't', 'wechat': 't', 'weixin': 't', 'wei xin': 't'}

# filedir = os.getcwd() + '/data'
# filenames = os.listdir(filedir)
# targetdir = os.getcwd() + '/preprocessed'
current_path = os.getcwd()


# paths = ['/intl_relations_20200304_0514', '/intl_relations_20200515_0604', '/intl_relations_20200605_0624', '/intl_relations_20200625_0714', '/intl_relations_20200715_0804']
paths = ['/intl_relations_20200715_0804']
targetdir = current_path + '/retrived_data'

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
                    try:
                        text = tweets['text'].lower()
                        try:
                            lang = str(langid.classify(text)[0])
                            if lang == 'en':
                                # print (text)
                                country_codes = []
                                country_names = ''
                                company_codes = []
                                company_names = ''
                                for countries in countries_all:
                                    if re.findall(countries.lower(), text) != []:
                                        country_codes.append(dictionary[countries])
                                for companies in companies_all:
                                    if re.findall(companies.lower(), text) != []:
                                        company_codes.append(dictionary[companies])
                                if country_codes == [] or company_codes == []:
                                    continue
                                # print ('Find one!')
                                country_codes = list(set(country_codes))   #去除重复项
                                country_codes.sort()
                                company_codes = list(set(company_codes))   #去除重复项
                                company_codes.sort()
                                underline = '-'
                                country_names = underline.join(country_codes)
                                company_names = underline.join(company_codes)
                                with open ('{}/{}.jsonl'.format(targetdir, country_names + '_' + company_names), "a") as file:
                                    file.write(json.dumps(tweets)+'\n')
                                # print ('2')
                        except:
                            pass
                            # with open ('{}/not_a_language_{}.jsonl'.format(targetdir, country_names), "a") as file:
                            #     file.write(json.dumps(tweets)+'\n')
                            # print ('3')
                    except:
                        print (filename)
                        try:
                            print (tweets['id'])
                        except:
                            try:
                                print (tweets['limit'])
                            except:
                                print (tweets)
            except:
                print ("文件内没有内容！文件名：" + filename)
                continue