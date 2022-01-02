import copy
import timeit

import boggle_board_randomizer
import collections

POSSIBLE_MOVES = {"u": (-1, 0), "r": (0, 1), "d": (1, 0), "l": (0, -1), "ur": (-1, 1), "dr": (1, 1), "dl": (1, -1),
                  "ul": (-1, 1)}
SEARCH_WORD, SEARCH_PATH = True, False


def create_words_dict():
    word_dict = []
    with open("boggle_dict.txt", "r") as file:
        for line in file:
            word_dict.append(line.strip())
    return word_dict


def _is_valid_sub_word(sub_word, word):
    """
    Chaecks if the sub-word is valid.
    :param sub_word: str
    :param word: str
    :return: bool
    """
    if sub_word == word[0:len(sub_word)]:
        return True
    return False


def path_to_str(board, path):
    """
    Return the path to the word from the content of the cells.
    :param board: List[List[str]]
    :param path: List[Tuple[int, int]]
    :return: str
    """
    word = ""
    for cord in path:
        word += board[cord[0]][cord[1]]
    return word


def _is_valid_cell(board, cord):
    """
    Checks if the cell is in the board range.
    :param board: List[List[str]]
    :param cord: Tuple[int, int]
    :return: bool
    """
    x, y = cord
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    return False


def _is_path_reached_limit(limit, search_type, path, sub_word):
    search_by_word = search_type is SEARCH_WORD and len(sub_word) >= limit
    search_by_path = search_type is SEARCH_PATH and len(path) >= limit
    if search_by_path or search_by_word:
        return True
    return False


def _find_all_paths_helper(limit, search_type, board, words, all_paths, path, sub_word):
    # if reached limit by word or path length (depends on search type):
    if _is_path_reached_limit(limit, search_type, path, sub_word):
        if sub_word in words:
            all_paths.append(copy.deepcopy(path))
        return
    for direction in POSSIBLE_MOVES.values():  # iterate all directions
        new_cord = path[-1][0] + direction[0], path[-1][1] + direction[1]
        if _is_valid_cell(board, new_cord) and new_cord not in path:  # check if new_cord is not in path and is in board
            prev_word = sub_word
            sub_word += board[new_cord[0]][new_cord[1]]  # add new_letter to sub_word
            path.append(new_cord)  # add new_cord to path
            _find_all_paths_helper(limit, search_type, board, words, all_paths, path, sub_word)
            sub_word = prev_word  # return to prev word
            path.pop()  # remove new_cord from path


def find_length_n_words(n, board, words):
    all_paths = []
    word_dict = dict()  # create a dictionary from words list
    for word in words:
        if len(word) == n:  # filter dict with n length words
            word_dict[word] = 0
    # iterate all cells in board
    for r in range(len(board)):
        for c in range(len(board[r])):
            _find_all_paths_helper(n, SEARCH_WORD, board, word_dict, all_paths, [(r, c)], board[r][c])
    return all_paths


def find_length_n_paths(n, board, words):
    all_paths = []
    word_dict = dict()  # create a dictionary from words list
    for word in words:
        word_dict[word] = 0
    # iterate all cells in board
    for r in range(len(board)):
        for c in range(len(board[r])):
            _find_all_paths_helper(n, SEARCH_PATH, board, word_dict, all_paths, [(r, c)], board[r][c])
    return all_paths


def max_score_paths(board, words):
    max_length = len(max(words, key=len))
    max_score = 0
    for n in range(max_length + 1, max_length // 2, -1):
        print(n)


brd = boggle_board_randomizer.randomize_board()
boggle_dict = create_words_dict()
max_score_paths(brd, boggle_dict)
# print(brd)
# w_paths = find_length_n_paths(5, brd, boggle_dict)
#
# for p in w_paths:
#     print(path_to_str(brd, p), end=" ")
# print()
