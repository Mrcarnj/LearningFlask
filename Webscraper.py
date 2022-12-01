from flask import Flask, render_template
app = Flask(__name__)
from bs4 import BeautifulSoup
import requests
import time
import os


while True:
    url = 'https://www.espn.com/golf/leaderboard'
    req = requests.get(url)
    bsObj=BeautifulSoup(req.text,'lxml')

    data = bsObj.find_all('div', class_ = 'Table__Scroller')

    table_data=[]
    tablerows=bsObj.select('table tr')

    for tr in tablerows[1:]:
        row=[]
        for t in tr.select('td')[1:4]:
            row.extend([t.text.strip()])
        table_data.append(row)
    data = table_data



    @app.route('/')
    def home():
        return render_template('home.html', data=data)

    if __name__ == '__main__':
        app.run(debug=True)
    time.sleep(1 * 60)
