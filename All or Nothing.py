def possibly_perfect(key, answers):
    all_correct_possible = True
    all_incorrect_possible = True

    for k, a in zip(key, answers):
        if k == "_":
            continue
        if k != a:
            all_correct_possible = False
        else:
            all_incorrect_possible = False
    return all_correct_possible or all_incorrect_possible