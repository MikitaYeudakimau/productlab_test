def check_relation(net, first, second):
    friends = {}
    for pair in net:
        x, y = pair
        if x not in friends.keys():
            friends[x] = set()
        if y not in friends.keys():
            friends[y] = set()
        friends[x].add(y)
        friends[y].add(x)

    passed= set()
    stack = [first]
    while stack:
        current = stack.pop()
        passed.add(current)
        if current == second:
            return True
        for friend in friends[current]:
            if friend not in passed:
                stack.append(friend)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
