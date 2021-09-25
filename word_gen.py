while True:

    from itertools import combinations

    txt = sorted(input("Enter text: "))
    s = set()

    for i in range(1, len(txt)+1):
        s.update(combinations(txt, i))

    with open("words.txt", "r") as words:
        for line in words:
            if tuple(sorted(line.strip())) in s:
                if len(tuple(sorted(line.strip()))) > 2:
                    print(line.strip())

    has_another_word = input("Another entry? ").lower()
    if has_another_word in ("y", "yes"):
        pass
    else:
        break
