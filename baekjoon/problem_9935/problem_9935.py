import sys

sys.stdin = open("input/input_9935_2.txt", "r")

input = sys.stdin.readline
after_explosion_no_char = "FRULA"

given_string = input().rstrip()
explosion_string = input().rstrip()
len_explosion_string = len(explosion_string)

stack = []
for i in range(len(given_string)):
    stack.append(given_string[i])
    if "".join(stack[-len_explosion_string:]) == explosion_string:
        for j in range(len_explosion_string):
            stack.pop()

answer = "".join(stack)

print(answer if answer != "" else after_explosion_no_char)
