import random


def game(start_pos: int) -> dict:
    if not 0 < start_pos < 6:
        raise ValueError('Nie ma otworu')
    # current_pos = start_pos + 3
    current_pos = start_pos + 2
    paths = []
    for i in range(4):
        choice = random.randint(0, 1)
        current_pos += 0.5 if choice else -0.5
        paths.append('P' if choice else 'L')
    scores = {
        '1': 1000,
        '2': 10,
        '3': 2000,
        '4': 1,
        '5': 500,
        '6': 1,  # zmienic na 500 w z3
        '7': 2000,
        '8': 10,
        '9': 1000,

    }
    current_pos = str(int(current_pos))
    return {'final': current_pos, 'score': scores[str(current_pos)], 'path': paths}


if __name__ == '__main__':
    _scores = []
    for _ in range(1000):
        _scores.append(game(3)['score'])
    print(sum(_scores) / len(_scores))
    print('-----')
    for y in range(1,6):
        _scores = []
        for i in range(4000):
            _scores.append(game(y)['score'])
        print(sum(_scores) / len(_scores))
