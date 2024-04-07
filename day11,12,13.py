a1="disha"
a2="i love chocolates"
a3="i am learning python"
print(a1)
print(a2)
print(a3)
print(a1[0])
print(a1[1])
print(a1[2])
print(a1[3])
print(a1[4])

print("lets use a for loop\n")
for character in a2:
    print(character)
print("\n")
for character in a3:
    print(character)
print("\n")
names="disha,rithu,tanvi"
print(names[0:5])
print(names[5:8])
print(names[6:17])
print("length of name is", len(names))
print("\n")

#strings are immutable
b= "Disha !!!!disha !!!"
print(b)
#lower() method converts a string to lower case
print(b. lower())
#upper() method converts a string to upper case.
print(b. upper())
# strip() method removes any white spaces before and after the string.
#rstrip() removes any trailing characters.
print(b. rstrip("!"))
#replace() method replaces all occurences of a string with another string
print(b. replace("disha", "tanvi"))  
#split() method splits the given string at the specified instance and returns the separated strings as list items. 
print(b. split(" "))
# capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
print(b. capitalize())
# center() method aligns the string to the center as per the parameters given by "me"
print(b. center(80))
#count() method returns the number of times the given value has occurred within the given string
print(b. count("!"))
#count() method returns the number of times the given value has occurred within the given string
print(b. endswith("!"))
print(b. endswith("a",0,5))
# find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("an"))
#index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception
# print(str1.index("ann"))[it shows an error]
#isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
#isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
str1 = "Welcome"
print(str1.isalpha())
# islower() method returns True if all the characters in the string are lower case, else it returns False.
str1 = "hellow world"
print(str1.islower())
# isprintable() method returns True if all the values within the given string are printable, if not, then return False.
str1 = "wow you are beautiful\n" #cuz \n is not printable
print(str1.isprintable())
#isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
# istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str1 = "World Health Organization" 
print(str1.istitle())
# startswith() method checks if the string starts with a given value. If yes then return True, else return False
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
# swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
# title() method capitalizes each letter of the word within the string.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())



