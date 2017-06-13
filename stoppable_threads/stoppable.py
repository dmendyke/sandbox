

##
# Required Modules
#------------------------------------------------------------------------------
from __future__ import print_function  # use version 3 print function
from threading import Thread as OriginalThread  # standard thread class
from time import sleep  # delay in seconds
from running import Running  # Termination flag



##
# Wrap the standard thread class around a signal handler that
# can interrup the thread if a signal is caught.
#------------------------------------------------------------------------------
class Thread( OriginalThread ) :


  ##
  # Constructor
  def __init__( self, name = False ) :
    super( Thread, self ).__init__()
    if name : self.name = name  # save the thread name


  ##
  # built in "sleep" function will check for end condition
  def delay( self, period ) :
    while Running()() and period > 0 :
      period = period - 1  # reduce the period by 1 second
      sleep( 1 )
