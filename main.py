def countWords ():
    file_name = input("Enter the name of the file: ")
    count = 0
    file1 = open(file_name, "r")

    for lines in file1:
        words = lines.split()
        count = count + len(words)

    print("The number of words are:", count)

countWords()