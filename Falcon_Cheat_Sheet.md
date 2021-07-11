# Falcon Cheat sheet

### Initializing the app:
```python
import falcon
api = application = falcon.App()
```

### Initializing the API end point
```python
api.add_route('/hello', hello_world)
```
`hello_world` is an object of the resource class containing on_get() (on_*(), replace * with HTTP Verb).  

### Running the app
```shell
$ gunicorn app
```
Using configurations while running the app
```shell
$ gunicorn -w 1 -b 0.0.0.0:5000 app:api --reload
```

### Inspecting the app
```shell
$ falcon-inspect-app app:api
```

### Making a request
```shell
$ curl http://0.0.0.0:5000/hello
{"message": "Hello World"}%
```