
def getSection(para, sectionName):
	block = ""
	begin_copy = False
	delimiter = ""
	for each_line in para:
		if (begin_copy == False):
			if (isSubString(each_line, sectionName) == False):
				continue
			else:
				begin_copy = True
				block = block + each_line
				w = each_line.split(">")
				delimiter = w[0]
		
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
	