from os.path import join
# from time import time_ns
from uuid import uuid4

from django.views.decorators.http import require_http_methods

from Trello.settings import MEDIA_ROOT
from authentication.models import Uploads


def media_path(file_name):
    return f'/media/uploads/{file_name}'


def process_name(code: str, extension: str):
    return f"{code}.{extension}"


def get_extension(file_name: str):
    return file_name.split(".")[-1]


def unique_code():
    return "%s" % (str(uuid4()).replace("-", ""))


def store_file(file):
    code = unique_code()
    new_name = process_name(code, get_extension(file.name))
    for chunk in file.chunks():
        with open(join(MEDIA_ROOT, 'uploads', new_name), mode="wb+") as write_file:
            write_file.write(chunk)

    uploads = Uploads(
        original_name=file.name,
        content_type=file.content_type,
        size=file.size,
        code=code,
        new_name=new_name,
        path=media_path(new_name)
    )
    uploads.save()

    return uploads.id
