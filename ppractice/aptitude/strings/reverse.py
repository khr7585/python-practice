# 1.using two pointers
s=input("enter a string:")
chars=list(s)
left=0
right=len(chars)-1
while left<right:
    chars[left],chars[right]=chars[right],chars[left]
    left+=1
    right-=1
    reversed="".join(chars)
print(reversed)

# 2.using loop
s=input("enter a string:")
reversed=""
for ch in s:
    reversed=ch+reversed
print(reversed)

#3.using slicing
s=input("enter a string:")
reversed=s[::-1]
print(reversed)

#4.reverse a sentence
s=input("enter a sentence:")
words=[]
word=""
for ch in s:
    if ch!=" ":
        word+=ch
    else:
        words.append(word)
        word=""
words.append(word)
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")