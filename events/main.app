#!/usr/bin/env python2

# Time-stamp: <2017-04-13 15:54:10 dmendyke>   -*- mode: python; -*-


from handler import Handler


##
# Main class of the application
#------------------------------------------------------------------------------
class Application( object ) :   # python3+ 'class Application :'

  def __init__( self ) :
    print( 'Application.__init__' )
    self._handle = Handler()


  ##
  #
  def _run( self ) :
    self._handle.start_events()
    while True : pass

  ##
  # Static entry into this class
  @staticmethod
  def main( ) :
    print( 'Application.main' )
    Application()._run()

##
# Entry into the application
#------------------------------------------------------------------------------
if __name__ == '__main__' : Application.main()
