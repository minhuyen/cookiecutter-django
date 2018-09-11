import os
import random
import string
import uuid

from django.utils.deconstruct import deconstructible
from rest_framework.views import exception_handler


@deconstructible
class RandomFileName(object):

    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response
