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
        # avail is the number of spaces available in the current run of free space
        avail = spaces.popleft()
        # sometimes we have 0 spaces, we want to add the next run of blocks to the
        # assembled list if so
        if avail == 0:
            assembled.append(files.popleft())
        # determine how much to prune from the end of files
        while avail > 0 and files:
            last_run = files[-1][1]  # length of the last run of numbers
            # do we have space to put the whole run?
            if last_run <= avail:
                # pop off the last set of values, reduce the available space count
                nxt = files.pop()
                avail -= last_run
                assembled.append(nxt)
            else:
                # split the run and reduce the count of the final block count
                files[-1][1] -= avail
                assembled.append([files[-1][0], avail])
                avail = 0
            # used up all of the run of free space, put the next block of files
            # onto the assembled list
            if avail == 0:
                assembled.append(files.popleft())
    # if we have used all available spaces but there are files left, assemble them
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
