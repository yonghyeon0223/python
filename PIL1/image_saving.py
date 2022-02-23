from PIL import Image
import os

# for every jpg file inside the current directory, save with another extension in other folder.
for each_file in os.listdir():
    file_name, file_extension = os.path.splitext(each_file)
    if file_extension == ".jpg":
        img = Image.open(each_file)
        img.save(f"./folder_for_saved_images/{file_name}.jpeg")