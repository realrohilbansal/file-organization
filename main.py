import os
import shutil

# Define the directory path
dirpath = "/home/rohil/Downloads"

# Create subdirectories if they don't exist
if not os.path.exists(dirpath + "/Images"):
    os.makedirs(dirpath + "/Images")

if not os.path.exists(dirpath + "/Music"):
    os.makedirs(dirpath + "/Music")

if not os.path.exists(dirpath + "/Videos"):
    os.makedirs(dirpath + "/Videos")

if not os.path.exists(dirpath + "/Documents"):
    os.makedirs(dirpath + "/Documents")

if not os.path.exists(dirpath + "/Code"):
    os.makedirs(dirpath + "/Code")

if not os.path.exists(dirpath + "/Other"):
    os.makedirs(dirpath + "/Other")

# Lists of file extensions for different categories
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
music_extensions = [".mp3", ".wav", ".aiff"]
video_extensions = [".mp4", "mkv"]
doc_extensions = [".txt", ".pdf", ".docx", ".doc", ".md", ".epub"]
code_extensions = [".json", ".py", ".ipynb", ".cpp", ".c", ".js", ".rs"]

# Iterate through files in the directory
for file in os.listdir(dirpath):
    # Skip processing if the item is a subdirectory
    if os.path.isdir(dirpath + "/" + file):
        continue

    # Skip processing of .DS_Store files
    if file == ".DS_Store":
        continue

    # Get the file extension in lowercase
    extension = os.path.splitext(file)[1].lower()

    # Move the file to appropriate subdirectories based on the extension
    if extension in image_extensions:
        shutil.move(dirpath + "/" + file, dirpath + "/Images")
        
    elif extension in music_extensions:
        shutil.move(dirpath + "/" + file, dirpath + "/Music")
    
    elif extension in video_extensions:
        shutil.move(dirpath + "/" + file, dirpath + "/Videos")

    elif extension in doc_extensions:
        shutil.move(dirpath + "/" + file, dirpath + "/Documents")

    elif extension in code_extensions:
        shutil.move(dirpath + "/" + file, dirpath + "/Code")
    
    else:
        shutil.move(dirpath + "/" + file, dirpath + "/Other")
