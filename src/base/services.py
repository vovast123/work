import os

from django.core.validators import ValidationError


def get_path_upload_product_image(instance, file):
    """ Путь к обложке товара, format: (media)/products/product_id/photo.jpg """

    return f"products/product_{instance.id}/{file}"


def validate_size_image(file_object):
    """ Проверка размера загружаемого файла """

    megabyte_limit = 2
    if file_object.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла не должен превышать {megabyte_limit}MB")


def get_path_upload_profile_image(instance, file):
    """ Путь к профилю юзера"""

    return f"profile_{instance.id}/{file}"

