def find(a, key):
    assert type(a) == list
    for i in range(len(a)):
        assert type(key) == type(a[i])
        if a[i] == key:
            return i
    return -1


def test():
    a = [27, 82, 41, 124]
    assert find(a, 27) == 0
    assert find(a, 42) == -1
    assert find(a, 124) == 3

    empty = []
    assert find(empty, 42) == -1

    s = ["a", "b", "c", "d"]
    assert find(s, 'a') == 0
    assert find(s, 'd') == 3
    assert find(s, 'x') == -1


if __name__ == "__main__":
    test()
