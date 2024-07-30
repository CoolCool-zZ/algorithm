import sys, heapq

sys.stdin = open("input/input_19598_1.txt", "r")
input = sys.stdin.readline

count_of_meeting = int(input())
meeting_time = sorted(list(map(int, input().split())) for _ in range(count_of_meeting))

needed_meeting_room = []
for start, end in meeting_time:
    if needed_meeting_room and needed_meeting_room[0] <= start:
        heapq.heappop(needed_meeting_room)
    heapq.heappush(needed_meeting_room, end)

print(len(needed_meeting_room))
