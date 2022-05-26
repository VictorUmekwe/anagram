# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

 string1 = input("first_word")
 string2 = input("second word")
first_word = "funeral"
second_word = "realfun" 
   # strings are sorted and verified 

if(sorted(first_word)== sorted(second_word)):
    print("True")
else:
    print("False")    
   
   
   
   
    

