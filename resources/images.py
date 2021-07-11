import traceback
import uuid

import aiofiles
import falcon


class Images:
    def __init__(self, config, store):
        self._config = config
        self._store = store

    async def on_get(self, req, resp):
        resp.media = [image.serialize() for image in self._store.list_images()]

    async def on_get_image(self, req, resp, image_id):
        # image_id: UUID is converted back to a string identifier
        image = self._store.get(str(image_id))
        resp.stream = await aiofiles.open(image.path, 'rb')
        resp.content_type = falcon.MEDIA_JPEG

    async def on_post(self, req, resp):
        try:
            data = await req.stream.read()
            print("Image Directory: " + str(self._config.storage_path))
            image_id = str(self._config.uuid_generator())
            print("Image ID: " + image_id)
            image = await self._store.save(image_id, data)
        except:
            print(traceback.format_exc())
            raise Exception("Error in images - POST ")

        resp.location = image.uri
        resp.media = image.serialize()
        resp.status = falcon.HTTP_201


class Thumbnails:
    def __init__(self, store):
        self._store = store

    async def on_get(self, req, resp, image_id: uuid, width: int, height: int):
        try:
            image = self._store.get(str(image_id))
        except falcon.HTTPNotFound:
            print(traceback.format_exc())
            resp.status = falcon.HTTP_500
        except:
            print(traceback.format_exc())
            raise Exception


        if not image:
            raise falcon.HTTPNotFound
        if req.path not in image.thumbnails():
            raise falcon.HTTPNotFound
        resp.content_type = falcon.MEDIA_JPEG
        resp.data = await self._store.make_thumbnail(image, (width, height))


