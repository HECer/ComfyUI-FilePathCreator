import os

class FilePathExtractor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "test": ("STRING", {"default": ""})
            }
        }

    CATEGORY = "Custom Nodes"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("File Name", "File Extension", "Folder Name", "Folder Path")
    FUNCTION = "process"

    @staticmethod
    def IS_CHANGED():
        return True

    def process(self, test):
        if os.path.isfile(test):
            file_name = os.path.basename(test)
            file_extension = os.path.splitext(test)[1][1:]
            folder_path = os.path.dirname(test)
            folder_name = os.path.basename(folder_path)
        elif os.path.isdir(test):
            file_name = ""
            file_extension = ""
            folder_path = os.path.abspath(test)
            folder_name = os.path.basename(folder_path)
        else:
            file_name = ""
            file_extension = ""
            folder_path = ""
            folder_name = ""

        return file_name, file_extension, folder_name, folder_path
