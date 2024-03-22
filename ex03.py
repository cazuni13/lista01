def form_pyramid(base: list):
    pyramid = [base]

    while len(base) > 1:

        next_level = []
        for i in range(len(base) - 1):
            brick = base[i] + base[i + 1]
            next_level.append(brick)

        base = next_level

        pyramid.append(next_level)

    for level in reversed(pyramid):
        print(level)


form_pyramid([30, 12, 10, 5])