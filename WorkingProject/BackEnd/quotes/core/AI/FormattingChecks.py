from . ParseHelpers import *

acceptable_fonts = ['Calibri', 'Times New Roman', 'Cambria', 'Garamond', 'Georgia', 'Helvetica', 'Arial', 'Verdana']

def formatting_checks(font_counts, font_styles, tages, para):
	print (font_counts)
	print("\n\n")
	print(font_styles)
	print(tages)
	print(para)
	font_size_score, font_size_comments = check_font_sizes(font_counts)
	score = font_size_score
	comments = font_size_comments  # you can add comments by comments.append("......")
	
	font_style_score, font_style_comments = check_font_styles(font_styles)
	
	score = score + font_style_score
	comments = comments + font_style_comments
	
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
		if isSubString(strn, each_element):
			return True
	
	
	return False
			
		