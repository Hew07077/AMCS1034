message = input("Enter a string:").strip()

words = message.split()

acyronm = ""

for word in words:
    acyronm += word[0].upper()

print("The acryonm for '{}' is '{}'".format(message.strip(),acyronm))