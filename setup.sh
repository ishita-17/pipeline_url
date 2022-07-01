pip install celery
pip install pymongo
pip install requests
pip install json
brew install rabbitmq-server
brew install supervisor

PATH=$PATH:/usr/local/sbin
rabbitmq-server

export PYTHONPATH=.
python pipeline_url/msg_script/run_task.py

cd ..

supervisord -c pipeline_url/conf/supervisord.conf
supervisorctl -c pipeline_url/conf/supervisord.conf

brew services restart supervisor
tail -f url_collection_worker
kill -9 <workerNumber>
