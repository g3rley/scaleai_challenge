# Scale AI - Challenge

<p align="center">
  <img src="https://github.com/g3rley/scaleai_challenge/assets/96620547/e42d376a-7f3e-4c2e-a179-a59daf016f0d" alt="image">
</p>

## Introduction

This is a solution to the Scale AI challenge. The solution is written in Python 3.7.3. The solution is divided into two
problems. The first problem is a simple string manipulation problem. The second problem is a physics problem.

### Problem 1: Passing Notes

You and your friend are passing notes in class, but to secure the safety of your notes you both decide to scramble the words. Your friend is going to pass you the first note, so that you can figure out the type of scramble that was used. Use the example test case below to figure out how the words where scrambled and write a program that will scramble words in the same way.

**Input**
The only line that you will be given will the plain unscrambled note that you want to send.

**Output**
Print the scrambled version of the note, so that you can send a message to your friend safely.

**Example**
```
Input: good luck trying to figure out how this was scrambled :)

Output: ): delbmarcs saw siht woh tuo erugif ot gniyrt kcul doog
```

### Problem 2: H. Flying balls

Petya and Kolya love to play with balls. Now they are playing an interesting game called "Collision". The essence of
the game is as follows. Kolya throws a ball, and Petya tries to knock this ball down with another ball. Petya was
interested in whether it is possible to calculate the point at which they will collide from the information about the
position of the balls and their velocities. Help, please, Pete.
Input data. The input file consists of two lines. The first line describes Colin's ball, the second - Petin. For each ball, 7
parameters are given: R, x, y, z, vx, vy, vz, where R is the radius of the ball; x, y, z are its initial coordinates; vx, vy, vz
are its initial speed. Since the boys throw the balls very hard, the acceleration can be neglected.

All numbers in the input file are integers, their absolute value does not exceed 10000. At the initial moment, the balls
do not touch.

Output. In the first line print the word "YES" if the balls collide, or the word "NO" if they don't. If the answer is yes, then
in the second line print the coordinates of the point where they collide. If the answer is no, then print the minimum
distance between the balls. All numbers must be displayed with 5 decimal places.

**Example**
```
Input:
Input.txt

1 0 0 0 1

Output.txt
100 1000-2
3000001
YES
0.00000 0.00000 5.00000
```

## Solution

### Problem 1: Passing Notes

The solution to this problem is in the file `problem1.py`. The solution is a simple python script that takes in a string
and reverses it. The script can be run as follows:

```
python problem_one.py "good luck trying to figure out how this was scrambled :)"
```

### Problem 2: H. Flying balls

The solution to this problem is in the file `problem2.py`. The solution is a simple python script that takes in a file
containing the information about the balls and outputs the result. The script can be run as follows:

```
python problem_two.py input.txt
```

## Author

* **[Gerley Adriano](github.com/g3rley)**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
