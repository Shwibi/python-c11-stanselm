
# Practice: 18/8/2021 
# Conditional Statements with calculation
# Program 1

physics = int(input("Enter marks in physics: "))
chemistry = int(input("Enter marks in chemistry: "))
biology = int(input("Enter marks in biology: "))

total = physics + chemistry + biology
percentage = total/3

print("Total marks: ", total)
print("Total percentage: ", percentage)

if percentage >= 40:
  print("You passed")
else:
  print("You failed")

