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

    CATEGORY = "FilePath Utils"
    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("Filename", "Folder Path", "Combined Path")
    FUNCTION = "process"
    
    @staticmethod
    def IS_CHANGED():
        # Always return True to force the node to run on every iteration
        return True

    def process(self, file_prefix, time_format, output_folder, filetype):
        output_folder = output_folder or os.path.abspath("output")
        
        # Erstelle den Basis-Namen mit oder ohne Zeitstempel
        if time_format and time_format.strip():
            current_time = datetime.now().strftime(time_format)
            filename = f"{file_prefix}_{current_time}"
        else:
            filename = file_prefix
        
        # Füge Extension hinzu wenn vorhanden
        if filetype:
            filename = f"{filename}.{filetype}"
            
        combined_path = os.path.join(output_folder, filename)
        return filename, output_folder, combined_path
