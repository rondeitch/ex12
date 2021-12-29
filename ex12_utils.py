import copy

POSSIBLE_MOVES = {"u": (0, -1), "r": (1, 0), "d": (0, 1), "l": (-1, 0), "ur": (1, -1), "dr": (1, 1), "dl": (-1, 1),
                  "ul": (-1, -1)}


def _is_valid_move(board, path, index):
    """
    Checks if the move is valid.
    :param board: List[List[Any]]
    :param path: List[Tuple[int, int]]
    :param index: int
    :return: bool
    """
    if _is_valid_cell(board, path[index]):
        if index == 0:
            return True
        elif index > 0:
            if path[index] in path[:index] or (
                    path[index - 1][0] - path[index][0],
                    path[index - 1][1] - path[index][1]) in POSSIBLE_MOVES.values():
                return True
    return False


def is_valid_path(board, path, words):
    """
    Checks if the path is valid, and if the word that suites it is in words.
    :param board:  List[List[Any]]
    :param path:  List[Tuple[int, int]]
    :param words: List[str]
    :return: Optional[str]
    """
    word = ''
    for i, cord in enumerate(path):
        if not _is_valid_move(board, path, i):
            return None
        word += str(board[cord[0]][cord[1]])
    if word in words:
        return word
    return None


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


def _path_to_str(board, path):
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


def _find_all_paths_helper(board, word, all_paths, path, sub_word, n, find_len_n_paths):
    """
    Helper for find_all_paths. Find all the paths for the given word.
    :param board: List[List[str]]
    :param word: List[List[Tuple[int, int]]]
    :param all_paths: List[Tuple[int, int]]
    :param path: List[Tuple[int, int]]
    :param sub_word: str
    :param n: int
    :param find_len_n_paths: bool
    :return: None, but append paths to the all_paths list.
    """
    if find_len_n_paths and len(path) > n:
        return
    if _is_valid_sub_word(sub_word, word):
        if len(sub_word) == len(word):
            if find_len_n_paths and len(path) != n:
                return
            all_paths.append(path)
            return
    elif len(sub_word) > len(word):
        return
    prev_cord = path[-1]
    for direction in POSSIBLE_MOVES.values():
        new_cord = prev_cord[0] + direction[0], prev_cord[1] + direction[1]
        # Check if cell in board and if new cord is not in path:
        if _is_valid_cell(board, new_cord) and new_cord not in path:
            new_path = copy.deepcopy(path)
            new_path.append(new_cord)
            new_sub_word = sub_word + board[new_cord[0]][new_cord[1]]
            _find_all_paths_helper(board, word, all_paths, new_path, new_sub_word, n, find_len_n_paths)


def _find_all_paths(board, word, n=0, find_len_n_paths=False):
    """
    Find all the paths for the given word.
    :param board: List[List[str]]
    :param word: str
    :param n: int, default is 0 (made for find_length_n_paths).
    :param find_len_n_paths: bool, default is False (made for find_length_n_paths).
    :return: List[List[Tuple[int, int]]]
    """
    all_paths = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            cord = (x, y)
            _find_all_paths_helper(board, word, all_paths, [cord], board[cord[0]][cord[1]], n, find_len_n_paths)
    return all_paths


def find_length_n_paths(n, board, words):
    """
    Find paths that are in n length for the words in words arg.
    :param n: int
    :param board: List[List[str]]
    :param words: iterable[str]
    :return: List[List[Tuple[int, int]]] or empty list
    """
    all_paths = []
    for word in words:
        all_paths += _find_all_paths(board, word, n, True)
    return all_paths


def find_length_n_words(n, board, words):
    """
    Find paths for words in n length from the words arg.
    :param n: int
    :param board: List[List[str]]
    :param words: iterable[str]
    :return: List[List[Tuple[int, int]]] or empty list
    """
    all_paths = []
    for word in words:
        if len(word) == n:
            all_paths += _find_all_paths(board, word)
    return all_paths


def max_score_paths(board, words):  # TODO: check if its exact how they asked for.
    """
    Return a list of paths that give the max score for the board and words given as input. There is just one path for
    each word (the longest path).
    :param board: List[List[str]]
    :param words: iterable[str]
    :return: List[List[Tuple[int, int]]] or empty list
    """
    all_paths = []
    for word in words:
        paths_for_word = _find_all_paths(board, word)
        if paths_for_word != []:
            max_len = max([len(path) for path in paths_for_word])
            for path in paths_for_word:
                if len(path) == max_len:
                    all_paths.append(path)
                    break
    return all_paths
