from day_02_part_01 import read_input, gravity_assist


def find(output: int , numbers:list):
    
    check=False
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            check_numbers=numbers.copy()
            check_numbers[1]=i
            check_numbers[2]=j
            result=gravity_assist(check_numbers)
            if output==result[0]:
                check=True
                break
        
        if check:
            break
    
    if check:
        return 100*check_numbers[1]+check_numbers[2]
    
    else:
        raise TypeError("Not found!")


            




numbers=read_input("input_02")
result_2=find(19690720 , numbers)
print("answer day_02_part_02: " , result_2)





