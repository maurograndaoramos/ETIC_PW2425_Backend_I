import pytest 

def sum(a:int, b:int)-> int:
    return a+b

@pytest.mark.parametrize(
   argnames="a,b,result",  
   argvalues=[
       (x,x,x*2)
       for x in range(10)
   ]   
)
def test_cenas(a,b,result):
    assert sum(a,b) is result

def two():
    assert 1 == 1


