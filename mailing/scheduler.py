# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# # from mailing import
#
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
#
#
# @register_job(scheduler, "interval", minutes=1)
# def your_scheduler_job_function():
#     # Ваш код для периодической задачи
#     pass
#
#
# register_events(scheduler)
# scheduler.start()
