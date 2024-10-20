import os

class FilePathExtractor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": ""})
            }
        }

    CATEGORY = "Custom Nodes"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("File Name", "File Extension", "File Name With Extension", "Folder Name", "Folder Path")
    FUNCTION = "process"

    @staticmethod
    def IS_CHANGED():
        return True

    def process(self, path):
        if os.path.isfile(path):
            file_name_with_extension = os.path.basename(path)
            file_name = os.path.splitext(file_name_with_extension)[0]
            file_extension = os.path.splitext(path)[1][1:]
            folder_path = os.path.dirname(path)
            folder_name = os.path.basename(folder_path)
        elif os.path.isdir(path):
            file_name = ""
            file_extension = ""
            folder_path = os.path.abspath(path)
            folder_name = os.path.basename(folder_path)
            file_name_with_extension = ""
        else:
            file_name = ""
            file_extension = ""
            folder_path = ""
            folder_name = ""
            file_name_with_extension = ""

        return file_name, file_extension, file_name_with_extension, folder_name, folder_path
