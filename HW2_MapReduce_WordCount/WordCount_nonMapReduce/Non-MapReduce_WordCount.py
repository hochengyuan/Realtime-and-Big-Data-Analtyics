
# coding: utf-8

# In[1]:

import re

def count_keyword_in_tweet( inputFile , keyword ):
    # open and read the inputFile:
    input = open( inputFile , 'r' , encoding = 'UTF-8')
    lines = input.read().lower() # each line is lowercased
    lines = lines.split('\n') # transfer lines to a list of strings
    input.close()
    
    # strip punctuation marks
    lines = [re.sub(r'[^A-Za-z0-9]+', ' ', each_line) for each_line in lines]
    
    # count total lines contain input keywords 
    count = 0
    keyword = keyword.lower()
    for each_line in lines:
        if keyword in each_line:
            count += 1
    
    return count


chicago = "Chicago " + "%d"%count_keyword_in_tweet("input_sample.txt" , "Chicago")
dec = "Dec " + "%d"%count_keyword_in_tweet("input_sample.txt" , "Dec")
java = "Java " + "%d"%count_keyword_in_tweet("input_sample.txt" , "Java")
hackathon = "hackathon " + "%d"%count_keyword_in_tweet("input_sample.txt" , "hackathon")

to_output_String = chicago + '\n' + dec + '\n' + java + '\n' + hackathon

with open('job_output.txt' , 'w' , encoding = 'UTF-8') as output:
    output.write(to_output_String)


# In[2]:

print(to_output_String)

