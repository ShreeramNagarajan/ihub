import os
import shutil
import time
from datetime import datetime

source="C:\\Users\\nrshr\\OneDrive\\Desktop\\ihub2"
destination="C:\\Users\\nrshr\\OneDrive\\Desktop\\destination"
log_file="log_file.txt"

def log_transfer(filename):
    with open(log_file,"a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - Moved file: {filename}\n")

def movefile(file):
    source_file=os.path.join(source,file)
    destination_file=os.path.join(destination,file)

    try:
        shutil.move(source_file,destination_file)
    
    except:
        print(f"error in moving file {file}")

def moniter_file():
    current_files=set(os.listdir(source))

    while True:
        try:
            new_file = set(os.listdir(source))
            new_files = new_file-current_files

            for filename in new_files:
                movefile(filename)
                log_transfer(filename)
                

            current_files = new_file
            time.sleep(1)  

        except Exception as e:
            print(f"Error accessing source folder: {e}")
            time.sleep(5)

if __name__== "__main__":
    print("files are monitering")
    moniter_file()














