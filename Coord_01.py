import os
import subprocess

exe_path = "Coord_Foto.exe"
images_dir = "./images/L1"  # Images Path

files = os.listdir(images_dir)
print("files: {0}".format(files))
image_files = [f for f in files if f.lower().endswith('.jpg')]  # List JPG files
print("image_files: {0}".format(image_files))

for image_file in image_files:
    print("image_file: {0}".format(image_file))
    image_path = os.path.join(images_dir, image_file)
    
    # Replace backslashes with forward slashes
    image_path = image_path.replace("\\", "/")
    
    print("image_path: {0}".format(image_path))
    command = f"{exe_path} {image_path}"  # EXE + Image Path
    
    print("command: {0}".format(command))
    subprocess.run(command, shell=True)
    print(f"Processed {image_file}")