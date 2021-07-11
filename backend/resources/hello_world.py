import falcon
import json

"""
Hello World resource
"""


class HelloWorld(object):

    def __init__(self):
        self._message = "Hello World !!"

    async def on_get(self, req, resp):
        """GET Request"""
        payload = {'message': self._message}

        resp.text = json.dumps(payload)
        resp.status = falcon.HTTP_200
