from .file_path_creator import FilePathCreator
from .file_path_extractor import FilePathExtractor

NODE_CLASS_MAPPINGS = {
    "FilePathCreator": FilePathCreator,
    "FilePathExtractor": FilePathExtractor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FilePathCreator": "File Path Creator",
    "FilePathExtractor": "File Path Extractor"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
