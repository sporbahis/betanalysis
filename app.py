from flask import (Flask, render_template)

from apscheduler.schedulers.background import BackgroundScheduler
from Models.InterBahis import InterBahis


app = Flask(__name__)

def sensor():
    t = InterBahis("http://interbahis246.com")
    t.find_leage()

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',hours=1)
sched.start()


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
