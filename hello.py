#!/usr/bin/env python

import curses
import time

def WordDrift(slang, speed=0.08):
    screen = curses.initscr()
    curses.noecho()
    screen.nodelay(1)
    dims = screen.getmaxyx()
    q = -1
    x, y = 0, 0
    Vertical = 1
    Horizontal = 1
    while q != ord('q'):
        screen.clear()
        screen.addstr(y, x, slang)
        screen.refresh()

        if y == dims[0] - 1:
            Vertical = -1
        elif y == 0:
            Vertical = 1
        if x == dims[1] - len(slang) - 1:
            Horizontal = -1
        elif x == 0:
            Horizontal = 1
        y += Vertical
        x += Horizontal

        q = screen.getch()
        if q == ord('w') and y > 0:
            y -= 1
        elif q == ord('s') and y < dims[0]-1:
            y += 1
        elif q == ord('a') and x > 0:
            x -= 1
        elif q == ord('d') and x < dims[1] - len(slang) - 1:
            x += 1

        time.sleep(speed)

    curses.endwin()

def main():
    WordDrift("Hellow")

if __name__ == "__main__":
    main()
