input = [
['E', 'Y'],
['Y', 'T'],
['I', 'C'],
['G', 'F'],
['C', 'P'],
['B', 'Q'],
['Z', 'N'],
['J', 'W'],
['W', 'P'],
['K', 'D'],
['Q', 'L'],
['V', 'D'],
['O', 'M'],
['A', 'P'],
['M', 'L'],
['R', 'S'],
['D', 'X'],
['X', 'N'],
['P', 'T'],
['F', 'N'],
['S', 'L'],
['U', 'N'],
['T', 'L'],
['N', 'H'],
['L', 'H'],
['N', 'L'],
['X', 'F'],
['P', 'F'],
['P', 'H'],
['B', 'D'],
['V', 'H'],
['X', 'S'],
['Q', 'O'],
['Z', 'T'],
['K', 'N'],
['S', 'H'],
['M', 'P'],
['Q', 'D'],
['R', 'U'],
['J', 'P'],
['P', 'S'],
['V', 'U'],
['R', 'T'],
['F', 'S'],
['D', 'T'],
['E', 'N'],
['J', 'N'],
['J', 'A'],
['K', 'U'],
['V', 'N'],
['V', 'S'],
['U', 'L'],
['F', 'U'],
['I', 'T'],
['J', 'L'],
['E', 'T'],
['T', 'N'],
['I', 'G'],
['R', 'D'],
['E', 'B'],
['X', 'H'],
['P', 'L'],
['Z', 'J'],
['O', 'L'],
['E', 'H'],
['F', 'T'],
['A', 'F'],
['U', 'H'],
['F', 'H'],
['C', 'W'],
['A', 'L'],
['V', 'M'],
['U', 'T'],
['E', 'P'],
['Y', 'U'],
['W', 'R'],
['E', 'X'],
['Q', 'U'],
['I', 'F'],
['V', 'F'],
['V', 'T'],
['R', 'P'],
['B', 'A'],
['S', 'T'],
['M', 'F'],
['Y', 'F'],
['C', 'K'],
['D', 'S'],
['O', 'S'],
['M', 'U'],
['Z', 'S'],
['R', 'H'],
['C', 'O'],
['G', 'Q'],
['Z', 'D'],
['B', 'N'],
['I', 'H'],
['I', 'P'],
['E', 'J'],
['V', 'L'],
['B', 'U'],
]

requirements = dict()

for i in input:
    requirements[i[1]] = requirements.get(i[1], []) + [i[0]]
    requirements[i[0]] = requirements.get(i[0], [])

def main():
    global input
    import string
    from contextlib import suppress
    
    letters = '.' + string.ascii_uppercase  # align letter with time needed
    total = len(requirements)
    output = ''
    second = -1
    workers = [[0, 0] for _ in range(5)]
    while len(output) < total:
        second += 1
        for w in workers:
            if w[0] != 0:
                w[1] -= 1
                if w[1] == 0:
                    l = w[0]
                    output += l
                    for r in requirements.keys():
                        with suppress(Exception):
                            requirements[r].remove(l)
                    w[0] = 0
        for w in workers:
            if w[0] == 0:
                for l in letters:
                    i = requirements.get(l, None)
                    if isinstance(i, list) and len(i) == 0:
                        requirements[l] = None
                        w[0] = l
                        w[1] = 60 + letters.index(l)
                        break

    print(second)


main()