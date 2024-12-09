from collections import deque

with open("test") as f:
    data = f.read().strip()

# grab each second number from the input string into the files and free lists,
# keeping track of what the current file_id is from its position
# turns into a list of [[file_id, run_amount], ... ]
space_file = [[file_id, int(amount)] for file_id, amount in enumerate(data[::2])]
space_free = data[1::2]


def defrag(files, spaces):
    spaces = deque(map(int, spaces))
    files = deque(files)
    assembled = [files.popleft()]
    while spaces and files:
        avail = spaces.popleft()
        if avail == 0:
            assembled.append(files.popleft())
        # avail is the number of spaces available, idx contains
        # the insertion point into `spaces`, which will continue to
        # be a deque of [file_id, amount] lists
        # determine how much to prune from the end of files
        while avail > 0 and files:
            last_run = files[-1][1]  # length of the last run of numbers
            # do we have space to put the whole run?
            if last_run <= avail:
                # pop off the last set of values, reduce the available space
                # count, and add it to the move list
                nxt = files.pop()
                avail -= last_run
                assembled.append(nxt)
            else:
                # split the run
                files[-1][1] -= avail
                assembled.append([files[-1][0], avail])
                avail = 0
            if avail == 0:
                assembled.append(files.popleft())
    while files:
        assembled.append(files.popleft())
    return assembled


def calc_checksum(file_list):
    total = 0
    place = 0
    for n, i in file_list:
        while i > 0:
            total += n * place
            place += 1
            i -= 1
    return total


files = defrag(space_file, space_free)
print(f"Part A: {calc_checksum(files)}")

# Part B
