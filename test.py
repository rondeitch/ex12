from ex12_utils import *

POSSIBLE_MOVES = {"u": (0, -1), "r": (1, 0), "d": (0, 1), "l": (-1, 0), "ur": (1, -1), "dr": (1, 1), "dl": (-1, 1),
                  "ul": (-1, -1)}

words1 = ["hello", "world", "queen", "ron", "alon", "time", "boggle", "list"]
words_cord_dict = {"hello": [(0, 0), (0, 1), (0, 2), (1, 2), (0, 3)], "queen": [(2, 0), (1, 0), (1, 1), (2, 2)]}
brd = [
    ["h", "e", "qu", "e"],
    ["e", "e", "t", "a"],
    ["l", "l", "n", "o"],
    ["o", "t", "x", "l"]
]


def test_is_valid_path():
    assert is_valid_path(brd, words_cord_dict["hello"], words1) == "hello"
    assert is_valid_path(brd, words_cord_dict["queen"], words1) == "queen"
    assert is_valid_path(brd, [(-1, 3)], words1) is None
    assert is_valid_path(brd, [(5, 3)], words1) is None
    assert is_valid_path(brd, [(3, 3), (4, 3)], words1) is None
