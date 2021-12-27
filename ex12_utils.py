import copy

POSSIBLE_MOVES = {"u": (0, -1), "r": (1, 0), "d": (0, 1), "l": (-1, 0), "ur": (1, -1), "dr": (1, 1), "dl": (-1, 1),
                  "ul": (-1, -1)}


def _is_valid_move(board, path, index):
    x = path[index][0]
    y = path[index][1]
    if 0 <= x <= (len(board[0]) - 1) and 0 <= y <= (len(board) - 1):
        if index == 0:
            return True
        elif index > 0 and \
                (path[index - 1][0] - path[index][0], path[index - 1][1] - path[index][1]) in POSSIBLE_MOVES.values():
            return True
    return False


def is_valid_path(board, path, words):
    word = ''
    for i, cord in enumerate(path):
        if i > 0:
            if cord in path[:i] or not _is_valid_move(board, path, i):
                return None
            else:
                word += str(board[cord[1]][cord[0]])
        elif not _is_valid_move(board, path, i):
            return None
        else:
            word += str(board[cord[1]][cord[0]])
    if word in words:
        return word
    else:
        return None


def is_valid_sub_word(sub_word, word):
    if sub_word == word[0:len(sub_word)]:
        return True
    return False


def path_to_str(board, path):
    word = ""
    for cord in path:
        word += board[cord[1]][cord[0]]
    return word


def is_valid_cell(board, cord):
    x, y = cord
    if 0 <= y < len(board) and 0 <= x < len(board[0]):
        return True
    return False


def _all_paths_to_word_helper(board, word, all_paths, path, sub_word):
    if is_valid_sub_word(sub_word, word):
        if len(sub_word) == len(word):
            all_paths.append(path)
            return
    elif len(sub_word) > len(word):
        return
    prev_cord = path[-1]
    for direction in POSSIBLE_MOVES.values():
        new_cord = prev_cord[0] + direction[0], prev_cord[1] + direction[1]
        # Check if cell in board and if new cord is not in path:
        if is_valid_cell(board, new_cord) and new_cord not in path:
            new_path = copy.deepcopy(path)
            new_path.append(new_cord)
            new_sub_word = sub_word + board[new_cord[1]][new_cord[0]]
            _all_paths_to_word_helper(board, word, all_paths, new_path, new_sub_word)


def find_paths_to_word(board, word):
    all_paths = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            cord = (x, y)
            _all_paths_to_word_helper(board, word, all_paths, [cord], board[cord[1]][cord[0]])
    return all_paths


def find_length_n_paths(n, board, words):
    all_paths = []
    for word in words:
        if len(word) == n:
            all_paths += find_paths_to_word(board, word)
    return all_paths


def find_length_n_words(n, board, words):
    pass


def max_score_paths(board, words):
    pass
