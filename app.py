from flask import (Flask, render_template, request)
from apscheduler.schedulers.background import BackgroundScheduler
from Models.DB.Matches import MatchInfo
from Models.InterBahis import InterBahis
from Models.DB.Leages import LeageInfo
from Models.DB.JobSchedular import JobSchedular
import math
import re
import datetime
from bson.objectid import ObjectId

app = Flask(__name__)


def background_inter_bahis():
    jobName = "İnterBahis"
    try:
        JobSchedular.objects.raw({"State": "Continue","JobName":jobName}).all().first()
        return False
    except JobSchedular.DoesNotExist:
        job = JobSchedular()
        job.StartDate = datetime.datetime.utcnow()
        job.JobName = jobName
        job.State = "Continue"
        job.save()
        t = InterBahis("http://interbahis249.com")
        t.find_leage()
        job.FinishDate = datetime.datetime.utcnow()
        job.State = "Finished"
        job.save()


def background_remove_matches():
    jobName = "İnterBahisRemove"
    try:
        JobSchedular.objects.raw({"State": "Continue","JobName":jobName}).all().first()
        return False
    except JobSchedular.DoesNotExist:
        job = JobSchedular()
        job.StartDate = datetime.datetime.utcnow()
        job.JobName = jobName
        job.State = "Continue"
        job.save()
        interbahis = InterBahis()
        interbahis.clear_match_data(datetime.datetime.utcnow())
        job.FinishDate = datetime.datetime.utcnow()
        job.State = "Finished"
        job.save()


job_schedular = BackgroundScheduler(daemon=True)

job_schedular.add_job(background_inter_bahis, 'interval', minutes=5, coalesce=True, max_instances=1)
job_schedular.add_job(background_remove_matches, 'interval', hours=12, coalesce=True, max_instances=1)
job_schedular.start()


"""
_________________ JOBS METHODS ____________________________-

"""

@app.route("/job_info")
def job_info():
    try:
        job_list = JobSchedular.objects.values().all()
    except JobSchedular.DoesNotExist:
        job_list = []
    return render_template('job_info.html', job_list=job_list)


@app.route("/job_clear")
def job_clear():
    try:
         list = JobSchedular.objects.all()
         now = datetime.datetime.utcnow()
         for job in list:
             if math.floor(((now - job.StartDate).seconds) / 3600) > 1:
                 job.State = "Continue"
                 job.save()
         is_deleted = True
    except JobSchedular.DoesNotExist:
        is_deleted = False
    return render_template('clear_all_data.html', is_deleted = is_deleted)


"""
_________________ JOBS METHODS ____________________________-

"""

"""
_________________ ALL LİST METHODS ____________________________-

"""

@app.route('/test')
def test():
    return render_template('index.html', leages = LeageInfo.objects.all(), matches = MatchInfo.objects.limit(5).all())

@app.route('/test_all')
def test_all():
    return render_template('index.html', leages = LeageInfo.objects.all(), matches = MatchInfo.objects.all())


"""
_________________ ALL LİST METHODS ____________________________-

"""

@app.route('/match_info',methods=["Post"])
def match_info():
    req_data = request.get_json()
    match_id = req_data['match_id']
    match = None
    try:
        match = MatchInfo.objects.raw({'_id': ObjectId(match_id)}).all().first()
    except MatchInfo.DoesNotExist:
        pass
    return render_template('match_info.html',match = match)

@app.route('/')
def all():
    try:
        page = request.args.get('page')
        if page == None:
            page = 0
    except:
        page = 0

    return render_template('test.html',page = page, leages = LeageInfo.objects.all(), matches = MatchInfo.objects.limit(5).skip(5).all())


@app.route('/job_pause')
def job_pause():
    job_schedular.pause()
    return render_template('test.html')


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
