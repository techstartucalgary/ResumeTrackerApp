from . ParseHelpers import *

weak_verbs = ["handle", "work", "assist", "help"]

strong_verbs = ["achieve", "create", "develop", 
					"establish", "ideas", "improve", 
								"increase", "decrease", "influence",
								"launch", "manage", "negotiate", "resolve", "revenue", "profit", 
								"train", "mentor", "volunteer", "budget"]





# Return number of weak and strong verbs for any type of resume
def general_words_check(lines):
	num_weak_verbs = 0
	num_strong_verbs = 0
	for each_line in lines:
		words = each_line.split()
		for each_word in words:
			for weak_verb in weak_verbs:
				if (isSubString(each_word, weak_verb) == True):
					num_weak_verbs = num_weak_verbs + 1
					print(each_word)
			
			for strong_verb in strong_verbs:
				if (isSubString(each_word, strong_verb) == True):
					num_strong_verbs = num_strong_verbs + 1
					print(each_word)

	return num_weak_verbs, num_strong_verbs




