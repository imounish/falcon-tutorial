import logging
from config import Config


class ResponseLoggerMiddleware(object):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    fh = logging.FileHandler(Config().www_log)
    fh.setLevel(level=logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    async def process_response(self, req, resp, resource, req_succeeded):
        # self.logger.info('{0} ({1}, {2}) {3}'.format(req.url, resp.status[:3], req_succeeded, resource))
        self.logger.info("'{}' | {}".format(req.url, resp.status[:3]))
