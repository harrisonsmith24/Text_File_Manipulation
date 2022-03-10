# Harrison Smith
# CPT 187 Chapter 9 Exam
# Professor Carman
# This program is designed to allow the user to create a list of products that have a corresponding number and save
# that information to a text file. The user can change the products, add or delete products, search for products in the
# directory, and display the full directory of products. The data will save everytime the program ends.

# importing the pickle attachment
import pickle


# Defining the main function
def main():
    # Saving a Bool for the while loop
    proceed = True
    # Creating an empty directory
    emails = {}

    # Opening the file with the dictionary of products
    input_file = open('productList.txt', 'rb')
    # Will try to open the file if one exist with information in it
    try:
        # Setting the information from the file into a dictionary
        products = pickle.load(input_file)
    # Error to operate the dictionary as empty if there is no information in the file
    except:
        products = {}

    # Closing the file
    input_file.close()

    # While loop to continue to prompt the user in the menu
    while proceed == True:

        # Calls the display menu function
        displayMenu()

        # Prompting the user to enter a command
        selection = input("Enter command here:")

        # Depending on the command this if statement will call the following function.
        if selection == "1":
            displayProducts(products)
        if selection == "2":
            lookUp(products)
        if selection == "3":
            addNewProduct(products)
        if selection == "4":
            changeProduct(products)
        if selection == "5":
            deleteProduct(products)

        # Asking the user if they would like to continue
        repeat = input("Would you like to continue? (y/n):")

        # Setting the bool depending on the user's response
        if repeat == "y" or repeat == "Y":
            proceed = True
        else:
            proceed = False

    # Pickleing the dictionary to the text file
    output_file = open('productList.txt', 'wb')
    pickle.dump(products, output_file)
    output_file.close()


# Defining the displayMenu function
def displayMenu():

    # Printing the menu
    print("Welcome to the product lookup directory!")
    print('')
    print("To display the list of products press '1'")
    print("To look up a product press '2'")
    print("To add a new product and number to the directory press '3'")
    print("To change a current product or product number press '4'")
    print("To delete a current product press '5'")


# Defining the displayProducts function
def displayProducts(dictionary):

    # For loop to loop through each of the keys in the dictionary
    for key in dictionary:
        # print the key and value
        print(key, dictionary[key])


# Defining the lookUp function
def lookUp(dictionary):
    # Asking the user for the name of the product to find
    number = input("What is the number of the product?:")

    # if statement to check if the number of the product used is actually in the directory
    if number in dictionary:
        # printing the info of the product
        print(number, dictionary[number])
    # Telling the user that the product doesnt exist if the name is not found
    else:
        print("Product does not exist.")


# Defining the addNewProduct function
def addNewProduct(dictionary):
    # Asking the user for the number and product name they would like to add
    number = input("What is the number of the new product?:")
    productName = input("What is the name of the new product?:")

    # Adding the product to the directory
    dictionary[number] = productName
    # Showing the user that the product was in fact added
    displayProducts(dictionary)

    # Printing out a confirmation
    print('')
    print(productName, "Was added to the directory!")


# Defining the changeProduct function
def changeProduct(dictionary):
    # Asking the user for the name of the current product
    number = input("What is the number of the current product?:")

    # if statement to check if the product is in the dictionary
    if number in dictionary:
        # Telling the user the number was found
        print("Product", number, "was found in the directory.")
        # Asking the user for the new name
        name = input("What is the new product name?:")
        # Saving the new name to the product
        dictionary[number] = name
    # Print a statement if the number is not found in the directory
    else:
        print("That product was not found in the dictionary")


# Defining the deleteProduct function
def deleteProduct(dictionary):

    # Asking the user what is the name of the current product they want to delete
    number = input("What is the number of the product you are choosing to delete?:")

    # if statement to check if the product is in the directory
    if number in dictionary:
        # Delete the product
        del dictionary[number]
        # print a confirmation for the user
        print("Product", number, "Was found in the directory and was deleted.")
    # Print statement if the product is not found.
    else:
        print("That product was not found in the dictionary")


# Call the main function
main()

