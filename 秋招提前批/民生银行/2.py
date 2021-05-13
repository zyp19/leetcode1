import sys
num = 0
t = input()
if t == "1":
    # 统计行数
    for line in sys.stdin.readline():
        if not line:
            continue
        num += 1
    print(num)
elif t == "Q":
    print("Quit")
else:
    print("Wrong input.Please re-choose")
    print("Menu Function Test")
    print("1:Count Lines")
    print("Q:Quit")
