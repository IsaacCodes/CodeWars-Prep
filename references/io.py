#For all problems:
with open("input.txt") as f:
  text = f.read().strip() #May not always need strip, usually recommended
  lines = text.split("\n") #To split it into multiple lines


#For directory based problems:
import os
files = os.listdir("files")

#Loop through the files in the directory, add logic as necessary
for file_name in files:
  
  #This is the cross platform equivilant of "files/file_name"
  file_path = os.path.join("files", file_name)

  #Now each file in the directory can be opened
  with open(file_path) as f:
    text = f.read().strip()
    #...