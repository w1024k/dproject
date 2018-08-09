# coding: utf-8
from qiniu import Auth, put_data, etag, urlsafe_base64_encode, put_file
from common import settings


class Bucket(object):
    def __int__(self):
        self.q = Auth(settings.QINIU_ACCESSKEY, settings.QINIU_SECRETKEY)
        self.token = self.q.upload_token(settings.BUCKET_NAME)

    def put_obj(self, key, localfile):
        ret, info = put_file(self.token, key, localfile)

    def delete_obj(self):
        pass
