from ex12_utils import *
import tests_helper as ts


def test_is_valid_path():
    words1 = ["hello", "world", "queen", "ron", "alon", "time", "boggle", "list"]
    words_cord_dict = {"hello": [(0, 0), (1, 0), (2, 0), (2, 1), (3, 0)], "queen": [(0, 2), (0, 1), (1, 1), (2, 2)],
                       'alon': [(1, 3), (1, 2), (2, 3), (2, 2)], 'ron': [(3, 2), (2, 3), (2, 2)]}
    brd = [
        ["h", "e", "qu", "e"],
        ["e", "e", "t", "a"],
        ["l", "l", "n", "o"],
        ["o", "t", "x", "l"]
    ]
    assert is_valid_path(brd, words_cord_dict["hello"], words1) == "hello"
    assert is_valid_path(brd, words_cord_dict["queen"], words1) == "queen"

    # checks if the path is out of range of the board
    assert is_valid_path(brd, [(-1, 3)], words1) is None
    assert is_valid_path(brd, [(5, 3)], words1) is None
    assert is_valid_path(brd, [(3, 3), (4, 3)], words1) is None

    brd = [
        ["h", "e", "qu", "e"],
        ["e", "e", "l", "a"],
        ["l", "l", "n", "o"],
        ["o", "t", "r", "l"]
    ]
    assert is_valid_path(brd, words_cord_dict["alon"], words1) == "alon"
    assert is_valid_path(brd, words_cord_dict["ron"], words1) == "ron"

    # checks if the path is legal but word not in words.
    assert is_valid_path(brd, [(1, 3), (2, 3), (3, 3), (2, 2)], words1) is None
    assert is_valid_path(brd, [(0, 2), (0, 1), (1, 1), (1, 0)], words1) is None
    # path in length 1
    assert is_valid_path(brd, [(0, 2)], words1) is None
    assert is_valid_path(brd, [(1, 0)], words1) is None
    assert is_valid_path(brd, [(1, 1)], words1) is None
    # path in length 2
    assert is_valid_path(brd, [(1, 3), (2, 3)], words1) is None
    assert is_valid_path(brd, [(3, 3), (2, 2)], words1) is None
    assert is_valid_path(brd, [(1, 3), (2, 2)], words1) is None
    # empty path
    assert is_valid_path(brd, [], words1) is None
    # a very long path
    assert is_valid_path(brd, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2),
                               (2, 3), (3, 3), (3, 2), (3, 1), (3, 0)], words1) is None
    # word that in words but the move is not legal
    assert is_valid_path(brd, [(0, 2), (1, 0), (1, 1), (2, 2)], words1) is None
    assert is_valid_path(brd, [(0, 0), (0, 3), (1, 2), (2, 1), (3, 0)], words1) is None
    assert is_valid_path(brd, [(0, 0), (0, 3), (2, 0), (2, 1), (3, 0)], words1) is None


def test_find_length_n_paths_2_len_char():
    brd = [
        ["h", "e", "qu", "e"],
        ["e", "e", "t", "a"],
        ["l", "l", "n", "o"],
        ["o", "t", "x", "l"]
    ]
    assert ts.compare_lists(find_length_n_paths(3, brd, ['quee', 'a', 'que']),
                            [[(0, 2), (0, 1), (1, 1)], [(0, 2), (0, 1), (1, 0)], [(0, 2), (1, 1), (0, 1)],
                             [(0, 2), (1, 1), (1, 0)]])
    assert ts.compare_lists(find_length_n_paths(5, brd, ['eaolx', 'eaolo']), [[(0, 3), (1, 3), (2, 3), (3, 3), (3, 2)]])
    assert ts.compare_lists(find_length_n_paths(4, brd, ['quanl', 'queta', 'eaolx', 'eaolo', 'hee']),
                            [[(0, 2), (1, 3), (2, 2), (3, 3)], [(0, 2), (1, 3), (2, 2), (2, 1)],
                             [(0, 2), (0, 3), (1, 2), (1, 3)], [(0, 2), (0, 1), (1, 2), (1, 3)],
                             [(0, 2), (1, 1), (1, 2), (1, 3)]])


def test_find_length_n_paths_1x1():
    brd = [['a']]
    assert find_length_n_paths(2, brd, ['a']) == []
    assert find_length_n_paths(1, brd, ['a', 'asd', 'cvxz']) == [[(0, 0)]]
    assert find_length_n_paths(1, brd, ['a']) == [[(0, 0)]]
    assert find_length_n_paths(1, brd, ['b']) == []
    assert find_length_n_paths(0, brd, ['a']) == []
    assert find_length_n_paths(-1, brd, ['a']) == []
    brd = [['bc']]
    assert find_length_n_paths(1, brd, ['bc']) == [[(0, 0)]]
    assert find_length_n_paths(1, brd, ['a']) == []
    brd = [['bc', 'a', 'b', 'c']]
    assert find_length_n_paths(1, brd, ['bc']) == [[(0, 0)]]
    assert find_length_n_paths(2, brd, ['bc']) == [[(0, 2), (0, 3)]]


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


def test_find_length_n_paths_long_char():
    brd = [
        ["h", "aaaaa", "qu", "e"],
        ["e", "e", "t", "abc"],
        ["l", "l", "abcde", "o"],
        ["o", "t", "x", "abcd"]
    ]
    assert ts.compare_lists(find_length_n_paths(1, brd, ['aaaaa', 'eaolo']), [[(0, 1)]])
    assert ts.compare_lists(find_length_n_paths(2, brd, ['aaaaaqu', 'eaolo']), [[(0, 1), (0, 2)]])
    assert ts.compare_lists(find_length_n_paths(3, brd, ['aaaaaquabc', 'eaolo']), [[(0, 1), (0, 2), (1, 3)]])
    assert ts.compare_lists(find_length_n_paths(2, brd, ['aaaaaquabc', 'eaolo']), [])
    assert ts.compare_lists(find_length_n_paths(10, brd, ['aaaaaquabc', 'eaolo']), [])
    assert ts.compare_lists(find_length_n_paths(1, brd, ['abcd', 'abcde']), [[(3, 3)], [(2, 2)]])


def test_find_length_n_paths():
    test_find_length_n_paths_2_len_char()
    test_find_length_n_paths_1x1()
    test_find_length_n_paths_empty_board()


def test_find_length_n_words_empty_board():
    brd = []
    assert find_length_n_words(1, brd, ["a"]) == []
    assert find_length_n_words(0, brd, ["a"]) == []
    assert find_length_n_words(0, brd, []) == []
    brd = [[]]
    assert find_length_n_words(1, brd, ["a"]) == []
    brd = [[], []]
    assert find_length_n_words(1, brd, ["a"]) == []
    assert find_length_n_words(0, brd, ["a"]) == []
    assert find_length_n_words(0, brd, []) == []


def test_find_length_n_words_one_item():
    brd = [["a"]]
    assert find_length_n_words(1, brd, ["a"]) == [[(0, 0)]]
    # empty output:
    assert find_length_n_words(1, brd, ["b"]) == []
    assert find_length_n_words(2, brd, ["a"]) == []
    assert find_length_n_words(2, brd, ["b"]) == []
    assert find_length_n_words(1, brd, ["aa"]) == []
    assert find_length_n_words(1, brd, []) == []
    assert find_length_n_words(0, brd, [""]) == []  # TODO : Check if this test is legit


def test_find_length_n_words_two_items():
    brd = [["a", "b"]]
    # valid output:
    assert find_length_n_words(1, brd, ["a"]) == [[(0, 0)]]
    assert find_length_n_words(1, brd, ["b"]) == [[(0, 1)]]
    assert find_length_n_words(1, brd, ["a", "b"]) == [[(0, 0)], [(0, 1)]]
    assert find_length_n_words(1, brd, ["a", "b", "bb"]) == [[(0, 0)], [(0, 1)]]
    assert find_length_n_words(2, brd, ["ab"]) == [[(0, 0), (0, 1)]]
    assert find_length_n_words(2, brd, ["ba"]) == [[(0, 1), (0, 0)]]
    # empty output:
    assert find_length_n_words(1, brd, ["c"]) == []
    assert find_length_n_words(2, brd, ["bc"]) == []
    assert find_length_n_words(3, brd, ["ab"]) == []


def test_find_length_n_words_2x2():
    brd = [["a", "b"], ["c", "d"]]
    # n = 2:
    assert find_length_n_words(2, brd, ["ab", "ba", "bc", "da"]) == [[(0, 0), (0, 1)], [(0, 1), (0, 0)],
                                                                     [(0, 1), (1, 0)], [(1, 1), (0, 0)]]
    # n = 3
    assert find_length_n_words(3, brd, ["abc", "dac", "bc", "da"]) == [[(0, 0), (0, 1), (1, 0)],
                                                                       [(1, 1), (0, 0), (1, 0)]]
    brd = [["a", "a"],
           ["a", "a"]]
    assert len(find_length_n_words(1, brd, "a")) == 4
    assert len(find_length_n_words(2, brd, ["aa"])) == 12
    # assert len(find_length_n_words(3, brd, ["aaa"])) == 24


def test_find_length_n_words():
    test_find_length_n_words_empty_board()
    test_find_length_n_words_one_item()
    test_find_length_n_words_two_items()


def test_max_score_paths():
    brd = [
        ["q", "e", "qu", "a"],
        ["u", "e", "t", "a"],
        ["l", "l", "n", "o"],
        ["o", "t", "x", "l"]
    ]
    assert max_score_paths(brd, ['queen']) == [[(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)]]
    assert ts.compare_lists(max_score_paths(brd, ['queen', 'qua', 'qutn', 'qu']),
                            [[(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)], [(0, 2), (0, 3)], [(0, 2), (1, 2), (2, 2)],
                             [(0, 0), (1, 0)]]) or ts.compare_lists(
        max_score_paths(brd, ['queen', 'qua', 'qutn', 'qu']),
        [[(0, 0), (1, 0), (0, 1), (1, 1), (2, 2)], [(0, 2), (1, 3)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 0)]])
    brd = [
        ["q", "ee", "qu", "a"],
        ["u", "e", "t", "e"],
        ["l", "e", "n", "o"],
        ["o", "te", "x", "l"]
    ]
    assert max_score_paths(brd, ['ee']) == [[(1, 1), (2, 1)]] or [[(2, 1), (1, 1)]]
    assert max_score_paths(brd, ['queete']) == [[(0, 0), (1, 0), (1, 1), (2, 1), (1, 2), (1, 3)]]
    assert max_score_paths(brd, ['quee']) == [[(0, 0), (1, 0), (1, 1), (2, 1)]]
    assert max_score_paths(brd, ['quea']) == [[(0, 2), (1, 3), (0, 3)]]

    # empty output
    assert max_score_paths(brd, ['alon', 'ron']) == []
    assert max_score_paths(brd, ['alon', 'ron', 'dad', 'hello', 'holiday', 'happy', 'ba']) == []


if __name__ == '__main__':
    test_is_valid_path()
    test_find_length_n_paths()
    test_find_length_n_words()
    test_max_score_paths()
