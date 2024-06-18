# this is their solution but they want it to print out exactly like this

#my name is Tim Tester, I am 20 years old

#my skills are
# - python (beginner)
# - java (veteran)
# - programming (semiprofessional)

#I am looking for a job with a salary of 2000-3000 euros per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is ", name, " , I am ", age, "years old")
print("my skills are")
print("- ", skill1, " (", level1, ")")
print("- ", skill2, " (", level2, ")")
print("- ", skill3, " (", level3, " )")
print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")

# my solution would be

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is", name + ",", "I am", age, "years old")
print("\nmy skills are")
print(" -", skill1 + " (" + level1 + ")")
print(" -", skill2 + " (" + level2 + ")")
print(" -", skill3 + " (" + level3 + ")")
print("\nI am looking for a job with a salary of", str(lower) + "-" + str(upper) + " euros per month")

# to fix this program to display correctly i had to first make it show as 8 lines rather than 6 so i used an "\n" which adds a new line in between

# the second thing to tackle was the indented lines for the skills list which i did by removing the space at the end of the "- " and then adding one to the beginning making it " -"

# to fix the formatting in the parentheses i had changed out the ","s to "+" when displaying the strings

