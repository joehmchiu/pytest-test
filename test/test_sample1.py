def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
def test_uppercase2():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed2():
    assert list(reversed([1, 2, 3, 4])) == [3, 4, 2, 1]

def test_some_primes2():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
def test_uppercase3():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed3():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes3():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }

