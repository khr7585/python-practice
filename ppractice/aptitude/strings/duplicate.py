# s=input("enter a string:")
# dupe={}
# for ch in s:
#     if ch in dupe:
#         dupe[ch]+=1
#     else:
#         dupe[ch]=1
# print("duplicates:")
# for ch in dupe:
#     if dupe[ch]>1:
#         print(ch)
        
# frequency
# s=input("enter a string:")
# freq={}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# for ch in freq:
#     print(ch,":",freq[ch])
    
#remove duplicate
s=input("enter a string:")
seen=set()
result=""
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result+=ch
print(result)
        
        
#first non-repeating character
s=input("enter a string:")
found=False
for i in range(len(s)):
    count=0
    for j in range(len(s)):
        if s[i]==s[j]:
            count+=1
    if count==1:
        print("first non-repeating character is:",s[i])
        found=True
        break
if found==False:
    print("no first non-repeating characters")