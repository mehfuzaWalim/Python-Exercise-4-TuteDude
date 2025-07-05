#program to open and read a sample file "sample.txt" line by line and displays its content. 
#It also handles errors if file does not exist.

try:
	file= open("sample.txt","r")
	file_reader= file.readlines()
	line_number = 1;
	print("Reading File Content: ")
	for i in file_reader:
		print("Line ", line_number ,": ", i)
		line_number+=1
	file.close()
except FileNotFoundError:
	print("Error: The file \"Sample.txt\" was not found")
	


