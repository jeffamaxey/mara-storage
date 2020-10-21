"""Information functions for storage file/directory information"""

from functools import singledispatch
import os

from mara_storage import storages, config


@singledispatch
def file_exists(storage: object, file_name: str) -> str:
    """
    Check if a file exists on a storage
    """
    raise NotImplementedError(f'Please implement file_exists for type "{storage.__class__.__name__}"')


@file_exists.register(str)
def __(alias: str, file_name: str):
    return file_exists(storages.storage(alias), file_name=file_name)


@file_exists.register(storages.LocalStorage)
def __(storage: storages.LocalStorage, file_name: str):
    return (storage.base_path.absolute() / file_name).is_file()