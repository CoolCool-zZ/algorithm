import sys
from collections import deque

# remove this line before submit
sys.stdin = open("input/input_13913_1.txt", "r")

input = sys.stdin.readline

subin_location, sister_location = map(int, input().split())

current_location = subin_location
visited = [{"depth": -1, "parent": -1} for i in range(100_001)]
visited[current_location] = {"depth": 0, "parent": current_location}
found = False

depth = 0
bfs_queue = deque([current_location])
while not found:
    current_location = bfs_queue.popleft()
    current_depth = visited[current_location]["depth"] + 1

    if current_location == sister_location:
        found = True
        break

    for next_location in (
        current_location * 2,
        current_location - 1,
        current_location + 1,
    ):
        if 0 <= next_location < 100_001 and visited[next_location]["depth"] == -1:
            bfs_queue.append(next_location)
            visited[next_location] = {
                "depth": current_depth,
                "parent": current_location,
            }
            if next_location == sister_location:
                found = True
                current_location = next_location
                break

path = []
print(visited[current_location]["depth"])
while current_location != subin_location:
    path.append(current_location)
    current_location = visited[current_location]["parent"]

path.append(subin_location)
path.reverse()
answer = " ".join(map(str, path))
print(answer)
