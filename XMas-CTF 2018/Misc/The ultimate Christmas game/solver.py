import functools

MISERE = 'misere'
NORMAL = 'normal'


def nim(heaps, game_type):
    print(game_type, heaps, end=' ')

    is_misere = game_type == MISERE

    count_non_0_1 = sum(1 for x in heaps if x > 1)
    is_near_endgame = (count_non_0_1 <= 1)

    if is_misere and is_near_endgame:
        moves_left = sum(1 for x in heaps if x > 0)
        is_odd = (moves_left % 2 == 1)
        sizeof_max = max(heaps)
        index_of_max = heaps.index(sizeof_max)

        if sizeof_max == 1 and is_odd:
            return "You will lose :("
        return index_of_max, sizeof_max - int(is_odd)

    nim_sum = functools.reduce(lambda x, y: x ^ y, heaps)
    if nim_sum == 0:
        return "You will lose :("

    for index, heap in enumerate(heaps):
        target_size = heap ^ nim_sum
        if target_size < heap:
            amount_to_remove = heap - target_size
            return index, amount_to_remove


print(nim([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0], NORMAL))
