# developed and organised by Ashwin kk 
# for any Queries: 00ashwinkk00@gmail.com
def calc():
    import pandas as pd
    df = pd.read_excel('coordi.xlsx')
    xyz = list(df.itertuples(index=False, name=None))
    print(xyz)

    # xyz = [
    #        (0, 0, 0), (0, 2, 0), (2, 2, 0), (2, 0, 0),
    #        (0, 0, 4), (0, 2, 4), (2, 2, 4), (2, 0, 4)
    #       ]

    def group_coordinates(coordinates):
        group = []
        n = len(coordinates)
        used = [False] * n

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        p1, p2, p3, p4 = coordinates[i], coordinates[j], coordinates[k], coordinates[l]

                        x_vals = {p1[0], p2[0], p3[0], p4[0]}
                        y_vals = {p1[1], p2[1], p3[1], p4[1]}

                        if len(x_vals) == 2 and len(y_vals) == 2:
                            group.append([p1, p2, p3, p4])
                            used[i] = used[j] = used[k] = used[l] = True

        last_coordinate = None
        for i in range(n):
            if not used[i]:
                last_coordinate = coordinates[i]
                break

        return group, last_coordinate  # Now returning two values

    groups, last_coordinate = group_coordinates(xyz)
    volume = 0

    for j in groups:
        x1, y1, z1 = j[0]
        x2, y2, z2 = j[1]
        x3, y3, z3 = j[2]
        x4, y4, z4 = j[3]

        # Shoelace theorem
        area = 0.5 * abs(x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - (y1 * x2 + y2 * x3 + y3 * x4 + y4 * x1))
        z_avg = (z1 + z2 + z3 + z4) / 4

        volume += area * z_avg

    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def find_adjacent_points(points, target):
        distances = [(point, manhattan_distance(point, target)) for point in points if point != target]
        distances.sort(key=lambda x: x[1])
        return [distances[0][0], distances[1][0]]

    if last_coordinate is not None:
        adjacent_points = find_adjacent_points(xyz, last_coordinate)
        tp1, tp2, tp3 = last_coordinate, adjacent_points[0], adjacent_points[1]
        area = 0.5 * abs(tp1[0] * (tp2[1] - tp3[1]) + tp2[0] * (tp3[1] - tp1[1]) + tp3[0] * (tp1[1] - tp2[1]))

        tpz_avg = (tp1[2] + tp2[2] + tp3[2]) / 3
        volume += area * tpz_avg

    return volume/10

vol = calc()
print(vol)
