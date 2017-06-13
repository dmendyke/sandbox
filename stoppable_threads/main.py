#!/usr/bin/env python2


##
# Required modules
#------------------------------------------------------------------------------
from __future__ import print_function  # Use python3 print function
from worker import Worker
from running import Running
from termination import TerminationSignalHandler


##
# Main class
#------------------------------------------------------------------------------
class Application( object ) :


  ##
  # Constructor
  def __init__( self ) :
    super( Application, self ).__init__()
    self.signal_handler = TerminationSignalHandler( Running.Stop )


  ##
  # enter into the object
  def main( self ) :
    for name in [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven' ] :
      Worker( name ).start()
    while Running()() : pass


##
# Entry into the application
#------------------------------------------------------------------------------
if __name__ == '__main__' : Application().main()
