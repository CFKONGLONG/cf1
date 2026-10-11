import random

answer = random.randint(1, 100)
count = 0

print("=== 猜数字小游戏 ===")
print("我已经想好了一个 1-100 之间的整数，请开始猜吧！")

while True:
    guess_str = input("请输入你猜的数字（1-100）：")

    if not guess_str.strip().isdigit():
        print("输入无效，请输入一个整数！")
        continue

    guess = int(guess_str)
    count += 1

    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print(f"恭喜你，猜中了！答案就是 {answer}")
        print(f"你一共猜了 {count} 次")
        break