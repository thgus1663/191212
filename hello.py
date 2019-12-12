from flask import Flask, escape, request, render_template
import random
import numpy as np
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/') #앞에있는 서버주소 생략됨
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi'

@app.route('/thgus')
def thgus():
    return 'hello thgus'


@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

@app.route('/html_file')
def html_file():
    return render_template('index.html')

@app.route('/variable')
def variable():
    name="정소현"
    return render_template('variable.html', html_name=name)

@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name=name
    return render_template('greeting.html', html_name=def_name)

@app.route('/cube/<int:num>/')
def cube(num):
    def_num=num
    def_num1=num**3
    return render_template('cube.html', html_num=def_num, html_num1=def_num1)

@app.route('/lunch')
def lunch():
    menu = ['치킨', '피자', '떡볶이', '족발', '자장면']
    menuimg = ['https://img1.daumcdn.net/thumb/R720x0/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fliveboard%2FSNUH%2Fea3136eda7e44fd4a423e78efff8e3ec.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzN55hPJsFizfKo4qdCpENMp1zTbF62pYryGKQKXBvtE1q1JNQ&s', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ4xEnDJmJqOiyGXj-Uu2cVivUvZsCfjI49X2fwcVxz2tnUtuJgA&s', 'http://img.daily.co.kr/@files/www.daily.co.kr/content/food/2017/20170310/8383e1ff029938ebc4aa15d15badda0d.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH4x-1Hx3R91TtYHxZqBSTY0qVV2pwyC_oooFuLkP9qdI1xHiI&s']
    #dicionary 형식으로     
    random_idx = np.random.randint(0, len(menu))
    return render_template('lunch.html', html_name=menu[random_idx], html_image=menuimg[random_idx])

# dic으로
# @app.route('/lunch')
# def lunch():
#     menus = {
#         '치킨': 'https://img1.daumcdn.net/thumb/R720x0/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fliveboard%2FSNUH%2Fea3136eda7e44fd4a423e78efff8e3ec.jpg', 
#         '피자': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzN55hPJsFizfKo4qdCpENMp1zTbF62pYryGKQKXBvtE1q1JNQ&s', 
#         '떡볶이': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ4xEnDJmJqOiyGXj-Uu2cVivUvZsCfjI49X2fwcVxz2tnUtuJgA&s', 
#         '족발': 'http://img.daily.co.kr/@files/www.daily.co.kr/content/food/2017/20170310/8383e1ff029938ebc4aa15d15badda0d.jpg', 
#         '자장면': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH4x-1Hx3R91TtYHxZqBSTY0qVV2pwyC_oooFuLkP9qdI1xHiI&s'
#         }
#     menu_list = list(menus.keys())
#     pick=random.choice(menu_list)
#     img=menus[pick]
#     return render_template('lunch.html', html_name=pick, html_image=img)
    

@app.route('/movies')
def movies():
    movies = ['겨울왕국2', '쥬만지', '포드v페라리']
    return render_template('movies.html', movies=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong', methods=['GET', 'POST'])
def pong():
    #print(request.form.get('keyword'))
    keyword = request.form.get('keyword') #post방식 post방식은 url이 안바뀜
    #keyword = request.args.get('keyword') #get방식 get방식은 url이 바뀜
    return render_template('pong.html', keyword=keyword)


@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/summoner')
def summoner():
    return render_template('summoner.html')

@app.route('/opgg')
def opgg():
    username = request.args.get('username', '잘못된 키 접근임') #디폴트값도 지정
    opgg_url = f'https://www.op.gg/summoner/userName={username}'
    res = requests.get(opgg_url).text
    soup = BeautifulSoup(res, 'html.parser')

    tier = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    return render_template('opgg.html', username=username, opgg_url=opgg_url, tier=tier.text, wins=wins.text)

if __name__ == '__main__' :
    app.run(debug=True)