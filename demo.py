# author: Ruben De la Garza
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]          Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)

def main():
  print(opt)
  print(opt["<arg4>"])
  print(type(opt))

if __name__ == "__main__":
  main()
