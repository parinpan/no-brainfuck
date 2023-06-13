def brainfuck_reader(s):
    i, ptr = 0, 0
    out, stack = [], []
    blocks = [0 for _ in range(0, 30000)]

    def jump(idx):
        bracket = 1

        while idx < len(s) and bracket != 0:
            idx += 1
            bracket += int(s[idx] == '[')
            bracket -= int(s[idx] == ']')

        return idx

    while i < len(s) and 0 <= ptr < len(blocks):
        if s[i] == ',':
            blocks[ptr] = int(input('enter a block value: ')) % 256
        elif s[i] == '.':
            out.append(blocks[ptr])
        elif s[i] == '[' and blocks[ptr] != 0:
            stack.append(i)
        elif s[i] == '[' and blocks[ptr] == 0:
            i = jump(i)
        elif s[i] == ']' and blocks[ptr] != 0:
            i = stack[-1] - 1
        elif s[i] == ']' and blocks[ptr] == 0:
            stack.pop()
        else:
            ptr += int(s[i] == '>')
            ptr -= int(s[i] == '<')
            blocks[ptr] += int(s[i] == '+')
            blocks[ptr] -= int(s[i] == '-')
            blocks[ptr] = blocks[ptr] % 256

        i += 1

    return ''.join([chr(o) for o in out])
