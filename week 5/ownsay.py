import sys

from sayings import hello

# type in command line window "python ownsay.py Riddhi"
if len(sys.argv) == 2:
    hello(sys.argv[1])

