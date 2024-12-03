import pandas as pd

# list of Series, since the shape of each row is not necessarily the same
with open("input") as f:
    data = [pd.Series(x.split()).astype(int) for x in f.read().strip().split("\n")]


def validate(s):
    return all(s.diff(1).dropna().abs().isin([1, 2, 3])) and (
        all(s.diff(1).dropna() < 0) or all(s.diff(1).dropna() > 0)
    )


# PART A
# Check if in order and 1 <= n <= 3 difference between each n
print("Part A:", sum([validate(s) for s in data]))

# PART B
# Check if dropping any single value will make the series valid.
print(
    "Part B:", sum([any([validate(d.drop(i)) for i, _ in enumerate(d)]) for d in data])
)
