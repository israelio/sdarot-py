from itertools import product

import requests

from configuration import Configuration

sids = [''.join(sid) for sid in product('0123456789', repeat=4)]
series_exists = []


def url(sid): return f'{Configuration.SDAROT_MAIN_URL}/watch/{sid}'


def get_last_series(arr, bot, top):

    while bot < top:

        mid = (bot + top) // 2

        is_exists = requests.head(url(arr[mid])).status_code == 200
        print(arr[mid], is_exists)

        # If x is greater, ignore left half
        if is_exists:
            bot = mid + 1

        # If x is smaller, ignore right half
        else:
            top = mid - 1

    is_exists = requests.head(url(arr[bot])).status_code == 200
    sid = bot - (0 if is_exists else 1)
    print(arr[mid], is_exists)
    return sid


get_last_series(sids, 0, len(sids))
