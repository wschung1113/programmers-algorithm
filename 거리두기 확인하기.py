def solution(places):
    answer = []

    def move_cursor(pos):
        if pos[1] < 4:
            pos = (pos[0], pos[1] + 1)
        else:
            pos = (pos[0] + 1, 0)

        return pos

    def get_mh_dist(origin, neigh):
        mh_dist = abs(origin[0] - neigh[0]) + abs(origin[1] - neigh[1])
        return mh_dist

    def is_valid(arr):
        cursor = (0, 0)
        visited_nodes = []
        while cursor != (4, 4):
            if arr[cursor[0]][cursor[1]] == "P":
                origin = cursor
                search_queue = [cursor]
                while len(search_queue) != 0:

                    cur_node = search_queue.pop(0)
                    visited_nodes.append(cur_node)
                    cur_node_val = arr[cur_node[0]][cur_node[1]]
                    for d in ["up", "right", "down", "left"]:
                        if d == "up":
                            neighbor = (cur_node[0] - 1, cur_node[1])
                        elif d == "right":
                            neighbor = (cur_node[0], cur_node[1] + 1)
                        elif d == "down":
                            neighbor = (cur_node[0] + 1, cur_node[1])
                        elif d == "left":
                            neighbor = (cur_node[0], cur_node[1] - 1)
                        if 0 <= neighbor[0] < 5 and 0 <= neighbor[1] < 5 and get_mh_dist(origin, neighbor) <= 2 and neighbor not in visited_nodes and arr[neighbor[0]][neighbor[1]] != "X":
                            search_queue.append(neighbor)
                    if cur_node != origin and cur_node_val == "P":
                        return 0
            cursor = move_cursor(cursor)

        return 1

    for p in places:
        answer.append(is_valid(p))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))