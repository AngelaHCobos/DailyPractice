def dishes(n, q):
    stacks = [[]]
    for query in q:
        if query[0] == "ADD":
            if not stacks:
                stacks.append([])
            if len(stacks[-1]) < n:
                stacks[-1].append(query[1])
            else:
                stacks.append([query[1]])
        elif query[0] == "REMOVE":
            print(stacks[0].pop())
            for index, stack in enumerate(stacks):
                if index != 0:
                    stacks[index - 1].append(stack.pop())
            if not stacks[-1]:
                stacks.pop()
        elif query[0] == "COUNT":
            if len(stacks) > query[1]:
                print(len(stacks[query[1]]))
            else:
                print(-1)

dishes(2, [("ADD", 13), ("ADD", 7), ("ADD", 17), ("COUNT", 0), ("COUNT", 1), ("ADD", 2), ("COUNT", 1), ("ADD", 47), ("REMOVE",), ("COUNT", 0), ("COUNT", 1), ("COUNT", 2)])