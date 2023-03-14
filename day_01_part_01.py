import os
def read_input(address):
    address=address+".txt"
    if os.path.exists(address):
        file=open(address , "r")
        
        
        lines=file.readlines()
        file.close()
        
        fuels=[]
        for item in lines:
            
            if item!="":
                fuels.append(int(item))
        
        return fuels
    
    else:
        raise TypeError("File not found!")


def sum_fuels(mass_list: list):
    sum=0
    for item in mass_list:
        sum+=(item//3)-2
    
    return sum



fuels=read_input("input_01")

result=sum_fuels(fuels)
print(result)
