from collections import Counter


def find_duplicate(nums):
    if nums:
        for num in nums:
            if type(num) != int or num < 1:
                return False
        most = Counter(nums).most_common(1)[0]
        if most[1] > 1:
            return most[0]
    return False
