web: gunicorn -b 0.0.0.0:5000 app:baseApp --log-file -
worker:        env QUEUE=* bundle exec rake resque:work
urgentworker:  env QUEUE=urgent bundle exec rake resque:work