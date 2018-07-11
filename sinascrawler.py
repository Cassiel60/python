#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup 
import json
import pandas


#取得评论数与评论内容
# jd =json.loads(comments.text.strip('var data='))
# jd['result']['count']['total']

# class 时，加. ;id 时，加#
# soup.select('.article-editor')[0].text.lstrip('责任编辑')
# soup.select('#commentcount1')

# 将抓取评论数方法整理成一函式
commentURL = 'http://comment5.news.sina.com.cn/page/info?version=1&format=is&channel=an&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page size=20'

def getCommentCount(newsurl):
	m=re.search('doc-i(.*).shtml',newsurl)
	newsid = m.group(1)
	comments = requests.get(commentURL.format(newsid))
	jd = json.loads(comments.text.strip('var data='))
	return jd['result']['count']['total']

# 将抓取内文信息方法整理成一函数

def getNewsDetail(newsurl):
	result = {}
	res = requests.get(newsurl)
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,'html.parser')  # or 'lxml'
	result['title'] = soup.select('#artibodyTitle')[0].text
	result['newssource'] = soup.select('.time-source span a')[0].text
	timesource = soup.select('.time-source')[0].contents[0].strip()
	result['dt'] = datetime.striptime(timesource,'%Y年%m月%d日%H:%M')
	result['article'] = ''.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
	result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑 ：')
	result['comments'] = getCommentCount(newsurl)
	return result

#找到分页连结
# 1.选择Network页签
# 2.点选JS
# 3.点找到连结 (包含page = ?)

# 剖析分页信息
res = requests.get('http"//.....page=1&....') # 简写，可能每个网址的分页不同
jd = json.loads(res.text.lstrip('...').rstrip('....')) # 移除左右多余字符串
for ent in jd['result']['data']:
	print ent['url']   # 印出每页连结

# 建立剖析清单链接函式
def parseListLinks(url):
	newsdetails = []
	res = requests.get(url)
	jd = json.loads(res.text.lstrip('newsloadercallback(').rstrip(');'))
	for ent in jd['result']['data']:
		newsdetails.append(getNewsDetail(ent['url']))
	return newsdetails

# 批次抓取每页新闻内文
url = 'http://......page={}'
news_total = []
for i in range(1,3):
	newsurl = url.format(i)
	newsary = parseListLinks(newsurl)
	news_total.extend(newsary)

# 将资料保存至excel
df.to_excel('news.xlsx')
# 将资料保存至资料库
import sqlite3
with sqlite3.connect('news.sqlite') as db:
	df.to_sql('news',con=db)

# 从资料库读取
import sqlite3
with sqlite3.connect('news.sqlite') as db:
	df2 = pandas.read_sql_query('SELECT * FROM news',con=db)