from crontab import CronTab

def job():
    cron = CronTab(user=True)
    job = cron.new(command='run_task.py')
    job.minute.every(5)

    cron.write()
    
job()

#To clear cron of all jobs
#cron.remove_all()
    

'''

To start a cron job for every 5 minutes:
 
Go to terminal:
    Go to file directory
    pwd : /Users/ishi/newj_project/cron-job/url_cron.py
    which python : /Users/ishi/.pyenv/shims/python
    
crontab -e
press I for insert
*/5 * * * * /Users/ishi/.pyenv/shims/python /Users/ishi/newj_project/cron-job/url_cron.py
esc
:wq
return
crontab -l 

'''
