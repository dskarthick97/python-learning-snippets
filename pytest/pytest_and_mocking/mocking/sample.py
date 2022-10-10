from dice import roll_dice


def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"
