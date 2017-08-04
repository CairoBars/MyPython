#Author:Cairo Li

import sys


sys.argv.append("r")
sys.argv.append("G:/Python/learn/MyPython/basic/day12/2.txt")

print(sys.argv)

if len(sys.argv) < 3:
    print("usage: grepword.py word infile1 [infile2 [... infileN]]")
    sys.exit()

print(sys.argv[2:])

word = sys.argv[1]
for filename in sys.argv[2:]:

    for lino, line in enumerate(open(filename), start=1):
        if word in line:
            print("{0}:{1}:{2:.40}".format(filename, lino,
                                           line.rstrip()))
