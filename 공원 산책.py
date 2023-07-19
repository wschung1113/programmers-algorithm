def solution(park, routes):
    park_x = len(park[0])
    park_y = len(park)
    for ix, p in enumerate(park):
        if "S" in p:
            answer = [ix, p.index("S")]
    for r in routes:
        direction = r[0]
        magnitude = int(r[-1])
        x = answer[1]
        y = answer[0]
        if direction == "E":
            if x + magnitude >= park_x:
                continue
            no_obstacle = True
            for i in range(x + 1, x + magnitude + 1):
                if park[y][i] == "X":
                    no_obstacle = False
                    break
            if no_obstacle:
                answer[1] += magnitude
        elif direction == "S":
            if y + magnitude >= park_y:
                continue
            no_obstacle = True
            for i in range(y + 1, y + magnitude + 1):
                if park[i][x] == "X":
                    no_obstacle = False
                    break
            if no_obstacle:
                answer[0] += magnitude
        elif direction == "N":
            if y - magnitude < 0:
                continue
            no_obstacle = True
            for i in range(y - 1, y - magnitude - 1, -1):
                if park[i][x] == "X":
                    no_obstacle = False
                    break
            if no_obstacle:
                answer[0] -= magnitude
        elif direction == "W":
            if x - magnitude < 0:
                continue
            no_obstacle = True
            for i in range(x - 1, x - magnitude - 1, -1):
                if park[y][i] == "X":
                    no_obstacle = False
                    break
            if no_obstacle:
                answer[1] -= magnitude
    return answer