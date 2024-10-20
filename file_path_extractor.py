import os

class FilePathExtractor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": "", "multiline": True, "width": 400})  # Adjust height
            }
        }

    CATEGORY = "Custom Nodes"
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("File Name", "File Extension", "File Name With Extension", "Folder Name", "Folder Path")
    FUNCTION = "process"

    @staticmethod
    def IS_CHANGED():
        # Always return True to force the node to run on every iteration
        return True

    def process(self, path):
        folder_path = os.path.dirname(path) if os.path.dirname(path) else path  # Use folder part of the path, even if it doesn't exist
        folder_name = os.path.basename(folder_path)
        file_name_with_extension = os.path.basename(path)
        file_name, file_extension = os.path.splitext(file_name_with_extension)
        file_extension = file_extension[1:]  # Strip leading dot from extension

        return file_name, file_extension, file_name_with_extension, folder_name, folder_path