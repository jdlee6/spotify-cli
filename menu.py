"""
Usage:
  spot_cli.py  <name> -a (displays users saved albums)
  spot_cli.py  <name> -t (displays users saved playlists)
  spot_cli.py  <name> -s (searches for albums by artists)
    * can also look at the album tracks

Options:
  -h --help     Show this screen.
  --version     Show version.  

* <name> refers to the name of the current user
"""
from docopt import docopt
if __name__ == '__main__':
    arguments = docopt(__doc__, version='1')
    print(arguments)