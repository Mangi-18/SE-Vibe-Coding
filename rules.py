def valid_move(board, orientation, row, col):
    return board._line_is_available(orientation, row, col)


def completed_boxes(board, before):
    return len(board.completed - before)
