import os
from posix import listdir

#Provide windows directory
windows_dir=input("Enter the directory or drag-and-drop the folder you wish to search: ")
#Replace backslashes with forward slashes
unix_dir= windows_dir.replace("\\","/")
#Make drive letter lowercase and remove colon
unix_lower = unix_dir[0].lower() + unix_dir[0 + 2:]

#Add /mnt/ for WSL compatibility
wsl_dir= ("/mnt/" + unix_lower)

print("\n")
print("Your path is: ", wsl_dir)
print("\n")

extension = []
pres_ext = [".mxf", ".xml"]
access_ext = [".mp4"]

#Prompt user to say if they are looking in a pres or access folder. Changes what extensions are searched for
while True:
    user_choice = input(
    "What kind of folder are you searching in?\n" 
    "1. PRES \n"
    "2. ACCESS\n"
    )
    #There's definitely a better way to do this...
    if user_choice=="PRES" or user_choice== "pres" or user_choice== "1" or user_choice== "ACCESS" or user_choice== "access" or user_choice== "2":
        break
    else:
        print("Invalid entry")
        continue

#... and this
if user_choice == "PRES" or user_choice == "pres" or user_choice == "1":
    extension = pres_ext
elif user_choice == "ACCESS" or user_choice == "access" or user_choice == "2":
    extension = access_ext
        
print(
    "\n"
    "Searching for files with ", extension, " extensions..."
    "\n"
    )

results = []

#Skips subdirectories and adds all files to the files variable
files = (file for file in os.listdir(wsl_dir)
    if os.path.isfile(os.path.join(wsl_dir, file)))

#If files do not have the correct extension, they are added to the results list
for f in files:
    if not f.endswith(tuple(extension)):
        results.append(f)

#Prints the count and names of files that have the wrong extension
print("--------------------------------------------")
if extension == pres_ext:
    print("There are", len(results), "invalid PRES files: ")
elif extension == access_ext:
    print("There are", len(results), "invalid ACCESS files: ")

for item in results:
    print(item)
print("--------------------------------------------")
