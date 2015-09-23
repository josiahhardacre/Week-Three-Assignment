#Intro to Computers
#Josiah Hardacre
#Star Wars Name
#9/23/15

#Prompt the user to input their First and Last name and their mother's maiden name and the city where they where born.

last =input("What is your last name: ")
first =input("What is your first name: ")
maiden =input("What is your mother's maiden name: ")
town =input("What is the town you were born: ")

#Calculate their "Star Wars" name.

starfirst = last[0:3] + first[0:2]
starlast = maiden[0:2] + town[0:3]

#Print out their "Star Wars" name.

print(starfirst.capitalize(), starlast.capitalize())
