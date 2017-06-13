
##
# Required Modules
#------------------------------------------------------------------------------
from __future__ import print_function



##
# Object to hold the flag which determines the running state of the application
#------------------------------------------------------------------------------
class Running( object ) :


  ##
  # Class variables - static variables
  __currently = True  # Default is that the application is running


  ##
  # Set the flag to 'false' meaning not running
  @staticmethod
  def Stop( ) : Running.__currently = False


  ##
  # Return a bool value on if the application flag is set to 'true' - running
  @staticmethod
  def __call__( ) : return Running.__currently



  ##
  # Return the opposite of the running flag
  @staticmethod
  def Stopped( ) : return not Running.__currently
