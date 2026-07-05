import cowsay
import sys

# type "python say.py Riddhi"
if len(sys.argv) == 2:
    cowsay.cow("hello, "+ sys.argv[1])
    cowsay.trex("hello, "+ sys.argv[1])

