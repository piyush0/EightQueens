def unset_kth_bit(n, k):
    if k < 0:
        return n
    return n & ~(1 << k)


def set_kth_bit(n, k):
    return (1 << k) | n


def is_kth_bit_set(n, k):
    if n & (1 << k):
        return True
    else:
        return False
