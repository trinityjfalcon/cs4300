# Write a program inside task6.py of that reads task6_read_me.txt and counts the number
# of words in it

try:
    with open('/home/student/cs4300/homework1/task6_read_me.txt', 'r') as file:
        # Reads file into string
        content = file.read()

        # Split content by white space
        wordList = content.split()

        # Removing commas and periods
        commaRemove = ","
        periodRemove = "."

        while commaRemove in wordList:
            wordList.remove(commaRemove)

        while periodRemove in wordList:
            wordList.remove(periodRemove)

        # Count words
        wordCount = 0
        for i in wordList:
            wordCount += 1
        print(wordCount)

except FileNotFoundError:
    print("File could not be found")
except Exception as e:
    print(f"Error: {e}")