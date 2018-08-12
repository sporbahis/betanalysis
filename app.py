from flask import (Flask, render_template)

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from Models.DB.TestModel import TestModel


app = Flask(__name__)

def sensor():
    test = TestModel()
    test.Date = datetime.now()
    test.save()

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=1)
sched.start()


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
