#!/usr/bin/python3
""" UTF-8 Validate """


def validUTF8(data):
    """
    Determines if given data set represents valid UTF-8 encoding.
    """
    n_b = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        m_b = 1 << 7

        if n_b == 0:

            while m_b & i:
                n_b += 1
                m_b = m_b >> 1

            if n_b == 0:
                continue

            if n_b == 1 or n_b > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                    return False

        n_b -= 1

    if n_b == 0:
        return True

    return False
