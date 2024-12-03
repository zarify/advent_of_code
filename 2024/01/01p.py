import pandas as pd

df = pd.read_csv(
    "input",
    sep = "   ",
    header = None,
    names = ["first", "second"],
    engine = "python"
)
# Part 1

# .values gives a numpy array that ignores the index, otherwise subtracting
# these does it in the original order, not the sorted order
print(
    "Part A:",
    abs(
        df["first"].sort_values().values - df["second"].sort_values().values
    ).sum()
)

# Part 2

right = df["second"].value_counts()
# map the counts of each value to their respective position in "first"
# filling any nonexistent entries with 0
in_right = df["first"].map(right).fillna(0)
print(
    "Part B:",
    (df["first"] * in_right).sum()
)