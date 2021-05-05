from . ParseHelpers import *

acceptable_fonts = ['Calibri', 'Times New Roman', 'Cambria', 'Garamond', 'Georgia', 'Helvetica', 'Arial', 'Verdana']

def formatting_checks(font_counts, font_styles, tages, para):
	#print (font_counts)
	#print("\n\n")
	#print(font_styles)
	#print(tages)
	#print(para)
	
	# Check font sizes
	font_size_score, font_size_comments = check_font_sizes(font_counts)
	score = font_size_score
	comments = font_size_comments  # you can add comments by comments.append("......")
	
	# Check font styles 
	font_style_score, font_style_comments = check_font_styles(font_styles)
	score = score + font_style_score
	comments = comments + font_style_comments
	
	# Organize file based on header
	organized_file = organize_headers(tages, para)
	
	# Check for section independence 
	section_ind_score, section_ind_comments = check_section_independance(organized_file, para)
	score = score + section_ind_score
	comments = comments + section_ind_comments
	
	
	
	
	return score, comments


def check_font_sizes(font_counts):
	# Too small font < 10
	# Too big font > 20
	# Most frequent count should be smallest font size
	
	font_size_score = 0
	font_size_comments = []
	tooSmallFont = 0
	tooLargeFont = 0
	inconsistency = 0
	prev_font_size = -1
	
	for (font_size, font_count) in font_counts:
		# Check if font_size is too small --> if so, reduce one point
		if (float(font_size) < 10.00):
			tooSmallFont = tooSmallFont + 1
		
		if (float(font_size) > 20.00):
			tooLargeFont = tooLargeFont + 1
		
		if (not(prev_font_size == -1) and prev_font_size > float(font_size)):
			inconsistency = inconsistency + 1
		
		prev_font_size = float(font_size)
	
	if (tooSmallFont > 0):
		font_size_comments.append("Avoid font sizes smaller than 9 pt.\n")
	
	
	if (tooLargeFont > 0):
		font_size_comments.append("Avoid font sizes larger than 20 pt.\n")
	
	if (inconsistency > 0):
		font_size_comments.append("Dedicate the smallest font size to your bullet points. This allows you to save space.\n")
	
	
	font_size_score = (tooSmallFont + tooLargeFont + inconsistency)*-1
	
	return font_size_score, font_size_comments


def check_font_styles(font_styles):
	bad_fonts_count = 0
	bad_fonts_comments = []
	bad_fonts = []
	
	for val in font_styles.values():
		if not inn(val['font'], acceptable_fonts):
			bad_fonts_count = bad_fonts_count + 1
			bad_fonts.append(val['font'])
			bad_fonts.append(", ")
	
	
	if (bad_fonts_count > 0):
		bad_fonts_comments.append("These fonts aren't typical to a professional resumé: ")
		bad_fonts_comments = bad_fonts_comments + bad_fonts
	
	
	return (bad_fonts_count*-1), bad_fonts_comments


def inn(strn, list_elements):
	for each_element in list_elements:
		if (isSubString(strn, each_element) or isSubString(each_element, strn)) :
			return True
	
	
	return False
	


def organize_headers(tages, para):
	dict = {}
	for header in tages.values():
		dict[header] = []
	
	for each_line in para:
		for k in dict.keys():
			if isSubString(each_line, k):
				dict[k] = dict[k] + [each_line]
		
		
	return dict


def check_section_independance(organized_file, para):
	
	potential_sections = ["Skill", "Education", "Experience", "Project", "History"]
	present_sections = []
	
	for potential_section in potential_sections:
		if (len(getSection(para, potential_section)) > 0):
			present_sections.append(potential_section)

	
	score = 0
	comments = []
	count_independent_sections = 0
	non_independent_sections = []
	
	
	# Make sure education, experience and skills are in resume 
	if ("Education" not in present_sections):
		score = score - 1
		comments.append("Include an Education section. ")
	if ("Experience" not in present_sections):
		score = score - 1
		comments.append("Include an Experience section. ")
	if ("Skill" not in present_sections):
		score = score - 1
		comments.append("Include a Skills section. ")
	
	# Make sure education, experience and skills, and/or projects get their own headers at the same level
	for level in organized_file.keys():
		titles = organized_file[level]
		for each_section in present_sections:
			if (inn(each_section, organized_file[level])):
				count_independent_sections = count_independent_sections + 1
			else:
				non_independent_sections.append(each_section)
		
		if count_independent_sections > 0:
			break
		
		else:
			non_independent_sections = []

	
	if ((count_independent_sections < len(present_sections)) and (count_independent_sections > 0)):
		score = (len(non_independent_sections))*-1
		comments.append("The headers: ")
		for n in non_independent_sections:
			comments.append(n)
			comments.append(", ")
		comments.append(" should have the same category level as the headers: ")
		for d in setDifference(present_sections, non_independent_sections):
			comments.append(d)
			comments.append(", ")

	
	return score, comments
		


def setDifference(list1, list2):
	res = []
	for l in list1:
		if l not in list2:
			res.append(l)
	
	return res	
		
	



	
	
				
		