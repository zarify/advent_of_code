import re
def coord(s, debug=False):
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
    first_m = re.match(r"^.*?(\d|one|two|three|four|five|six|seven|eight|nine)", s, re.MULTILINE)
    last_m = re.match(r".*(\d|one|two|three|four|five|six|seven|eight|nine).*?$", s, re.MULTILINE)
    if first_m and last_m:
        first = first_m.group(1) if first_m.group(1).isdigit() else str(nums[first_m.group(1)])
        last = last_m.group(1) if last_m.group(1).isdigit() else str(nums[last_m.group(1)])
        return int(first + last)
    else:
        return None

if __name__ == "__main__":
    with open("1_1.txt") as f:
        data = f.read().strip().split("\n")
        data = [coord(x,i<10) for i,x in enumerate(data)]
        # print(data)
        print(sum(data))