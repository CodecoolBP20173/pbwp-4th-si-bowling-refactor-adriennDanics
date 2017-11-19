def score(game):
    if game[-3] == 'X' or game[-3] == 'x':
        return how_to_count(game, len(game) - 2)
    else:
        return how_to_count(game, len(game))


def how_to_count(game, length):
    result = 0
    for i in range(length):
        if game[i] == '/':
                result += 10 - get_value(game[i-1]) + get_value(game[i+1])
        elif game[i] == 'X' or game[i] == 'x':
            result += get_value(game[i]) + get_value(game[i+1])
            if game[i+2] == '/':
                result += 10 - get_value(game[i+1])
            else:
                result += get_value(game[i+2])
        else:
            result += get_value(game[i])
    return result


def get_value(char):  # Values for rolls in game
    if char in str([i for i in range(1, 10)]):
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
