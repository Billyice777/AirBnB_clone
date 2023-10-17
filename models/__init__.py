#!/usr/bin/env python3
""" Creates a unique FileStorage instance for application """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
