string=input("Enter the string:")
characterCount=0
wordCount=1
for i in string:
    characterCount=characterCount+1
    if(i==''):
        wordCount=wordCount+1
print("Number of word in a string:")
print(wordCount)        
print("Number of characters in a string:")
print(characterCount)