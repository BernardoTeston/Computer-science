'''
s1 = "spam"
s2 = "ni! "
s1 [1]
'''
'''
s1 = "spam"
s2 = "ni! "
s1 [1 : 3]
'''
'''
s1 = "spam"
s2 = "ni! "
s1 . upper()
'''

#exercise 2
'''
s1 = "spam"
s2 = "ni! "
result = s2.upper()[:3]


s1 = "spam"
s2 = "ni! "
result = " " + s1


s1 = "spam"
s2 = "ni! "
result = [" " + s1[0:2], s1[2]]
'''

#exercise 3
'''
for w in "Now is the winter of our discontent . . . " . split ( ) :
 print (w)
#output
# Now
is
the
winter
of
our
discontent
.
.
.


for w in "Mississippi ".split("i"):
   print(w, end=" ")
#output
  M ss ss pp   


msg = " "
for ch in " secret " :
 msg = msg + chr (ord (ch) +1)
 print (msg)
#output 
!
 !t
 !tf
 !tfd
 !tfds
 !tfdsf
 !tfdsfu
 !tfdsfu!
 
#exercise 4
grades = ""

for _ in range(60): 
    grades += 'F'
for _ in range(10):  
    grades += 'D'
for _ in range(10):  
    grades += 'C'
for _ in range(10):  
    grades += 'B'
for _ in range(10):  
    grades += 'A'

print(f'grades = "{grades}"')





#exercise 5

score = float(input("Enter the exam score: "))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'

print("The grade is:", grade)


#exercise 6

phrase = input("Enter a phrase: ")

acronym = ''.join(word[0].upper() for word in phrase.split())

print(acronym)
 

#exercise 7

name = input("Welcome! Please enter your name: ")

numeric_value = sum(ord(char) - ord('a') + 1 for char in name.lower() if char.isalpha())

print(f"The numeric value of your name '{name}' is: {numeric_value}")
'''