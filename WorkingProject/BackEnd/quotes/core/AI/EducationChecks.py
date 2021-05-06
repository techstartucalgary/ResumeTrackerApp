from . ParseHelpers import *
import re
#important change: importing the regex library
# Somethings to check for:
# Applicant has a Bachelor or Master's degree in CS, SENG or Electrical Eng or Comp Eng
# Applicant's GPA > 3.5, or not written at all


def education_checks(block_of_text):
    # print(block_of_text)        # To help you view what the argument looks like
    # print("\n")
    score = 100
    comments = []

    if (isSubString(block_of_text, "Computer Science")):
        score += 10

    elif (isSubString(block_of_text, "CS")):
        score += 10

    elif (isSubString(block_of_text, "Software Engineering")):
        score += 10

    elif (isSubString(block_of_text, "Electrical Engineering")):
        score += 10

    elif (isSubString(block_of_text, "Computer Engineering")):
        score += 10

    else:
        score = -10
        comments.append("In today's job market, a degree in CS or Engineering is expected.")

    # TO-DO: Check GPA

    #removes all special characters except periods, converts to uppercase and the string to a list split by spaces. The instance called "tracker" is to iterate through said list
    regex = re.sub('[^a-zA-Z0-9.]+', ' ', block_of_text)
    subBlocks = regex.upper().split()
    print(subBlocks)
    tracker = 0
    gpaStatus = False
    #checks all words in the block of text, and looks for the letters "GPA"
    for word in subBlocks:
        #if GPA is found, checks the next 10 words. If a number is detected and it is less than 4.00, it is considered to be the GPA. The number of next words it checks can be altered
        if "GPA" in word:
            print("true")
            index = tracker

            while index < index + 9 and index < len(subBlocks):

                # print(subBlocks[index])

                # goes through each word. attempts to convert it to a number. if it can, it checks to see if the number is within an acceptable GPA range. This
                # is to ensure that
                # a) if the user supplies a year before the number, it will most likely not be detected. HOWEVER, if the user puts the year as " '05 "
                # will screw up the system. HOWEVER, this is unlikely to happen, and the only way i can see that this can be fixed is that if there is some library
                # that exists which can detect GPA, or an actual AI trained to detect GPAs
                # b) there is no b)
                try:
                    if 4.0 > float(subBlocks[index]) >= 3.5:
                        score = score + 10
                        comments.append("Your GPA: " + str(float(subBlocks[index])) + " is high. Great job!.")
                        gpaStatus = True
                        break

                    elif float(subBlocks[index]) < 3.5:
                        score = score - 10
                        comments.append("Your GPA: " + str(float(subBlocks[index])) + " is somewhat low. It is recommended that you only include a GPA of 3.5 or higher!.")
                        gpaStatus = True
                        break
                except ValueError:
                    pass
                finally:
                    index = index + 1


        tracker = tracker + 1
    if gpaStatus == False:
        comments.append("No GPA detected. It is not necessary to include a GPA, though it may help.")
    print(tracker)

    return score, comments
