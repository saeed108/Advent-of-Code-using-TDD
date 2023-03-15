import os
def read_input(file_path):
    address="{}.txt".format(file_path)
    if os.path.exists(address):
        file=open(address , "r")
        txt=file.read()
        file.close()
        x=txt.split(",")
        numbers=[]
        if "" in x:
            x.remove("")
        for item in x:
            numbers.append(int(item))
        
        return numbers
    
    else:
        raise TypeError("File not found!")


def gravity_assist(numbers:list):
    for i in range(0, len(numbers) , 4):
        if numbers[i]==99:
            break

        elif numbers[i]==1:
            position1=numbers[i+1]
            position2=numbers[i+2]
            position3=numbers[i+3]
            numbers[position3]=numbers[position1]+numbers[position2]
        
        else :
            position1=numbers[i+1]
            position2=numbers[i+2]
            position3=numbers[i+3]
            numbers[position3]=numbers[position1]*numbers[position2]
    
    return numbers


numbers=read_input("input_02")
numbers[1]=12
numbers[2]=2

result=gravity_assist(numbers)
print("answer day_02_part_01: ", result[0])
