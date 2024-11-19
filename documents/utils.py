from django.core.files.storage import default_storage
import os

# No repeat name validation
def get_unique_filename(file_name): 
    base, extension = os.path.splitext(file_name) 
    counter = 1 
    new_file_name = file_name

    while default_storage.exists(new_file_name): 
        new_file_name = f"{base}_{counter}{extension}" 
        counter += 1 
    return new_file_name