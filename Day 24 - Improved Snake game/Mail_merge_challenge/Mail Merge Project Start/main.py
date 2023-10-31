#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis +method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_list = []
with open('Input/Names/invited_names.txt') as data:
    pre_names = data.readlines()
with open('input/Letters/starting_letter.txt') as data:
    letter = data.read()
for n in pre_names:
    names = n.strip()
    name_list.append(names)
for n in name_list:
    x = letter.replace('[name]', n)
    with open(f'Output/ReadyToSend/letter_for_{n}', 'w') as file:
        file.write(x)
