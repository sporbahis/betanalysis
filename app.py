from flask import (Flask, render_template)

from apscheduler.schedulers.background import BackgroundScheduler

from Models.DB.Matches import MatchInfo
from Models.InterBahis import InterBahis
from Models.DB.Leages import LeageInfo


app = Flask(__name__)

def sensor():
    t = InterBahis("http://interbahis247.com")
    t.find_leage()

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',hours=1)
sched.start()


@app.route('/test')
def test():
    return render_template('test.html', leages = LeageInfo.objects.all(), matches = MatchInfo.objects.limit(10).all())

@app.route('/')
def index():
    return render_template('index.html', leages = LeageInfo.objects.all(), matches = MatchInfo.objects.all())


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
