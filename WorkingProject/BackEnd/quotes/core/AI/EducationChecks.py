from . ParseHelpers import *


# Somethings to check for:
    # Applicant has a Bachelor or Master's degree in CS, SENG or Electrical Eng or Comp Eng
    # Applicant's GPA > 3.5, or not written at all 

def education_checks(block_of_text):
	#print(block_of_text)       
    #print("\n")
	score = 0
	comments = []  
	
	if (isSubString(block_of_text, "Computer Science")):
		score += 10
	
	elif (isSubString(block_of_text, "CS")):	
		score += 10
	
	elif (isSubString(block_of_text, "Software Engineering")):	
		score += 10
	
	elif (isSubString(block_of_text, "Electrical Engineering")):	
		score += 10
	
	elif (isSubString(block_of_text, "Computer Engineering")):	
		score += 10
		
	else:
		score = -10
		comments.append("In today's job market, a degree in CS or Engineering is expected.")

	#TO-DO: Check GPA


    
	return score, comments
