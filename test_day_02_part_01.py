from day_02_part_01 import read_input,  gravity_assist
import pytest



def test_12():
    
    assert read_input("test_input_02")==[1,9,10,3,2,3,11,0,99,30,40,50]


def test_13():
    result=gravity_assist([1,0,0,0,99])
    assert result[0]==2


def test_14():
    result=gravity_assist([2,3,0,3, 99])
    assert result[3]==6


def test_15():
    result=gravity_assist([2 , 4 , 4 , 5, 99 , 0])
    assert result[5]==9801


def test_16():
    result=gravity_assist([1,1,1,4,99,5,6,0,99])
    assert result[0]==30 and result[4]==2


def test_17():
    numbers=read_input("test_input_02")
    result=gravity_assist(numbers)
    assert result[0]==3500 and result[3]==70


if __name__=="__main__":
    pytest.main(['-vv'])
