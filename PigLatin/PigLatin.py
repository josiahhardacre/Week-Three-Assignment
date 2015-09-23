#Intro to Computers
#Josiah Hardacre
#Pig Latin
#9/23/15

#The program should prompt the user to enter an English word to translate.  

originalword = input("Write an English word you want translated to PigLatin: ")
vowels = "aeiouAEIOU"
endofvowel = "yay"
endofconsonant = "ay"
if (originalword[0] in vowels):
    print((originalword + endofvowel).capitalize())
    
else:
    print((originalword[1:] + originalword[0] + endofconsonant).capitalize())

#The program should translate the word in to Simple Pig Latin, given the following rules.  
#The program should print the translated word.