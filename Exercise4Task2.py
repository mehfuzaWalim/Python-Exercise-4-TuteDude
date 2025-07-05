#program that asks user for some data, write data to the file named "output.txt". 
#It aslo appends additional data and displays content of the file.

try:
	file= open("output.txt","w")
	data = input("Please enter text to be written to the file: ")
	file.write(data)
	print("Data successfully written to \"output.txt\".")	
	file.close()
	
	file= open("output.txt","a")
	data = input("Please enter additional text to append to the file: ")
	file.write("\n")
	file.write(data)
	print("Data successfully appended.")	
	file.close()

	print("\n")
	file = open("output.txt", "r")	
	file_reader = file.read()
	print("Final content of \"output.txt\":")
	print(file_reader)
	file.close()
except FileNotFoundError:
	print("Error: The file \"Sample.txt\" was not found")
	


