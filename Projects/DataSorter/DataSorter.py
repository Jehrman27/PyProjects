# DataSorter
# this program will accept ten numbers through the console or the first ten lines of a file
# then output them in order on separate lines.

# declarations
dataList = []
dataSource = "console"
needPrompt = 'y'
userInput = 'n'


# ask user to input source of data
while needPrompt == 'y':
    userInput = input('Would you like to load the numbers from a file? ')
    try:
        # continue to prompt user until a valid input is received
        if userInput.lower() == 'yes' or userInput.lower() == 'y':
            dataSource = 'file'
            needPrompt = 'n'
        elif userInput.lower() == 'no' or userInput.lower() == 'n':
            dataSource = 'console'
            needPrompt = 'n'
        else:
            print('Invalid entry.')
    except:
        print('Invalid entry.')


if dataSource == 'file':
    # get file name to open
    x = 1
    while x == 1:
        fileName = input('Please enter the file name, including extension (leave blank to quit): ')
        try:
            # attempt to open file specified or quit if field left blank
            if fileName == "":
                quit()
            else:
                f = open(fileName)
                x = 0
        except:
            # tell user file could not be opened and show what they entered
            print(f'{fileName} could not be opened')
    # read the contents of the file to a variable
    fcontents = f.readlines()
    # insert the first ten lines into a list, convert to int type, and trim the carriage return
    for i in range(10):
        dataList.append(int(fcontents[i][:-1]))
    f.close()
elif dataSource == 'console':
    for i in range(10):
        # append entered number to list and convert to int type
        dataList.append(int(input(f'Please enter number {i+1}: ')))
else:
    print('Something went wrong. Please try again.')
    
# sort the list
dataList.sort()

# print the sorted numbers on separate lines
for i in range(10):
    print(dataList[i])

    
