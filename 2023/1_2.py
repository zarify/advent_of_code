def coord(s, debug=False):
    """
    Take a string s of digits and digits as words and return the concatenation of
    the first and last digits as an integer. If there is a single digit then the
    return value should be that digit repeated as it is the first AND the last digit.
    Word values should be searched from the beginning and from the end, as there may
    be overlapping characters from other word values.
    """
    nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    first = None
    last = None
    org_s = s
    for i in range(len(s)):
        found = False
        if s[i].isdigit():
            first = s[i]
            break
        for n in nums:
            if s[i:].startswith(n):
                first = str(nums[n])
                found = True
                break
        if found:
            break
    # now work backwards
    for i in range(len(s)-1, -1, -1):
        found = False
        if s[i].isdigit():
            last = s[i]
            break
        for n in nums:
            if s[i:].startswith(n):
                last = str(nums[n])
                found = True
                break
        if found:
            break
    if first is None or last is None:
        return None
    ret = int(first + last)
    if debug:
        print(f"{org_s} => {first}, {last}")
    return ret

if __name__ == "__main__":
    with open("1_1.txt") as f:
        data = f.read().strip().split("\n")
        data = [coord(x,i<10) for i,x in enumerate(data)]
        # print(data)
        print(sum(data))