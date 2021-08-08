# python 3.7.1
#             Corporate Renaming

import re

def corporate_rename(sentence):
  for replace_word, new_word in word_dict.items():
    sentence = re.sub(replace_word, new_word, sentence)
    
  #Print output
  print("\nOutput:\n")
  print(sentence)

#Taking inputs 
#that is words to rename
n = int(input())
word_dict = dict()
for _ in range(n):
  word_to_rename, new_word = input().split(' to ')
  word_dict.update({word_to_rename:new_word})
 

# Input sentence 
print("\n", word_dict, "\n")
m = int(input())
sentences = ""
for _ in range(m):
  temp_str = input()
  sentences += temp_str + "\n"

#Rename and display sentence 
corporate_rename(sentences)

    
