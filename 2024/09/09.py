from collections import deque

with open("input") as f:
    data = f.read().strip()

# grab each second number from the input string into the files and free lists,
# keeping track of what the current file_id is from its position
# turns into a list of [[file_id, run_amount], ... ]
space_file = [[file_id, int(amount)] for file_id, amount in enumerate(data[::2])]
space_free = data[1::2]


# A much faster method of running Part A, running two separate queues for spaces
# and files, but doesn't work for Part B. Keeping it around to remind myself how
# much slower the combined method is.
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


def defrag_combined(seq, contiguous=False):
    # find a file index or suitably large space
    def find_file(n, seq):
        for i in range(len(seq) - 1, -1, -1):
            if seq[i][0] == n:
                return i

    def find_space(n, seq):
        for i, s in enumerate(seq):
            if s[0] is None and (s[1] >= (n if contiguous else 1)):
                return i
        return -1

    # keep track of the last file moved
    last_file = seq[-1][0]
    while last_file:
        # get the index of the current file to be moved
        # and find a suitable space if there is one
        pos = find_file(last_file, seq)
        spos = find_space(seq[pos][1], seq)
        # found sufficient space and it's to the left of the file
        if spos != -1 and spos < pos:
            # how much space remains after shifting all of the file?
            # this can be negative if we're not in contiguous mode
            remaining = seq[spos][1] - seq[pos][1]
            if remaining >= 0:  # moving the whole file
                item = seq[pos]
                seq[pos] = [None, item[1]]  # set the moved file to blank space
                last_file -= 1
            else:  # split the file
                item = [seq[pos][0], seq[spos][1]]  # fill space available
                seq[pos][1] = abs(remaining)  # overflow is left in place
            seq.insert(spos, item)  # insert it before the space it fills
            if remaining <= 0:
                del seq[spos + 1]  # delete the now filled space
            else:
                seq[spos + 1][1] = remaining  # update the remaining space
        else:
            # move to the next file if we haven't found enough space
            last_file -= 1
    return seq


def calc_checksum(file_list):
    total = 0
    place = 0
    for n, i in file_list:
        while i > 0:
            if n:
                total += n * place
            place += 1
            i -= 1
    return total


disk = deque()
for i, n in enumerate(data):
    n = int(n)
    if i % 2 == 0:
        val = i // 2
    else:
        val = None
    # spaces are None, file ids are i
    disk.append([val, n])

files = defrag_combined(disk)
print(f"Part A: {calc_checksum(files)}")

# Part B
# reset the data since the defrag function modifies the deque
disk = deque()
for i, n in enumerate(data):
    n = int(n)
    if i % 2 == 0:
        val = i // 2
    else:
        val = None
    # spaces are None, file ids are i
    disk.append([val, n])

files2 = defrag_combined(disk, contiguous=True)
print(f"Part B: {calc_checksum(files2)}")
