print("This program calculate the number of letters and digits.")
words = input("please enter a sentence:")
letters_count = 0
digits_count = 0
for word in words:
    if word.isdigit():
        digits_count += 1
    elif word.isalpha():
        letters_count += 1
    else:
        continue
print("letters:", letters_count, "digits:", digits_count)