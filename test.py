from ex12_utils import *


def test_is_valid_path():
    words1 = ["hello", "world", "queen", "ron", "alon", "time", "boggle", "list"]
    words_cord_dict = {"hello": [(0, 0), (0, 1), (0, 2), (1, 2), (0, 3)], "queen": [(2, 0), (1, 0), (1, 1), (2, 2)]}
    brd = [
        ["h", "e", "qu", "e"],
        ["e", "e", "t", "a"],
        ["l", "l", "n", "o"],
        ["o", "t", "x", "l"]
    ]
    assert is_valid_path(brd, words_cord_dict["hello"], words1) == "hello"
    assert is_valid_path(brd, words_cord_dict["queen"], words1) == "queen"
    assert is_valid_path(brd, [(-1, 3)], words1) is None
    assert is_valid_path(brd, [(5, 3)], words1) is None
    assert is_valid_path(brd, [(3, 3), (4, 3)], words1) is None


def test_find_length_n_paths_empty_board():
    brd = []
    assert find_length_n_paths(1, brd, ["a"]) == []
    assert find_length_n_paths(0, brd, ["a"]) == []
    assert find_length_n_paths(0, brd, []) == []
    brd = [[]]
    assert find_length_n_paths(1, brd, ["a"]) == []
    brd = [[], []]
    assert find_length_n_paths(1, brd, ["a"]) == []
    assert find_length_n_paths(0, brd, ["a"]) == []
    assert find_length_n_paths(0, brd, []) == []


def test_find_length_n_paths_one_item():
    brd = [["a"]]
    assert find_length_n_paths(1, brd, ["a"]) == [[(0, 0)]]
    # empty output:
    assert find_length_n_paths(1, brd, ["b"]) == []
    assert find_length_n_paths(2, brd, ["a"]) == []
    assert find_length_n_paths(2, brd, ["b"]) == []
    assert find_length_n_paths(1, brd, ["aa"]) == []
    assert find_length_n_paths(1, brd, []) == []
    assert find_length_n_paths(0, brd, [""]) == []  # TODO : Check if this test is legit


def test_find_length_n_paths_two_items():
    brd = [["a", "b"]]
    # valid output:
    assert find_length_n_paths(1, brd, ["a"]) == [[(0, 0)]]
    assert find_length_n_paths(1, brd, ["b"]) == [[(1, 0)]]
    assert find_length_n_paths(1, brd, ["a", "b"]) == [[(0, 0)], [(1, 0)]]
    assert find_length_n_paths(1, brd, ["a", "b", "bb"]) == [[(0, 0)], [(1, 0)]]
    assert find_length_n_paths(2, brd, ["ab"]) == [[(0, 0), (1, 0)]]
    assert find_length_n_paths(2, brd, ["ba"]) == [[(1, 0), (0, 0)]]
    # empty output:
    assert find_length_n_paths(1, brd, ["c"]) == []
    assert find_length_n_paths(2, brd, ["bc"]) == []
    assert find_length_n_paths(3, brd, ["ab"]) == []


def test_find_length_n_paths_2x2():
    brd = [["a", "b"], ["c", "d"]]
    # n = 2:
    assert find_length_n_paths(2, brd, ["ab", "ba", "bc", "da"]) == [[(0, 0), (1, 0)], [(1, 0), (0, 0)],
                                                                     [(1, 0), (0, 1)], [(1, 1), (0, 0)]]
    # n = 3
    assert find_length_n_paths(3, brd, ["abc", "dac", "bc", "da"]) == [[(0, 0), (1, 0), (0, 1)],
                                                                       [(1, 1), (0, 0), (0, 1)]]
    brd = [["a", "a"],
           ["a", "a"]]
    assert len(find_length_n_paths(1, brd, "a")) == 4
    assert len(find_length_n_paths(2, brd, ["aa"])) == 12
    # assert len(find_length_n_paths(3, brd, ["aaa"])) == 24


def test_find_length_n_paths():
    test_find_length_n_paths_empty_board()
    test_find_length_n_paths_one_item()
    test_find_length_n_paths_two_items()
