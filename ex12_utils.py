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


def find_length_n_paths(n, board, words):
    pass


def find_length_n_words(n, board, words):
    pass


def max_score_paths(board, words):
    pass
