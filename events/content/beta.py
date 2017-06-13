
# Time-stamp: <2017-04-13 14:27:45 dmendyke>   -*- mode: python; -*-

##
# Sample 'SystemEvent' - Q key pressed
##



from event import SystemEvent
from threading import Thread
from getkey import getkey

##
#
#------------------------------------------------------------------------------
class Event( SystemEvent ) :

  ##
  # Constructor
  # Perform init of instance variables and resources
  def __init__( self ) :
    super( SystemEvent, self ).__init__()
    self._data = 'qkey'

  ##
  # Wait until a 'Q' has been printed
  #@staticmethod
  #def _read_key( instance ) :
  def __call__( self ) :
    _continue = True
    while _continue == True :
      _key = getkey().upper()
      print( 'BETA key: {}'.format( _key ) )
      if _key == 'Q' :
        print( self._data )
        _continue = False

  ##
  # entery into this 'SystemEvent'
  # Actually start actions for this instance
  def main( self ) :
    self._handle = Thread( target = self )
    self._handle.start()
