from crontab import CronTab


def job():
    cron = CronTab(user=True)

    job = cron.new(command="msg_script/run_task.py")  # creating cron job to be executed

    job.minute.every(5)

    cron.write()


job()
