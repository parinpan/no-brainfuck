def brainfuck_reader(s):
    i, ptr = 0, 0
    out, stack = [], []
    blocks = [0 for _ in range(0, 30000)]

    while i < len(s) and 0 <= ptr < len(blocks):
        c = s[i]

        ptr += int(c == '>')
        ptr -= int(c == '<')
        blocks[ptr] += int(c == '+')
        blocks[ptr] -= int(c == '-')

        if c == '.':
            out.append(blocks[ptr])
        elif c == '[' and blocks[ptr] != 0:
            stack.append(i)
        elif c == ']':
            if blocks[ptr] == 0:
                stack.pop()
            else:
                i = stack[-1]

        i += 1

    return ''.join([chr(o) for o in out])
