listFile = open("english3.txt", "r")
refList = listFile.read().splitlines()
resultList = []

def permutations(string, step = 0):
    if step == len(string):
        # we've gotten to the end, print the permutation
        result = "".join(string)
        if result in refList and result not in resultList:
            resultList.append(result)

    for i in range(step, len(string)):
        # copy the string (store as array)
        string_copy = [c for c in string]
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        # recurse on the portion of the string that has not been swapped yet
        permutations(string_copy, step + 1)

userWord = input("Enter your word: ")
permutations(userWord)
print(resultList)



#Take user input
#Split input and rearrange
#compare new word to entire array 'if X in refList'
#if yes return matched word, continue rearrange and compare
#stop once max number of iterations is hit.