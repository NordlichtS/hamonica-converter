# ATTENTION: 
# 1. in original tabs text, no spaces allowed at beginning or end of a line.
# 2. must delete or rename the translated file from last time, or the new output can't be written.
# 3. run from directory (better be the directory written down there.) is better than from VScode
import re
# print('Hello World, welcome to harpnote translator')
key = {
    #"0" :"",
    "1" :"A--",
    "-1" :"o--",
    "2" :"-A-",
    "-2" :"-o-",
    "3" :"--A.",
    "-3" :"--o.",
    "4" :"---.A",
    "-4" :"---.o",
    "5" :"---.-A",
    "-5" :"---.-o",
    "6" :"---.--A.",
    "-6" :"---.--o.",
    "7" :"---.---.A",
    "-7" :"---.---.o",
    "8" :"---.---.-A ",
    "-8" :"---.---.-o ",
    "9" :"---.---.--A- ",
    "-9" :"---.---.--o- ",
    "10" :"---.---.---A. ",
    "-10" :"---.---.---o. ",
  }

# num_lines = eval(input("Enter the number of lines of the song : "))
# l_notes_input = []
# l_notes_list = []
# for i in  range(num_lines) :
#  l_notes_input.append(input("Enter a line of the song : "))
# for i in range(num_lines) :
#  l_notes_input[i] = re.sub("[ ]{2,}", " ", l_notes_input[i])

#  l_notes_list.append(l_notes_input[i].split(" "))
 
#  new_values = []
#  for n in l_notes_list[i] :
#   new_values.append(key[n])
#  print("\n".join(new_values))

import os
PATH = "c:/Users/22082/Documents/codesbackup/"
for filename in os.listdir(PATH):
    file_input = open(os.path.join(PATH, 'notes_input.txt')) #.read()
new_file = ""
for line in file_input :
    if line[0] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "-"] : 
        l = re.sub("[ ]{2,}", " ", line)  #to merge spaces
        l = l.replace('\n', '')
        new_notes = []
        notes = l.split(' ')
        for n in notes :
            new_notes.append(key[n] + "\n")
        new_file += "".join(new_notes) + "\n"
    else :
        new_file += line
translation = open('music_translation.txt', 'w')
translation.write(new_file)
print("The file 'notes_input.txt' was translated into 'music_translation.txt' successfully!")
input('Press enter to close the window!')