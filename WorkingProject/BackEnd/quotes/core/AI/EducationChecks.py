from . ParseHelpers import *


# Somethings to check for:
    # Applicant has a Bachelor or Master's degree in CS, SENG or Electrical Eng or Comp Eng
    # Applicant's GPA > 3.5, or not written at all 

def education_checks(block_of_text):
    #print(block_of_text)        # To help you view what the argument looks like
    #print("\n")

    if ('Computer Science') or ('Electrical Engineering') or ('Software Engineering') or ('Computer Engineering') in block_of_text:
        score += 10; 

#TO-DO: Check GPA

    #score = 0
    comments = ["testComment"]  # you can add comments by comments.append("......")
    return score, comments
