# codeforces
# # This approach counts good pairs and subtracts from total pairs to get splits
n = int(input())
arr = []
pos = {}
for t_index in range(n):
    tower = list(map(int, input().split()))
    arr.extend(tower[1:])
    for i, b in enumerate(tower[1:]):
        pos[b] = (t_index, i)

arr.sort()
good_pair = 0
for i in range(len(arr)-1):
    current = pos[arr[i]]
    next_ = pos[arr[i+1]]
    c_t, c_i = current
    n_t, n_i = next_
    if c_t == n_t and n_i == c_i + 1:
        good_pair += 1

pairs = len(arr) - n # each tower subtract one from the its length
splits = pairs - good_pair
combines = splits + n - 1
print(splits, combines)



# # Approach: save all the blocks in a list, sort,
#  and store their successor positions in position dictionary.
# count blocks that deviate their natural orders - on splits
# combine = needs to be the size of splits and the number of initial tower configuration minus 1
# becuase combining n items need n-1 operation eg. for 3 blocks 2 combine operation

# n = int(input())
# towers = []
# together = []
# for _ in range(n):
#     tower = list(map(int, input().split()))
#     towers.append(tower[1:])
#     together.extend(tower[1:])

# together.sort()
# position = {}

# for tower in towers:
#     for i in range(len(tower)):
#         if i < len(together)-1:
#             cur_element_index = together.index(tower[i])
#             next_element = together[cur_element_index + 1:][:1] # get the next element
#             position[tower[i]] = next_element

# splits = 0
# for tower in towers:
#     for i in range(len(tower)-1):
#         if position[tower[i]] and position[tower[i]][0] != tower[i+1]:
#             splits += 1
#         elif not position[tower[i]] and tower[i+1]:
#             splits += 1

# combines = n + splits - 1
# print(splits, combines)