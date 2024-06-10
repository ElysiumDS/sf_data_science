with open('pi_digits.txt') as file_object: #with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())