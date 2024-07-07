import os
from datetime import datetime

class FilePathCreator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_prefix": ("STRING", {"default": "output"}),
                "time_format": ("STRING", {"default": "%Y-%m-%d-%H%M%S"})
            },
            "optional": {
                "output_folder": ("STRING", {"default": ""}),
                "filetype": ("STRING", {"default": "txt"})
            }
        }

    CATEGORY = "Custom Nodes"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("Filename", "Folder Path", "Combined Path")
    FUNCTION = "process"

    def process(self, file_prefix, time_format, output_folder, filetype):
        output_folder = output_folder or os.path.abspath("output")
        current_time = datetime.now().strftime(time_format)
        
        if filetype:
            filename = f"{file_prefix}_{current_time}.{filetype}"
        else:
            filename = f"{file_prefix}_{current_time}"
            
        combined_path = os.path.join(output_folder, filename)
        return filename, output_folder, combined_path
