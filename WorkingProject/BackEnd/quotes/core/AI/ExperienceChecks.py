from .ParseHelpers import *

job_experience = ['work','internship','co-op','job','volunteer']
program_experience = ['Python','Java','JavaScript','C','C++','Ruby','Ruby on Rails','HTML','C#','Swift','Go']

def experience_checks(lines):
    # print(block_of_text)		# To help you view what the argument looks like
    # print("\n")
    job_score = 0
    program_score = 0
    # final_job_score = 0
    # final_program_score = 0
    comments = [""]  # you can add comments by comments.append("......")
    # program_comments = [""]
    # job_comments = [""]
    comment = ["Good Experience\n"]
    final_comment = [""]

    for each_line in lines:
        words = lines.split()
        for each_word in words:

            for job_experience_word in job_experience:
                if (isSubString(each_word, job_experience_word) == True):
                    job_score += 1
                    print(each_word)
                    print(comment)

            for program_experience_word in program_experience:
                if (isSubString(each_word, program_experience_word) == True):
                    program_score += 1
                    print(each_word)
                    print(comment)

            final_job_score = (job_score / 4) * 100
            final_program_score = (program_score / 11) * 100

            if final_job_score < 50:
                comments.append("You seem to be a little more inexperienced\n")

            if final_program_score < 50:
                comments.append("You seem to be lacking in programming lanugage variety\n")

            else:
                comments.append("Your experince looks great!")



    return final_program_score, final_job_score, com
