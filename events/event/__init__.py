


##
# Required modules
#------------------------------------------------------------------------------


##
# Defines system events and procedure to use them
#------------------------------------------------------------------------------
class SystemEvent( object ) :

  ##
  # Constants used with this class
  SYSTEM_EVENT = [ 'KEY', 'MOUSE' ]


  ##
  # Constructor
  def __init__( self ) :
    print( 'SystemEvent.__init__' )


  ##
  # called when (and if) the event is to be unloaded
  def unload( self ) :
    print( 'SystemEvent.unload' )
