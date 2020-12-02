heroku run python3 manage.py migrate account zero
heroku run python3 manage.py migrate admin zero
heroku run python3 manage.py migrate auth zero
heroku run python3 manage.py migrate authtoken zero
heroku run python3 manage.py migrate AppSolvePoscomp zero --fake
#heroku run rm db.sqlite3
