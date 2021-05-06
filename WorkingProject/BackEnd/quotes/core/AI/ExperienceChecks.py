from .ParseHelpers import *

job_experience = ['work','intern','co-op','job','volunteer']
program_experience = ['Python','Java','JavaScript','C','C++','Ruby','Ruby on Rails','HTML','C#','Swift','Go']

def experience_checks(lines):
    job_score = 0
    program_score = 0
    final_job_score = 0
    final_program_score = 0
    comments = [""] 
    final_comment = [""]

    for each_line in lines:
         for job_experience_word in job_experience:
         	if (isSubString(each_line, job_experience_word) == True):
         		job_score += 1
         
         for program_experience_word in program_experience:
         	if (isSubString(each_line, program_experience_word) == True):
         		program_score += 1
         
    final_job_score = (job_score / 4) * 100
    final_program_score = (program_score / 11) * 100
    
    if final_job_score < 50:
    	comments.append("You seem to be a little inexperienced")
    
    if final_program_score < 50:
    	comments.append("Your experiences seem to be lacking in technology and programming lanugage variety")
    
    else:
    	comments.append("Your experince looks great!")

    return (final_program_score + final_job_score), comments
    
    
    
    
    
    
    
    
    
    
    
