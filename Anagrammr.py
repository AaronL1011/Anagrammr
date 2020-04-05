#Grab reference file, split each like to an array element, store as refList
listFile = open("english3.txt", "r")
refList = listFile.read().splitlines()
resultList = []
originalString = ""

def permutations(string, step = 0): #Method for finding complete permutation of input, and comparing to reference list.
    originalString = string
    #when count reaches end of length of input word, add word to resultList
    if step == len(string): 
        result = "".join(string)
        if result in refList and result not in resultList:
            resultList.append(result)

    for i in range(step, len(string)): #Method for rearranging characters in input
        # copy the string (store each character in array string_copy)
        string_copy = [c for c in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the string that has not been swapped yet
        permutations(string_copy, step + 1)
    
while True:
    userWord = input("Enter your word: ")
    if userWord.isalpha():
        break
    else:
        print("Enter a valid string.")
permutations(userWord)
if len(resultList) <= 1 and resultList[0] == userWord:
    resultList.pop(0)
    resultList.append("There were no anagrams in the reference list")
else:
    print(resultList)





#Take user input
#Split input and rearrange
#compare new word to entire array 'if X in refList'
#if yes return matched word, continue rearrange and compare
#stop once max number of iterations is hit.