from . ParseHelpers import *
from . Parser import *
from . GeneralChecks import *
from . EducationChecks import *
from . SkillsChecks import *
from . ExperienceChecks import *
from . FormattingChecks import *

possibleHeaders = {
	"Education" : "Education",
	"Schooling" : "Education",
	"Training" : "Education",
	"Credentials" : "Education",
	"Studies" : "Education",
	"Academics" : "Education",
	"Academic History" : "Education",
	
	"Experience" : "Experience",
	"Employment" : "Employment",
	"Volunteering" : "Volunteering",
	"Activities" : "Experience",
	
	"Skills" : "Skills",
	"Skill-Set" : "Skills",
	"Skillset" : "Skills",
	"Skill" : "Skill",
	
	"Project" : "Projects",
	"Ventures" : "Projects",
	"Publications" : "Projects"
}


class Result:	
	dict = {}
	def __init__ (self, totalScore, educationScore, educationComments, experienceScore, experienceComments, formattingScore, formattingComments, app_name, details):
		self.dict = {'totalScore': totalScore, 'educationScore': educationScore, 'educationComments': educationComments, 
		'experienceScore': experienceScore, 'experienceComments': experienceComments, 'formattingScore': formattingScore, 
		'formattingComments': formattingComments, 'name': app_name, 'detail': details}

# This method will parse the file			
def compute(doc):
	font_counts, styles, tags, paragraphs = pdfParse(doc)
	
	
	
	skills_block = getSection(paragraphs, "Skills")
	education_block = getSection(paragraphs, "Education")
	experience_block = getSection(paragraphs, "Experience")
	skill_block = getSection(paragraphs, "Skill")
	project_block = getSection(paragraphs, "Project")
	
	educationScore, educationComments = education_checks(education_block)
	skillsScore, skillsComments = skills_checks(skills_block)
	experienceScore, experienceComments = experience_checks(experience_block + skill_block + project_block)
	formattingScore, formattingComments = formatting_checks(font_counts, styles, tags, paragraphs)
	totalScore = educationScore + skillsScore + experienceScore + formattingScore
	
	res = Result(str(int(totalScore)), educationScore, educationComments, experienceScore, experienceComments, formattingScore, formattingComments, "NoName", "N/A")
	
	return res.dict


    

