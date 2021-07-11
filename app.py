import traceback
import falcon.asgi

from config import Config
from resources.hello_world import HelloWorld
from utils.response_logger import ResponseLoggerMiddleware
from resources.images import Images, Thumbnails
from models.store import Store

"""
Main script to initialize falcon app
"""


def create_app(config=None):
    config = config or Config()
    store = Store(config)

    # Initialize the Resource object
    hello_world = HelloWorld()
    images = Images(config, store)
    thumbnails = Thumbnails(store)

    # Initialize the Falcon App
    try:
        app = falcon.asgi.App(middleware=[ResponseLoggerMiddleware()])
    except:
        print(traceback.format_exc())
    # Add the resource to an API Endpoint
    app.add_route('/hello', hello_world)
    app.add_route('/images', images)
    app.add_route('/images/{image_id:uuid}.jpeg', images, suffix="image")
    # app.add_route('/thumbnails/{image_id:uuid}.jpeg', thumbnails)
    app.add_route('/thumbnails/{image_id:uuid}/{width:int}x{height:int}.jpeg', thumbnails)

    return app

