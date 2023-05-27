# input
N, M = (int(x) for x in input().split())
S = [input() for i in range(N)]

# make diff table [NxN]
diff_table = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        # calc diff
        diff = 0
        for k in range(M): diff += 0 if S[i][k] == S[j][k] else 1
        diff_table[i][j] = diff

# search (dfs)
stack = [[i] for i in range(N)]
flag = False
while 0 < len(stack):
    target = stack.pop()
    for i in range(N):
        if diff_table[target[-1]][i] == 1 and not i in target:
            stack.append(target + [i])
            if len(stack[-1]) == N:
                flag = True
                break
            else:
                continue

# output
print('Yes' if flag else 'No')
