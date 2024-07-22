import sys

# remove this line before submit
sys.input = open("input/input_13023_1.txt", "r")

input = sys.stdin.readline

# get first input
count_of_people, count_of_relationship = map(int, input().split())

# make graph
relation_graph = [[] for i in range(count_of_people)]

for relation in range(count_of_relationship):
    person1, person2 = map(int, input().split())
    relation_graph[person1].append(person2)
    relation_graph[person2].append(person1)

# dfs
def dfs(graph, nth_person, visited, depth):
    global found
    if depth == 4:
        found = True
        return
    for related_person in graph[nth_person]:
        if not visited[related_person]:
            visited[related_person] = True
            dfs(graph, related_person, visited, depth + 1)
            visited[related_person] = False


if count_of_relationship < 4:
    print(0)
else:
    found = False
    for person in range(count_of_people):
        visited = [False] * count_of_people
        visited[person] = True
        dfs(relation_graph, person, visited, 0)
        if found:
            break

    if found :
        print(1)
    else :
        print(0)
