#Reading Data from the Keyboard(task01)
numbers = input("Enter numbers separated by spaces: ")
print("The numbers you entered are:",numbers)
row=int(input("Enter the number of rows: "))
collon=int(input("Enter the number of columns: "))
array = []
for i in range(row):
    row=[]
    for j in range(collon):
        value=int(input("Enter a number: "))
        row.append(value)
    array.append(row)
print("The array is:")
for row in array:
    print(row)
#Reading a String from a File(task02)
filename = input("Enter the text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        numbers_from_file = file.read().strip()

    print("Numbers in the file:", numbers_from_file)

except FileNotFoundError:
    print("File not found! Please check the filename.")
