#-----------------------------------------#
# Title: Home Inventory Script with Menu
# Dev: Dima Alexandrov
# Date: 10/28/2019
# Change Log: (Who, When, What)
#   DAlexandrov, 10/28/2019, Created Script
#-----------------------------------------#

# Step 1
# Display a menu of choices to the user
# ("Add Data to List", "Display Current Data", "Exit and Save to File")
lstTable = []
strUserChoice = ""
while strUserChoice != 3 and strUserChoice == "":
    print("\tMenu of Options")
    print("\t1) Add Data to List")
    print("\t2) Display Current Data")
    print("\t3) Exit and Save to File")
    strUserChoice = input("Which option would you like to perform? [1 to 3] ")

# Step 2
# Add a new item to the List(Table) each time the user makes that choice
    if strUserChoice == "1":
        print("Type in a 'Name' and Value for your household items")
        strItem = input("Enter a Name: ")
        strValue = input("Enter a Value: ")
        lstNewRow = [strItem, strValue]
        lstTable.append(lstNewRow)
        strUserChoice = "" # Get the user back to the menu

# Step 3
# Display the data in the List(Table) each time the user makes that choice

    elif strUserChoice == "2":
        print("Your Current Data is:")
        for row in lstTable:
            print(row[0], row[1], sep=",")
        strUserChoice = "" # Get the user back to the menu

# Step 4
# Exit the program and save the data to a text file when the user makes that choice
if strUserChoice == "3":
    print("Would you like to save your Data?")
    strAnswer = input("Enter 'y' or 'n': ")

    # Make sure that the user chose either the Y or N option
    while strAnswer.lower() != "y" and strAnswer.lower() != "n":
        print("Please choose either y or n")
        strAnswer = input("Enter 'y' or 'n': ")

    # If Y is chosen, save the file
    if strAnswer.lower() == "y":
            objF = open("HomeInventory.txt", "w")
            for row in lstTable:
                objF.write(row[0] + "," + row[1] + "\n")
            print("File saved!")
            objF.close()

    # If the user decides to not save, exit
    elif strAnswer.lower() == "n":
        print("Exiting...")
        exit()
