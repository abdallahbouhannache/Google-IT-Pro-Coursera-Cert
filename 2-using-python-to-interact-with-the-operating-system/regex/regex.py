#!/usr/bin/env python3


# just for notice  ## grep thon /usr/share/dict/words

import os
import re



pattern=r"\w+ \d*"
string="helpme 008"
match=re.search(pattern,string)
allmatches=re.findall(pattern,string)
print(match)
print(allmatches)

print(re.search(r"[Pp]","Python"))
print(re.search(r"[a-z]way","The end of the highway"))
print(re.search(r"cloud[a-zA-Z0-9]","the c9 cloud8"))
print(re.search(r"[^a-zA-Z]","This just a sentence with spaces."))
print(re.search(r"cat|dog","i Love Both cat and dogs."))
print(re.findall(r"cat|dog","i Love Both cat and dogs."))
#quantifiers
print(re.search(r"P.*ing","i would rather choose programming."))
print(re.search(r"P.*ing","playing with such toy is risky."))
print(re.search(r"P.*ing","gold fish."))
print(re.search(r"o+l+","wool and ooll."))
print(re.search(r"P?each","do i seem like i love peaches."))
print(re.search(r"\.com","file.com"))
#caracters
#\t \n
#\w() \d()  \s()  \b()

#^word$
#---------------------

pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"
string="_this_is_a_valid_character"
result=re.search(pattern,string)
string="this is not a valid character"
result=re.search(pattern,string)

#capturing_groups==>() the pattern enclosed between parenthesies



result=re.search(r"^(\w*), (\w*)$","lovelace, Ada")
print(result)
print(result.groups())
print(result[0],result[1],result[2])#==> "lovelace, Ada" |lovelace | Ada

result=re.search(r"^(\w{5}), (\w{2,})$","lovelace, Ada")

#advanced regex: 
#extract pid

log="July 31 07:12:00 my computer bad_process[54893]:denied to upgrade the package"
pattern=r"\[(\d+)\]"
resultwo=re.search(pattern,log)
print(resultwo)

#split

miresult=re.split(r'[?!.]',"the sentence! must not. take the last one?")
print(miresult)
#to include the characters in the result of splitting
miresult=re.split(r'([?!.])',"the sentence! must not. take the last one?")
print(miresult)

#replace 
replace_RES=re.sub(r'[\w.%+-]+@[\w.-]+','[REDACTED]',"received email for go_2urhome@myserver.freeserve.com")
print(replace_RES)

# substitute with backrefernce
replace_RES=re.sub(r'^([\w .-]*), ([\w .-]*)$',r'\2 ,\1',"received, email")
print("received, email","==>",replace_RES)
