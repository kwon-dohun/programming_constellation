def render(points, width, height):
    grid = [[" " for _ in range(width)] for _ in range(height)]

    for x, y in points:
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = "✦"

    lines = ["".join(row) for row in grid]

    while lines and lines[0].strip() == "":
        lines.pop(0)
    while lines and lines[-1].strip() == "":
        lines.pop()

    return "\n".join(lines)
