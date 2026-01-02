#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []
with open("MailMergeChallenge/Input/Names/invited_names.txt", "r") as file:
    for line in file:
        names.append(line.strip())


message_txt = ""
with open("MailMergeChallenge/Input/Letters/starting_letter.txt", "r") as file:
    message_txt = file.read()

for name in names:
    with open(f"MailMergeChallenge/Output/ReadyToSend/letter_for_{name}.docx", "w") as letter:
        new_message = message_txt.replace("[name]", name)
        letter.write(new_message)
