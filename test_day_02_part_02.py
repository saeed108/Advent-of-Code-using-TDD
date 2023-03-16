from  day_02_part_02 import find
from day_02_part_01 import gravity_assist , read_input
import pytest


numbers=read_input("input_02")


def test_18():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=1
    numbers_calculate[2]=2
    result=gravity_assist(numbers_calculate)

    
    assert find(result[0] , numbers)==102

def test_19():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=2
    numbers_calculate[2]=1
    result=gravity_assist(numbers_calculate)

    assert find(result[0] , numbers)==201


def test_20():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=2
    numbers_calculate[2]=12
    result=gravity_assist(numbers_calculate)
    assert find(result[0] , numbers)==212


def test_21():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=12
    numbers_calculate[2]=2
    result=gravity_assist(numbers_calculate)
    assert find(result[0] , numbers)==1202


def test_22():
    global numbers
    numbers_calculate=numbers.copy()
    numbers_calculate[1]=14
    numbers_calculate[2]=14
    result=gravity_assist(numbers_calculate)
    assert find(result[0] , numbers)==1414
















if __name__=="__main__":
    pytest.main(["-vv"])
