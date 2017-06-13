
# Time-stamp: <2017-04-13 14:05:55 dmendyke>   -*- mode: python; -*-

import tty, sys, termios

##
# Required modules
#------------------------------------------------------------------------------
from sys import stdin
from tty import tcgetattr, setraw, TCSADRAIN, tcsetattr


##
#
#------------------------------------------------------------------------------
def getkey( ) :
  _file_id = stdin.fileno()
  _previous = tcgetattr( _file_id )
  try :
    setraw( stdin.fileno() )
    _key = stdin.read( 1 )  # single key press
  finally :
    tcsetattr( _file_id, TCSADRAIN, _previous )
  return _key
