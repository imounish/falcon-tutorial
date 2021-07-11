import falcon.asgi

from resources.hello_world import HelloWorld
from config import Config
from resources.images import Images
from models.store import Store
"""
Main script to initialize falcon app
"""


def create_app(config=None):
    config = config or Config()

    # Initialize the Resource object
    hello_world = HelloWorld()
    store = Store(config)
    images = Images(config, store)

    # Initialize the Falcon App
    app = falcon.asgi.App()
    # Add the resource to an API Endpoint
    app.add_route('/hello', hello_world)
    app.add_route('/images', images)
    app.add_route('/images/{image_id:uuid}.jpeg', images, suffix="image")

    return app

