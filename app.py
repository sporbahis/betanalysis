from flask import (Flask, render_template)
from apscheduler.schedulers.background import BackgroundScheduler
from Models.DB.Matches import MatchInfo
from Models.InterBahis import InterBahis
from Models.DB.Leages import LeageInfo
from Models.DB.JobSchedular import JobSchedular
import re
import datetime

app = Flask(__name__)

def background_InterBahis():
    try:
        JobSchedular.objects.raw({"State": "Continue"}).all().first()
        return 1
    except JobSchedular.DoesNotExist:
        job = JobSchedular()
        job.StartDate = datetime.datetime.utcnow()
        job.JobName = "İnterBahis"
        job.State = "Continue"
        job.save()
        t = InterBahis("http://interbahis247.com")
        t.find_leage()
        job.FinishDate = datetime.datetime.utcnow()
        job.State = "Finished"
        job.save()


sched = BackgroundScheduler(daemon=True)
sched.add_job(background_InterBahis,'interval',minutes=10,id="00001",name="İnterBahis",coalesce=True,max_instances=1)
#sched.start()




@app.route('/datacheck')
def datacheck():
    t = InterBahis("http://interbahis247.com")
    t.find_leage()
    return render_template('data_check.html')


@app.route('/test')
def test():
    return render_template('index.html', leages = LeageInfo.objects.all(), matches = MatchInfo.objects.limit(5).all())


@app.route('/')
def index():
    return render_template('test.html', leages = LeageInfo.objects.all(), matches = MatchInfo.objects.limit(5).all())






@app.template_filter()
def group_by_type(list):
    temp_dict = dict()
    for x in list:
        temp_name = re.sub('[^a-zA-Z0-9]+', '', x.Type).lower()
        temp_dict.setdefault(temp_name, []).append(x)
    return temp_dict

app.jinja_env.filters['group_by_type'] = group_by_type


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
