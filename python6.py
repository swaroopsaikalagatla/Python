name=str(input("Name: "))
age=int(input("Age: "))
def old(n,a):
    year=2021+(100-a)
    return year
print(name,"You will be 100 years old in the year ",old(name,age))