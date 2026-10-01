# Command-Line Robot

A text-based robot simulation by **Daniel Pena Arias**, created for a Logic & Design midterm in November 2025.

The program simulates movement, LED state, servo positions, and a randomized dance using Python functions, conditionals, loops, and shared state. It runs entirely in the terminal and does not connect to physical robot hardware.

## Run

Requires Python 3. No third-party packages are needed. Open a terminal in this folder:

```sh
python robot.py
```

On Windows, `py robot.py` also works if the Python launcher is installed.

| Menu | Controls |
| --- | --- |
| 1 — Drive | `w` forward, `a` left, `d` right, `s` backward, `x` stop |
| Drive speed | `t` increase, `g` decrease; bounded from 0 to 10 |
| 2 — LEDs | `y` toggles the current LED state |
| 3 — Servo | `l` left, `r` right, `h` home |
| 4 — Dance | Random movement messages for approximately five seconds |
| 5 — Quit | Exit the program |

Use `m` to leave the drive or servo submenu. Type a command and press Enter. Commands are lowercase. State lasts only for the current session, and speed changes do not model physical movement or distance.

## Checks

```sh
python -m unittest -v
```

Tests cover menu repetition, speed boundaries, LEDs, servo positions, and the dance sequence without waiting five seconds.

## Coursework and maintenance

October 2026 portfolio maintenance replaced recursive menu calls with a loop, added an import guard, and used a monotonic timer for the dance duration. See [CHANGES.md](CHANGES.md).

Source: [danpena27/command-line-robot](https://github.com/danpena27/command-line-robot)
