s=input("enter a string1:")
s1=input("enter a string2:")
freq={}
freq1={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in s1:
    if ch in freq1:
        freq1[ch]+=1
    else:
        freq1[ch]=1
if freq==freq1:
    print("anagram")
else:
    print("not anagram")
    
    
#longest word in a sentence
s=input("enter a sentence:")
word=""
longest=""
for ch in s:
    if ch!=" ":
        word+=ch
    else:
        if len(word)>len(longest):
            longest=word
        word=""
if len(word)>len(longest):
    longest=word
print("longest",longest)
print("length",len(longest))