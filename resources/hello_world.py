import traceback
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
        try:
            payload = {'message': self._message}
        except:
            print(traceback.format_exc())
            raise Exception

        resp.text = json.dumps(payload)
        resp.status = falcon.HTTP_200
