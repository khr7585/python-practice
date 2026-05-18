#1.CASE METHODS
# h="hemanth"
# print(h.upper())
# print(h.lower())
# print(h.capitalize())
# print(h.title())
# print(h.swapcase())


#2.SEARCH & FIND METHODS
# s="hemanth"
# print(s.find("e"))
# print(s.index("m"))
# print(s.count("h"))
# print(s.startswith("he"))
# print(s.endswith("th"))


#3.REPLACE AND REMOVE METHODS
# s=" hem anth "
# print(s.strip())  #remove spaces front and back
# print(s.replace("e","a"))
# print(s.lstrip())
# print(s.rstrip())


#4.SPLIT AND JOIN METHODS(split(),rsplit(),splitlines(),join())
# s="apple,banana,orange"
# words=s.split(",")
# print("-".join(words))
# text="line1\line2\line3"
# print(text.splitlines())


#5.CHECK OR VALIDATE METHODS
# s="Hemanth"
# print(s.isalpha())  #only letters
# print(s.isdigit())  #only digits
# print(s.isalnum())  #letters or digits
# print(s.isspace())  #only spaces
# print(s.isupper())  
# print(s.islower())
# print(s.istitle())
# print(s.isnumeric())
# print(s.isdecimal())


#6.ALIGNMENTS /PADDDING METHODS
# s="hemanth"
# print(s.center(11,"-"))
# print(s.ljust(10,":"))
# print(s.rjust(10,"/"))
# print("69".zfill(4))