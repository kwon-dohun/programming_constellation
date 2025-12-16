def scale_coords(coords, width, height, padding=2):
    PRECISION = 100
    CHAR_ASPECT_Y = 0.4

    GAIN_X = 2.0
    GAIN_Y = 1.5

    precise = [(x * PRECISION, y * PRECISION) for x, y in coords]

    xs = [x for x, y in precise]
    ys = [y for x, y in precise]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    span_x = max_x - min_x
    span_y = max_y - min_y
    if span_x == 0: span_x = 1
    if span_y == 0: span_y = 1

    scale_x = (width - padding * 2) / span_x
    scale_y = (height - padding * 2) / span_y

    base_scale = min(scale_x, scale_y)

    scaled = []
    for x, y in precise:
        sx = (x - min_x) * base_scale * GAIN_X
        sy = (max_y - y) * base_scale * GAIN_Y * CHAR_ASPECT_Y
        scaled.append((sx, sy))

    xs2 = [x for x, y in scaled]
    ys2 = [y for x, y in scaled]

    box_w = max(xs2) - min(xs2)
    box_h = max(ys2) - min(ys2)

    offset_x = (width - box_w) / 2 - min(xs2)
    offset_y = (height - box_h) / 2 - min(ys2)

    points = []
    for x, y in scaled:
        points.append((
            int(x + offset_x),
            int(y + offset_y)
        ))

    return points
