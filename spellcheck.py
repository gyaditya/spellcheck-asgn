# Spell Check ADITYA
import re
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")


    for i in range(len(aliceWords)):
        aliceWords[i] = aliceWords[i].lower()


    programLoop = True

    while programLoop:
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice In Wonderland (Linear Search)")
        print("4: Spell Check Alice In Wonderland (Binary Search)")
        print("5: Exit")

        selection = input("Please enter your selection\n")

        #Slection 1
        if selection == "1":
            userInput = input("Please enter the word you want to search:\n")
            userInput = userInput.lower()
            timeStart = time.time()
            found = linearSearch(dictionary, userInput)
            if found == -1:
                endTimer = time.time()
                print(userInput + " was not found in the dictionary\n")
                print(f"Time Elapsed: {(endTimer - timeStart)}  seconds")
            else:
                print(userInput + " was found in the dictionary at position " + str(found))
                endTimer = time.time()
                print(f"Time Elapsed: {(endTimer - timeStart)}  seconds")

        

        #Selection 2
        elif selection == "2":
            userInput = input("Please enter the word you want to search:\n")
            userInput = userInput.lower()
            timeStart = time.time()
            found = binarySearch(dictionary, userInput)
            if found == -1:
                endTimer = time.time()
                print(userInput + " was not found in the dictionary\n")
                print(f"Time Elapsed: {(endTimer - timeStart)} seconds")
            else:
                endTimer = time.time()
                print(userInput + " was found in the dictionary at position " + str(found))
                print(f"Time Elapsed: {(endTimer - timeStart)}  seconds")

        
        #Selection 3
        elif selection == "3":
            count = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                found = linearSearch(dictionary, aliceWords[i])
                if found == -1:
                    count += 1
            endtimer = time.time()
            print(f"Total words not found: {(count)}")
            print(f"Time Elapsed {(endtimer - timeStart)} seconds")    
            
        #Selection 4
        elif selection == "4":
            count = 0
            timeStart = time.time()
            for i in range(len(aliceWords)):
                found = binarySearch(dictionary, aliceWords[i])
                if found == -1:
                    count += 1
            endtimer = time.time()
            print(f"Total words not found: {(count)}")
            print(f"Time Elapsed {(endtimer - timeStart)} seconds")    
        
        elif selection == "5":
            programLoop = False
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

#Linear Search
def linearSearch(anArray, item):
    for i in range (len(anArray)):
        if anArray[i] == item:
            return i
    return -1

#Binary Search
def binarySearch(anArray, item):
  lowIndex = 0
  highIndex = len(anArray) - 1

  while lowIndex <= highIndex:
    middleIndex = (lowIndex + highIndex) // 2

    if item == anArray[middleIndex]:
      return middleIndex
    elif item < anArray[middleIndex]:
      highIndex = middleIndex - 1
    else:
      lowIndex = middleIndex + 1

  return -1

# Call main() to begin program
main()
