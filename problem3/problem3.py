text = open("problem3.txt", "r").readlines()


def get_tree_count(right_steps, down_steps):
    h_pos = 0
    tree_count = 0
    for idx, line in enumerate(text):
        if idx % down_steps == 0:
            line = line.rstrip("\n")
            ch = line[h_pos]
            if ch == "#":
                tree_count += 1
            h_pos = (h_pos + right_steps) % len(line)
    return tree_count


# Part 1
num_trees = get_tree_count(3, 1)


# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
all_n_trees = 1
for s in slopes:
    n = get_tree_count(*s)
    all_n_trees = all_n_trees * n
