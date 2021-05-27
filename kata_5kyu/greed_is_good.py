def greed_is_good_score(dice):
    dice_freq = {d: dice.count(d) for d in dice}

    score = 0
    for k, v in dice_freq.items():

        if v >= 3:
            score += k * 1000 if k == 1 else k * 100
            if k == 1 and v > 3:
                score += k * (v - 3) * 100
            if k == 5 and v > 3:
                score += k * (v - 3) * 10
        else:
            score += k * v * 100 if k == 1 else 0
            score += k * v * 10 if k == 5 else 0

    return score


def solution(dice):
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]

    counter = [0, 0, 0, 0, 0, 0]
    for die in dice:
        counter[die - 1] += 1

    sum = 0
    for i, count in enumerate(counter):
        triple, unit = divmod(count, 3)  # divmod takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
        sum += triple * points[i] + unit * extra[i]

    return sum
