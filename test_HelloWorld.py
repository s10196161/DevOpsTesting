import pytest
from HelloWorld import *

def test_HelloWorld_NoInput():
    result = HelloWorld()
    assert result == "Hello World!"

@pytest.mark.parametrize("name, expectedResult",
[("Danny", "Hello Danny!"),("Caleb","Hello Caleb!"),
("Eugene","Hello Eugene!")])

def test_HelloWorld_UserInput(name, expectedResult):
    result = HelloWorld(name)
    assert result == expectedResult

