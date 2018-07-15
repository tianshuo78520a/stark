from flask import Blueprint, render_template, request
from chun import db
from chun import models
import requests
from bs4 import BeautifulSoup

us = Blueprint('us', __name__)


@us.route('/index',methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        url = request.form.get('html')
        response = requests.get(url)
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find(name='div', attrs={'id': 'auto-channel-lazyload-article'})
        li_list = div.find_all(name='li')

        for li in li_list:
            # 标题：title.text
            title = li.find(name='h3')
            if not title:
                continue

            # 简介：p.text
            p = li.find(name='p')

            # 图片路径：img
            img = li.find(name='img').get('src')
            img = 'http:' + img

            # 图片名 file_name
            file_name = img.rsplit('/', maxsplit=1)[1]

            # 图片保存到本地 file_path
            ret = requests.get(img)
            with open('chun/static/picture/%s' % file_name, 'wb')as f:
                f.write(ret.content)
            file_path = 'static/picture/%s' % file_name

            # 文章路径 href
            href = li.find(name='a').get('href')
            href = 'http:' + href

            # 文章来源 of.text
            ar_html = requests.get(href)
            ar_html.encoding = 'gbk'
            article_soup = BeautifulSoup(ar_html.text, 'html.parser')
            div = article_soup.find(name='span', attrs={'class': 'source'})
            if not div:
                continue
            of = div.find(name='a')

            # 存入数据库
            db.session.add(models.New(title=title.text,
                                      info=p.text,
                                      picture=file_path,
                                      href=href,
                                      of=of.text))
            db.session.commit()
            db.session.remove()

        return '提交成功'





