from flask import render_template
from flask import Flask, escape, url_for

app = Flask(__name__,
            static_url_path='',  
            )

class Data_article:
    def __init__(self, head, article):
        self.head = head
        self.article = article


data=[]
@app.route('/')
def nCoV_index():
    while(data==[]):
        data.append(Data_article('資料爬取中...很抱歉造成您的困擾','請稍候重新整理再來'))
        
    return render_template('mohw-news.html', posts=data)
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


