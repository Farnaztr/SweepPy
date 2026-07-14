import os
import shutil

folder = []
while True:
    direct = input("Enter the direction of your folder: ")
    if os.path.isdir(direct):
        folder = os.listdir(direct)
        break
    else:
        print("Enter correctly:/")
images = []
pdf = []
python_files = []
music = []
documents = []
others = []
if not os.path.exists(os.path.join(direct, "images")):
    os.mkdir(os.path.join(direct, "images"))

if not os.path.exists(os.path.join(direct, "pdf")):
    os.mkdir(os.path.join(direct, "pdf"))

if not os.path.exists(os.path.join(direct, "python")):
    os.mkdir(os.path.join(direct, "python"))

if not os.path.exists(os.path.join(direct, "music")):
    os.mkdir(os.path.join(direct, "music"))

if not os.path.exists(os.path.join(direct, "documents")):
    os.mkdir(os.path.join(direct, "documents"))

if not os.path.exists(os.path.join(direct, "others")):
    os.mkdir(os.path.join(direct, "others"))

for file in folder:
    path = os.path.join(direct, file)
    if os.path.isfile(path):
        if file.endswith((".png", ".jpg", ".jpeg")):
            images.append(file)
            shutil.move(os.path.join(direct, file), os.path.join(direct, "images", file))
            print(f"*{file}* moved to images folder:)")


        elif file.endswith(".pdf"):
            pdf.append(file)
            shutil.move(os.path.join(direct, file), os.path.join(direct, "pdf", file))
            print(f"*{file}* moved to pdf folder:)")
            
        elif file.endswith(".py"):

            python_files.append(file)
            shutil.move(os.path.join(direct, file), os.path.join(direct, "python", file))
            print(f"*{file}* moved to python folder:)")
            
        elif file.endswith((".mp3", ".wav", ".flac", ".aac")):
            music.append(file)

            shutil.move(os.path.join(direct, file), os.path.join(direct, "music", file))

            print(f"*{file}* moved to music folder:)")
            
        elif file.endswith((".txt", ".docx", ".xlsx", ".pptx", ".csv")):
            documents.append(file)

            shutil.move(os.path.join(direct, file), os.path.join(direct, "documents", file))
            print(f"*{file}* moved to documents folder:)")
            
        else:
            others.append(file)
            shutil.move(os.path.join(direct, file), os.path.join(direct, "others", file))
            print(f"*{file}* moved to others folder:)")
    else:
        print(f"{file} is a folder,we skipped-")

print("-"*30)

print(f"Images: {len(images)}")
print(f"PDFs: {len(pdf)}")

print(f"Python files: {len(python_files)}")
print(f"Music files: {len(music)}")

print(f"Documents: {len(documents)}")
print(f"Others: {len(others)}")
print("-"*30)