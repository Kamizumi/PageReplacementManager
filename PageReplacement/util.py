import random

'''
Function to clean up input file because we have job before text
Gets rid of new lines and white spaces
Returns list of just the process times
'''
def cleanInput(uploadedFile):
    sanitizedInput = []
    with open(uploadedFile, "r") as file:
        lines = file.readlines()

        for line in lines:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            else:
                sanitizedInput.append(int(line))
    return sanitizedInput

'''
Reads in the test data file 
Returns it in a string for the algorithms to use
'''
def read_test_data(filename):
    all_ref_strings = []

    with open(filename, 'r') as file:
        for line in file:
            clean_line =line.strip()

            if not clean_line:
                continue
                
            all_ref_strings.append(clean_line)
    return all_ref_strings
    

'''
Function to generate random reference strings
'''
def genRefString(length):
    emptyString = ""
    for i in range(length):
        emptyString += str(random.randint(0,7))
    return emptyString

for i in range(50):
    print(genRefString(30))
