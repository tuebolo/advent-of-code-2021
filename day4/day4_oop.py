import numpy as np


def read_input_numbers(file: str):
    with open(file) as f:
        lines = f.readlines()

    drawn_numbers = list(map(int, lines[0].split()[0].split(',')))
    bingo_data = lines[2:]

    bingo_sheets = np.loadtxt(bingo_data)
    bingo_sheets = np.split(bingo_sheets.astype(int), len(bingo_sheets) / 5)
    return drawn_numbers, bingo_sheets


class Sheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def mark(self, number):
        match = np.where(self.sheet == number)
        if match[0].size == 0:  # no match found
            return False

        row = match[0][0]  # row
        column = match[1][0]  # column
        self.sheet[row][column] = -1
        return True

    def is_finished(self):
        for line in range(5):
            # check each column
            if (self.sheet[:, line] > 0).sum() == 0:
                return True

            # check each row
            if (self.sheet[line] > 0).sum() == 0:
                return True

    def get_winners(self):
        leader_board = []
        for line in range(5):
            # check each column
            if (self.sheet[:, line] > 0).sum() == 0:
                leader_board.append(self.index)
                winning_

            # check each row
            if (self.sheet[line] > 0).sum() == 0:
                return True

    def sum(self):
        return self.sheet[self.sheet > 0].sum()

class Sheets:
    def __init__(self, sheets):
        self.sheets = sheets

    def mark_and_check(self, number):
        for sheet in self.sheets:
            if sheet.mark(number):
                if sheet.is_finished():
                    return sheet

def find_answer(file):
    drawn_numbers, bingo_sheets_master = read_input_numbers(file)
    bingo_sheets = np.copy(bingo_sheets_master)
    sheets = Sheets([Sheet(s) for s in bingo_sheets])

    for drawn_number in drawn_numbers:
        board = sheets.mark_and_check(drawn_number)
        if board is not None:
            return board.sum() * drawn_number

    assert 'No board found'




