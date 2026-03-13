import os


class FilePathExtractor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": "", "multiline": True, "width": 400})
            }
        }

    CATEGORY = "Custom Nodes"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("File Name", "File Extension", "File Name With Extension", "Folder Name", "Folder Path")
    FUNCTION = "process"
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, True, True, True, True)

    @staticmethod
    def IS_CHANGED():
        # Always return True to force the node to run on every iteration
        return True

    @classmethod
    def _normalize_paths(cls, path):
        normalized_paths = []

        def _flatten(value):
            if isinstance(value, (list, tuple)):
                for item in value:
                    _flatten(item)
                return

            if value is None:
                normalized_paths.append("")
            else:
                normalized_paths.append(str(value))

        _flatten(path)

        if not normalized_paths:
            return [""]

        return normalized_paths

    def process(self, path):
        paths = self._normalize_paths(path)

        file_names = []
        file_extensions = []
        file_names_with_extension = []
        folder_names = []
        folder_paths = []

        for path_item in paths:
            folder_part = os.path.dirname(path_item)
            # Keep original text when no directory part is present.
            folder_path = folder_part if folder_part else path_item
            folder_name = os.path.basename(folder_path)
            file_name_with_extension = os.path.basename(path_item)
            file_name, file_extension = os.path.splitext(file_name_with_extension)
            file_extension = file_extension[1:] if file_extension.startswith(".") else file_extension

            file_names.append(file_name)
            file_extensions.append(file_extension)
            file_names_with_extension.append(file_name_with_extension)
            folder_names.append(folder_name)
            folder_paths.append(folder_path)

        return file_names, file_extensions, file_names_with_extension, folder_names, folder_paths
