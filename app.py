from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 鸡汤语录库，你以后可以自己随便加
chicken_soup = [
    "生活原本沉闷，但跑起来就有风。",
    "别贪心，你不可能什么都有；别灰心，你不可能什么都没有。",
    "前路漫漫亦灿灿，往事堪堪亦澜澜。",
    "坚持的意义，是让自己有选择的权利。",
    "所有的好运，都藏在温柔和坚持里。",
    "不必追光，你我皆是星辰。"
]

# 主页路由
@app.route('/', methods=["GET", "POST"])
def index():
    soup = ""
    if request.method == "POST":
        # 不管用户输入啥，都随机给一句鸡汤
        soup = random.choice(chicken_soup)
    return render_template("index.html", soup=soup)

# 注意！这里删掉了 debug=True，而且不用写 app.run()
# Render 会用 Procfile 里的 gunicorn 启动，所以本地的 app.run() 可以删掉