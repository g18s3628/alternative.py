#FOR ALTERNATE CHARACTER ACTIVITY
#Request user to input a string
sent_req = input("Please write a sentence: ")

#Variable for storing the changed string  
alt_str = ""

#Loop to find the string in the characters in the sentence
#If the character is on the even numbers then it must be an upper case else make it lower case  
for i in range(len(sent_req)):
    if i % 2 == 0:
        alt_str += sent_req[i].upper()
    else:
        alt_str += sent_req[i].lower()
print(alt_str)    

print("\n")

#FOR THE ALTERNATE WORD ACTIVITY
#Request user to input a string
#Split the words in the sentences using the spaces used between each word
#Assign the variable to store the changed words
#Keep track of words if the next should be capitals or not 
sent_req_word = input("Please write a sentence : ")
words_in_sent = sent_req_word.split()
altered_words = []
cap_next_word = True 

#For loop for the words in the sentence 
#If capital letter then make the the next word in lower case else make it a capital letter
#Join the words in with spaces in between to form sentence with spaces in between then print
for word in words_in_sent:
    if cap_next_word: 
        altered_words.append(word.upper())
    else: 
        altered_words.append(word.lower())
    cap_next_word = not cap_next_word
final_sent = " ".join(altered_words)
print(final_sent)
