#!/usr/bin/env python3
import curses
import random


def snake(player, stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(10)  # Set input timeout for controlling game speed
    stdscr.clear()

    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Food
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Score

    # Get screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()

    # Create a window for the game
    game_win = curses.newwin(screen_height - 2, screen_width - 2, 1, 1)
    game_win.keypad(True)  # Enable special keys
    game_height, game_width = game_win.getmaxyx()

    # Initialize game variables
    snake = [(game_height // 2, game_width // 4)]  # Start with a single segment
    food = None
    direction = curses.KEY_RIGHT
    score = 0

    # Generate initial food
    while food is None or food in snake:
        food = (random.randint(1, game_height - 2), random.randint(1, game_width - 2))

    # Game loop
    while True:
        # Show score at the top
        stdscr.addstr(0, 0, f" Score: {score} | Press 'q' to quit ", curses.A_REVERSE)
        stdscr.refresh()

        # Get user input
        key = game_win.getch()

        # Handle quitting
        if key == ord("q"):
            break

        # Handle direction change
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            # Prevent 180-degree turns
            if key == curses.KEY_UP and direction != curses.KEY_DOWN:
                direction = key
            elif key == curses.KEY_DOWN and direction != curses.KEY_UP:
                direction = key
            elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
                direction = key
            elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
                direction = key

        # Calculate new head position based on direction
        head_y, head_x = snake[0]
        if direction == curses.KEY_UP:
            head_y -= 1
        elif direction == curses.KEY_DOWN:
            head_y += 1
        elif direction == curses.KEY_LEFT:
            head_x -= 1
        elif direction == curses.KEY_RIGHT:
            head_x += 1

        # Add new head to snake
        snake.insert(0, (head_y, head_x))

        # Check if snake ate food
        if snake[0] == food:
            # Generate new food
            while food in snake:
                food = (
                    random.randint(1, game_height - 2),
                    random.randint(1, game_width - 2),
                )
            score += 10
            # Make game slightly faster as score increases
            new_timeout = max(50, 100 - (score // 50) * 5)
            game_win.timeout(new_timeout)
        else:
            # Remove tail if no food was eaten
            snake.pop()

        # Check for collisions with walls
        head_y, head_x = snake[0]
        if (
            head_y <= 0
            or head_y >= game_height - 1
            or head_x <= 0
            or head_x >= game_width - 1
        ):
            game_over(stdscr, score)
            break

        # Check for collision with self
        if snake[0] in snake[1:]:
            game_over(stdscr, score)
            break

        # Clear and redraw game window
        game_win.clear()

        # Draw border
        game_win.border(0)

        # Draw snake
        for i, (y, x) in enumerate(snake):
            if i == 0:  # Snake head
                game_win.addch(y, x, "O", curses.color_pair(1) | curses.A_BOLD)
            else:  # Snake body
                game_win.addch(y, x, "O", curses.color_pair(1))

        # Draw food
        game_win.addch(food[0], food[1], "*", curses.color_pair(2) | curses.A_BOLD)

        # Refresh the screen
        game_win.refresh()

    return [1, score, player, "snake"]


def game_over(stdscr, score):
    # Display game over message
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    game_over_msg = "GAME OVER!"
    score_msg = f"Your score: {score}"
    exit_msg = "Press any key to exit..."

    # Display centered messages
    stdscr.addstr(
        height // 2 - 2, (width - len(game_over_msg)) // 2, game_over_msg, curses.A_BOLD
    )
    stdscr.addstr(height // 2, (width - len(score_msg)) // 2, score_msg)
    stdscr.addstr(height // 2 + 2, (width - len(exit_msg)) // 2, exit_msg)

    stdscr.refresh()
    stdscr.getch()  # Wait for user input before exiting
