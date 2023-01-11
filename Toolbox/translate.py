#! python3

# Apprentissage de Python : https://www.youtube.com/watch?v=rfscVS0vtbw&list=WL&index=59&t=10227s
# 2:55:00

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiouy":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase")))