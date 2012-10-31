#This program will take a first name, last name, and domain to create several popular email combinations

#Function that will build the text file with email combinations
def build_list():
	#Initial variables that will be broken down
	first_name = raw_input('What is the person\'s first name? ')
	last_name = raw_input('What is the person\'s last name? ')
	domain = raw_input('What is the domain of their workplace? ')

	#Manipulated variables from above to affix to new strings
	proper_domain = "@" + domain
	first_letterfn = first_name[0]
	firsttwo_letterfn = first_name[0] + first_name[1]

	#Opening the new text document
	f = open("emaillist.txt", "w")
	f.write("See below for the list of email addresses built:")
	f.write("\n")
	f.write("\n")
	
	#List of writes to the document
	f.write(first_letterfn + last_name + proper_domain)
	f.write("\n")
	f.write(firsttwo_letterfn + last_name + proper_domain)
	f.write("\n")
	f.write(last_name + first_letterfn + proper_domain)
	f.write("\n")
	f.write(first_letterfn + "." + last_name + proper_domain)
	f.write("\n")
	f.write(first_name + last_name + proper_domain)
	f.write("\n")
	f.write(first_name + "." + last_name + proper_domain)

	#Closing the document
	f.close()

#Running the function
print """
****************************************************
This little script will take a few inputs from you
and build a little list of potential email addresses 
for you to contact. Please don't add spaces beside
your inputs! @Bvlaar
****************************************************
"""

build_list()


