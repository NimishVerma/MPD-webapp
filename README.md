Mpd-downloader-webapp
Webapp for the mpd downloader project made originally on Shell https://github.com/bigpythonimish/MPDdownloader-merger

Prerequisites
-------------
* Redis Installed and running  [Redis official docs](https://redis.io/topics/quickstart)
* Celery installed [Celery docs](http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#installing-celery)
* Django  2+ and Python 3

How to Install?
-----------------
1. Run the following commands to install the dependencies
```shell
pip install youtube_dl
```
2. Run the following commands in the exact order to migrate and start django app
```shell
python3 manage.py migrate
python3 manage.py runserver
```

3. Start the celery worker
```shell
celery -A mysite worker --loglevel=info
```
[Check this out if you face trouble in starting the worked](http://docs.celeryproject.org/en/latest/userguide/workers.html)

4. Open Localhost:8000, the UI is pretty simple and not-so-colourful, so this might be self-explanatory when I mention putting the url of whatever video you want to download from youtube/vimeo/mpd hostings etc.

5. Videos are downloaded through celery asynchronously, you can see them in Queue ( /queue) when they're downloaded.



