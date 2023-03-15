from day_01_part_01 import read_input




def multi_fuel(fuels:list):
    result=0
    for fuel in fuels:
        fuel=(fuel//3)-2
        while fuel>0:
            result+=fuel
            fuel=(fuel//3)-2
    

    return result



fuels=read_input("input_01")
result=multi_fuel(fuels)
print("day_01_part_02 answer: ", result)



