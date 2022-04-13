PLACE_HOLDER = "[name]"
index = 1
output_mail = f"output_mail_{index}"
print(output_mail)
with open("./Input/Names/invited_names.txt", mode='r') as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


