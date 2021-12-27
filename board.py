class Board:
    def __init__(self, board):
        # TODO: add more validations for board
        if not isinstance(board, list):
            raise TypeError("Board is not a list")
        self.__board = board # List[List[Any]

    @property
    def board(self):
        return self.__board

    def is_valid_cell(self, x, y):
        # TODO
        # notice: board is not necessarily a square
        pass

    def get_cell_content(self, x, y):
        """
        :param x: int
        :param y: int
        :return: return the content of the of the cell
        """
        if not self.is_valid_cell(x, y):  # TODO : CHECK IF NECESSARY
            raise IndexError("Cell is not valid.")
        pass

    def set_cell_content(self, x, y, data):
        """
        :param x:
        :param y:
        :param data:
        :return:
        """
        if not self.is_valid_cell(x, y):
            raise IndexError("Cell is not valid.")
        pass
