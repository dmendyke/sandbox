

##
# Required Modules
#------------------------------------------------------------------------------
from signalhandler import Signal  # base handler module
from signal import SIGTERM, SIGINT  # symbols for specific signals



##
# Create an object that handles terminating the application
# upon receiving a SIGTERM or a SIGINT from an outside source
#------------------------------------------------------------------------------
class TerminationSignalHandler( object ) :


  ##
  # Constructor - Defines the pointers to the Signal objects
  def __init__( self, term_func ) :
    super( TerminationSignalHandler, self ).__init__()
    self._handle = {
      SIGTERM: Signal( SIGTERM, term_func ),
      SIGINT: Signal( SIGINT, term_func )
    }  # end self.signal
