no1 = int(input("Enter the first number: "));
no2 = int(input("Enter the second number: "));
no3 = int(input("Enter the Third number: "));

def find_Biggest():
    if (no1 >= no2) and (no1 >= no2):
        largest = no1
    elif (no2 >= no1) and (no2 >= no3):
        largest = no2
    else:
        largest = no3
    print("Largest number is", largest)
find_Biggest()