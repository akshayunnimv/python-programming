V=['a','e','i','o','u','A','E','I','O','U']
word=input("enter the text")
s=[i for i in word if i in V]
u=[i for i in word if i not in V]
print("the list of non vowel item",u)
print("the list of vowels",s)