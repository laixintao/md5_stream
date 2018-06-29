# Run

```
uwsgi --http :9090 --wsgi-file app.py --callable app
```

docker run

```
docker run -p 9090:9090 --memory=100m a814f0d52810 uwsgi --http :9090 --wsgi-file app.py --callable app
```

flask

```
FLASK_APP=app.py flask run
```
