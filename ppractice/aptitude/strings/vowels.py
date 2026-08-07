s=input("enter a string:")
vowels=0
consotants=0
for ch in s:
    if ch.lower() in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consotants+=1
print(vowels)
print(consotants)