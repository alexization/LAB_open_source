import curses
import random
import os
import sys

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

# 게임 화면 설정
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = stdscr.subwin(sh, sw, 0, 0)

w.keypad(1)
w.timeout(100)

# 초기 위치 및 뱀 설정
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# 먹이 설정
food = [sh // 2, sw // 2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# 방향 설정
key = curses.KEY_RIGHT

# 점수 초기화
score = 0

# 게임 루프
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # 게임 종료 조건
    if (
        snake[0][0] in [0, sh - 1] or
        snake[0][1] in [0, sw - 1] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        print("Score: ", score)
        ans = input("게임을 재시작 하시겠습니까? (y/n) : ")
        while True:
            if ans == 'y':
                restart()
            elif ans =='n':
                quit()
            else:
                print("잘못된 응답입니다. 다시 입력해주세요.")
                ans = input("게임을 재시작 하시겠습니까? (y/n) : ")
    new_head = [snake[0][0], snake[0][1]]

    # 방향 설정
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # 먹이 먹기
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    snake.insert(0, new_head)
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

    w.addstr(0, 2, f"Score: {score}")