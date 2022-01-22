# modify strings

# upper() method
# it returns the string in upper case
s1 = "soumadittya"
s1 = s1.upper()
print("s1 : ", s1)

# lower() case
# it returns the string in lower case
s2 = "SOUMADITTYA"
s2 = s2.lower()
print("s2 : ", s2)

# strip() function
# it returns a string that has all the whitesapces
# removed from the beginning and the end
s3 = "    soumadittya ghosh    "
s3 = s3.strip()
print("s3 : ", s3)

# replace() method
# it returns a string after replacement
s4 = "I am in VIT"
s4 = s4.replace("VIT", "Appointy")
print("s4 : ", s4)

# split() function
# it returns a list after splitting using a specific piece of string
s5 = "I am Soumadittya"
s5_array = s5.split(" ")
print("s5 : ", s5_array)

# format() function
quantity = 3
itemno = 567
price = 49.95
s6 = "I want {} pieces of ite   m {} for {} dollars."
s6 = s6.format(quantity, itemno, price)
print("s6 : ", s6)