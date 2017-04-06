#!/usr/bin/env python

import curses
import time
import random

def instructions(screen):
    dims = screen.getmaxyx()
    screen.clear()
    screen.nodelay(0)
    lines = ['Use W/S/A/D and the arrow keys to move', "Word will reflect if run into the wall",
            '', 'Press Any Key to go back']
    for z in range(len(lines)):
        screen.addstr((dims[0]-len(lines))/2+z, (dims[1]-len(lines[z]))/2, lines[z])
    screen.refresh()
    screen.getch()
    menu(screen)

def menu(screen):
    dims = screen.getmaxyx()
    screen.clear()
    screen.keypad(1)
    screen.nodelay(0)
    selection = -1
    option = 0
    optlen = 3
    while selection < 0:
        graphics = [0]*optlen
        graphics[option] = curses.A_REVERSE
        screen.addstr(0, dims[1]/2-3, "WordDrift")
        screen.addstr(dims[0]/2-1, dims[1]/2-2, "Play", graphics[0])
        screen.addstr(dims[0]/2, dims[1]/2-6, "Instructions", graphics[1])
        screen.addstr(dims[0]/2+1, dims[1]/2-2, "Exit", graphics[2])
        screen.refresh()
        action = screen.getch()
        if action == curses.KEY_UP:
            option = (option-1) % optlen
        elif action == curses.KEY_DOWN:
            option = (option+1) % optlen
        elif action == ord('\n'):
            selection = option

    screen.clear()
    if selection == 0:
        WordDrift(screen, "Hellow")
    elif selection == 1:
        instructions(screen)

def WordDrift(screen, slang, speed=0.08):
    screen.clear()
    screen.nodelay(1)
    screen.keypad(1)
    screen.border()
    dims = screen.getmaxyx()
    q = -1
    x, y = 1, 1
    Vertical = 1
    Horizontal = 1

    gameover = False
    foodmade = False

    while not gameover:
        while not foodmade:
            b, a = random.randrange(2, dims[0]-2), random.randrange(2, dims[1]-2)
            if screen.inch(b, a) == ord(' '):
                foodmade = True
                screen.addch(b, a, ord('@'))

        if y == dims[0] - 2:
            Vertical = -1
        elif y == 1:
            Vertical = 1
        if x == dims[1] - len(slang) - 2:
            Horizontal = -1
        elif x == 1:
            Horizontal = 1

        for z in range(len(slang)):
            screen.addch(y, x+z, ' ')
        y += Vertical
        x += Horizontal

        q = screen.getch()
        if (q == ord('w') or q == curses.KEY_UP) and y > 1:
            y -= 1
        elif (q == ord('s') or q == curses.KEY_DOWN) and y < dims[0]-2:
            y += 1
        elif (q == ord('a') or q == curses.KEY_LEFT) and x > 1:
            x -= 1
        elif (q == ord('d') or q == curses.KEY_RIGHT) and x < dims[1] - len(slang) - 2:
            x += 1
        elif q == ord('q'):
            gameover = True

        for z in range(len(slang)):
            if screen.inch(y, z+x) == ord('@'):
                gameover = True

        screen.addstr(y, x, slang)
        screen.refresh()

        time.sleep(speed)

    screen.clear()
    screen.nodelay(0)
    message1 = 'Game Over'
    message2 = 'Press Space to play again'
    message3 = 'Press Enter to quit'
    message4 = 'Press M to go back to the menu'
    screen.addstr(dims[0]/2-1, (dims[1]-len(message1))/2, message1)
    screen.addstr(dims[0]/2, (dims[1]-len(message2))/2, message2)
    screen.addstr(dims[0]/2+1, (dims[1]-len(message3))/2, message3)
    screen.addstr(dims[0]/2+2, (dims[1]-len(message4))/2, message4)
    screen.refresh()
    q = 0
    while q not in [32, 10, 77, 109]: # ' ', Enter, 'm', 'M'
        q = screen.getch()
    if q == 32:
        WordDrift(screen, "Hellow")
    elif q == 77 or q == 109:
        menu(screen)



def main():
    scr = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    menu(scr)
    curses.endwin()

if __name__ == "__main__":
    main()
