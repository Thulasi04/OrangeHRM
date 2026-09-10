import pytest


@pytest.fixture
def numbers():
    return 2

def test_print_numbers(numbers):
    print(numbers)