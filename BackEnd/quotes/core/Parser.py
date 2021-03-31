# This is where our backend program is implemented.


import PyPDF2

class Education:
	allDegrees = []
	
	def __repr__(self):
		res = ""
		for degree in self.allDegrees:
			res = res + repr(degree)
		return res


class Degree:
	focus1 = ""
	focus2 = ""
	gpa = ""
	degreeType = ""
	institution = ""
	gpa = 0.0
	
	def __repr__(self):
		res = ""
		res = res + self.degreeType + " at " + self.institution 
		return res


def getBounds(buffer, sublist):
	i = 0
	j = 0
	while ((i < len(buffer)) and (j < len(sublist))):
		if (buffer[i] != sublist[j]):
			j = 0
		i = i + 1
		j = j + 1
	if (j == len(sublist)):
		return i-len(sublist), i
	else:
		return -1, -1


def getBlockBounds(startDelimiters, endDelimiters, buffer):
	startIndex = -1
	endIndex = -1
	
	startIndexP = -1
	endIndexP = -1
	
	for word in startDelimiters:
		startIndex, endIndex = getBounds(buffer, word)
		if ((startIndex != -1) and (endIndex != -1)):
			break;
	
	if ((startIndex == -1) or (endIndex == -1)):
			return -1, -1
	
	for word in endDelimiters:
		i, j = getBounds(buffer, word)
		if (((i != -1) and (j != -1)) and (i >= endIndex)) :
			if ((startIndexP == -1) and (endIndexP == -1)):
				startIndexP = i
				endIndexP = j
			elif ((i < startIndexP) and (j < endIndexP)):
				startIndexP = i
				endIndexP = j
	
	if ((startIndexP == -1) or (endIndexP == -1)):
		return -1, -1
	
	elif (startIndexP < endIndex):
		return -1, -1
	
	else:
		return endIndex, startIndexP
			


def max(a, b):
	if (a > b):
		return a
	else:
		return b

def getEducation(extractedText):
	startDelimiters = ["Education"]
	endDelimiters = ["Experience", "Work", "Employment", "Skills"]
	lowerBound, upperBound = getBlockBounds(startDelimiters, endDelimiters, extractedText)
	
	buffer = extractedText[lowerBound:upperBound]
	schoolNames = []
	degreeNames = []

	
	while (len(buffer) > 0):
		a, b = getBounds(buffer, "University of")
		
		if ((a == -1) or (b == -1)):
			break 
		
		i = a
		strn = ""
		while ((i < len(buffer)) and (i != -1)):
			if not ((ord(buffer[i]) >= 65 and ord(buffer[i]) <= 90) or (ord(buffer[i]) >= 97 and ord(buffer[i]) <= 122)):
				if ((len(strn) > 0) and not ((ord(strn[len(strn)-1]) >= 65 and ord(strn[len(strn)-1]) <= 90) or (ord(strn[len(strn)-1]) >= 97 and ord(strn[len(strn)-1]) <= 122))):
					schoolNames.append(strn)
					break

			strn = strn + buffer[i]
			i = i + 1
		
		buffer = buffer[b:upperBound]
	
	buffer = extractedText[lowerBound:upperBound]
	while (len(buffer) > 0):
		c, d = getBounds(buffer, "Bachelor of")
		if ((c == -1) or (d == -1)):
			break 
		i = c
		strn = ""
		while ((i < len(buffer)) and (i != -1)):
			if not ((ord(buffer[i]) >= 65 and ord(buffer[i]) <= 90) or (ord(buffer[i]) >= 97 and ord(buffer[i]) <= 122)):
				if ((len(strn) > 0) and not ((ord(strn[len(strn)-1]) >= 65 and ord(strn[len(strn)-1]) <= 90) or (ord(strn[len(strn)-1]) >= 97 and ord(strn[len(strn)-1]) <= 122))):
					degreeNames.append(strn)
					break

			strn = strn + buffer[i]
			i = i + 1
		
		
		i = 0
		
		buffer = buffer[d:upperBound]
	
	
	degrees = []
	i = 0
	while (i < len(degreeNames)):
		degrees.append(Degree())
		degrees[i].degreeType = degreeNames[i]
		degrees[i].institution = schoolNames[0]
		if (len(schoolNames) > 1):
			schoolNames = schoolNames[1:]
		
		i = i + 1	
	
	e = Education()
	e.allDegrees = degrees	
	return e


class Result:
	
	dict = {}
	
	def __init__ (self):
		self.dict = {'totalScore': '0', 'educationScore': '0', 'educationComments': 'You are dumb.',
        'experienceScore': '0', 'experienceComments': 'You are inexperienced' , 'formattingScore': '0', 
        'formattingComments': 'Terrible Formatting.', 'name': 'NoName', 'detail': 'N.A.'}
	
	

	
# This method will parse the file			
def compute(pdfReader):
	#pageObj = pdfReader.getPage(0)
	#text = pageObj.extractText()
	#education = getEducation(text)
	#print(education)
	dummyResult = Result()
	return dummyResult.dict

