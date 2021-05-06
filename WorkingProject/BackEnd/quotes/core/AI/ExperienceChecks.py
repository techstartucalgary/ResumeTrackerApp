from .ParseHelpers import *
from .GeneralChecks import *

job_experience = ['work','intern','co-op','job','volunteer', 'developer', 'engineer', 'scientist', 'coordinator', 'manager']

all_programming_languages = ['Python','Java','JavaScript','C','C++','Ruby', 'Assembly', 'HTML','C#','Swift','Go', 'Haskell', 'Prolog', 'Lisp', 'Bash']

# Skills for front-end development 
front_end_skills = ['Atom', 'Visual Studio', 'VS', 'Sublime Text', 'Git', 'Apache', ' HTML', 'CSS', 'Bootstrap', 'Javascript', 'jQuery', 'React', 'Vue', 'Angular']

# Skills for back-end development 
back_end_skills = ['Python', 'Java', 'PHP', 'SQL', 'Git', 'HTML', 'CSS', 'JavaScript', 'Django', 'NoSQL', 'NET', 'C#', 'Server', 'API', 'REST', 'SOAP', 'Redis', 'Apache', 'Swift','Go']

# Skills for AI and data scientists
ai_skills = ['Neural Networks', 'Machine Learning', 'Python', 'R', 'Data Science', 'Hadoop', 'Java', 'Spark', 'TensorFlow', 'Pandas', 'NumPy', 'PyTorch', 'Parsing', 'Haskell', 'Prolog']

# Skills for embedded programers (also including network engineers)
embedded_skills = ['C', 'C++', 'Assembly', 'processor', 'controller', 'scheduler', 'OS', 'Operating System', 'Linux', 'Java', 'FPGA', 'VHDL', 'Verilog', 'GDB', 'Kernel', 
'Networks', 'RTOS', 'ARM', 'Bash', 'Multi Threading', 'Multithreading', 'Parallel', 'Process', 'File System', 'Memory', 'Kubernetes', 'Security', 'WiFi', 'Ethernet', 'IoT', 
'IPv6', 'IPv4', 'IP', 'TCP', 'UDP', 'Link Layer', 'Socket', 'HTTP', 'Cloud', 'BGP', 'OSPF', 'MPLS', 'QoS', 'STP', 'RIP', 'LAN', 'DHCP', 'DNS']

program_experience = ['Python','Java','JavaScript','C','C++','Ruby', 'Assembly', 'HTML','C#','Swift','Go', 'Haskell', 'Prolog', 'Lisp', 'Bash']
tools = ['SQL', 'NET', 'React', 'Node', 'Express', 'Ruby on Rails', 'Django', 'AWS', 'Azure', 'Docker', 'Git', 'PHP', 'Jenkins', 'Eclipse', 'Visual Studio',
'VS', 'IED', '']




def experience_checks(lines):
    total_score = 0
    job_score = 0
    front_end_score = 0
    back_end_score = 0
    ai_score = 0
    embedded_score = 0
    program_score = 0
    final_job_score = 0
    final_program_score = 0
    comments = [""] 
    final_comment = [""]
    all_comments = []
   # print(block_of_text)

	# General check
    general_words_score = 0
    num_weak_verbs, num_strong_verbs, weak_verbs_detected = general_words_check(lines)
    general_words_score = general_words_score + num_strong_verbs - num_weak_verbs
    if num_strong_verbs > 0:
    	all_comments.append("Good use of strong descriptor words.")
    if num_weak_verbs > 0:
    	all_comments.append("Avoid these weak descriptor words detected: " + weak_verbs_detected)
    
	
	# Quantity of Experience Check
    job_score = 0
    job_score = job_score + innCount(lines, job_experience)  
    job_score = (job_score / 4) * 100
    if job_score < 50:
    	comments.append("You seem to have had few experiences.")
	
	# Software Industry Checks
    software_score = 0
    front_end_score = front_end_score + innCount(lines, front_end_skills)
    back_end_score = back_end_score + innCount(lines, back_end_skills)
    ai_score = ai_score + innCount(lines, ai_skills)  
    embedded_score = embedded_score + innCount(lines, embedded_skills)  
    software_score = front_end_score + back_end_score + ai_score + embedded_score
    

	# Industry-Specific Coverage Check
    coverage_score = 0
    num_high_coverage = 0
    coverages_detected = ""
    front_end_coverage = float(front_end_score)/len(front_end_skills)
    if (front_end_coverage > 0.40):
    	num_high_coverage = num_high_coverage + 1
    	coverages_detected = coverages_detected + "Front End"
    	
    back_end_coverage = float(back_end_score)/len(back_end_skills)
    if (back_end_coverage > 0.40):
    	num_high_coverage = num_high_coverage + 1
    	if (num_high_coverage > 1):
    		coverages_detected = coverages_detected + ", "
    	coverages_detected = coverages_detected + "Back End"
    	
    ai_coverage = float(ai_score)/len(ai_skills)
    if (ai_coverage > 0.40):
    	num_high_coverage = num_high_coverage + 1
    	if (num_high_coverage > 1):
    		coverages_detected = coverages_detected + ", "
    	coverages_detected = coverages_detected + "AI"
    	
    embedded_coverage = float(embedded_score)/len(embedded_skills)
    if (embedded_coverage > 0.40):
    	num_high_coverage = num_high_coverage + 1
    	if (num_high_coverage > 1):
    		coverages_detected = coverages_detected + " and "
    	coverages_detected = coverages_detected + "Embedded Systems"
        
    
    if (num_high_coverage == 0):
    	comments.append("Your experiences lack the key skills of any particular industry. Learn more programming languages, tools and platforms.")
    	
    
    else:
    	comments.append("Your skills are in high demand for the following industries: " + coverages_detected + ".")
    	if (num_high_coverage == 1):
    		comments.append("Your resume is quite focused on one particular industry. This can be good, but always consider widening your search.")
    		coverage_score = 80
    	
    	elif (num_high_coverage == 2):
    		comments.append("Your resume is focused on two industries. In general, having focused resumes is desired.")
    		coverage_score = 100
    	
    	else:
    		comments.append("Your resume is too broad and general. Consider focusing on two industries you're interested in so that hiring teams can better pin-point your skills.")
    		coverage_score = 40
    
    
    total_score = int((general_words_score*0.10) + (job_score*0.20) + (software_score*0.40) + (coverage_score*0.30))

    return total_score, comments
    

    
    
    
    
    
    
