#! usr/bin/python #coding=utf-8

import os, re

from cssselect import Selector

lst = []

b = '''' '''


# my = MyParser()  # 传入要分析的数据，是html的。
# my.feed(b)
# for url in lst:
#     b = b.replace(url, url+'.html')
# print b



# 生成 url
# url(r'^$',views.index)
def to_url():
    for item in os.listdir('templates/html'):
        if ('.html' in item): # 读取读取目录下的html文件
            print (
            '''url(r'^''' + item.replace('.html', '').replace('_', '/') + '''',views.''' + 'grunt_'+item.replace('-', '_').replace(
                '.html', '').replace('.', '_') + '),')

# 生成 views
def to_views():
    for item in os.listdir('templates/html'):
        if ('.html' in item): # 读取读取目录下的html文件
            print ('def ' + 'grunt_' + item.replace('-', '_').replace('.html', '').replace('.', '_') + '(request):'); # 去掉所有非法字符生成函数名
            print ('''    return render(request, 'html/''' + item + '''')'''); # 并返回对应的当前html文件


# 改css路径
def change_css():
    for item in os.listdir('templates/html'):
        if ('.html' in item):
            f = open('templates/html/' + item, "rb")
            b = f.read()

            b = b.replace(''' href="/css/main.82b81aba.css"''',
                          '''href="/static/css/main.82b81aba.css"''')
            # b = b.replace('''src="/img/''', '''src="../img/''')

            f = open('templates/html/' + item, "wb")
            f.write(b)
            f.close()
            print item


# 改img路径
def change_img():
    for item in os.listdir('templates/html'):
        if ('.html' in item):
            f = open('templates/html/' + item, "rb")
            b = f.read()

            b = b.replace('''src="/img/''',
                          '''src="/static/img/''')
            # b = b.replace('''src="/img/''', '''src="../img/''')

            f = open('templates/html/' + item, "wb")
            f.write(b)
            f.close()
            print item


# change_css()
# change_img()
to_url()
to_views()