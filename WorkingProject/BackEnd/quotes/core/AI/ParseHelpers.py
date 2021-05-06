
def getSection(para, sectionName):
	block = ""
	begin_copy = False
	delimiter = ""
	for each_line in para:
		if (begin_copy == False):
			if (isSubString(each_line, sectionName) == False):
				continue
			else:
				w = each_line.split(">")
				delimiter = w[0]
				if not(isSubString(delimiter, "<s") or isSubString(delimiter, "<p")):
					begin_copy = True
					block = block + each_line
		
		else:
			if (isSubString(each_line, delimiter) == True):
				break
			else:
				block = block + each_line
	
	return block
			
		
def isSubString(word1, word2):
	i = 0
	j = 0
	
	while i < len(word1) and j < len(word2):
		if word1.lower()[i] == word2.lower()[j]:
			j = j + 1
		else:
			j = 0
			
		i = i + 1
	
	if j == len(word2):
		return True
	else:
		return False

def inn(strn, list_elements):
	for each_element in list_elements:
		if (isSubString(strn, each_element) or isSubString(each_element, strn)) :
			return True
	
	
	return False


def innCount(strn, list_elements):
	count = 0
	for each_element in list_elements:
		if (isSubString(strn, each_element) or isSubString(each_element, strn)):
			count = count + 1
	
	return count