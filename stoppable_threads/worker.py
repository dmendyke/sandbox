

##
# Required Modules
#------------------------------------------------------------------------------
from __future__ import print_function  #
from stoppable import Thread as StoppableThread
from random import randint
import stoppable  # Base thread class - includes features to stop a thread



##
# Wrapper around the run function of a thread
# Derived from stoppable.thread
#------------------------------------------------------------------------------
class Worker( stoppable.Thread ) :


  ##
  # Not realy needed but shows that the thread is being correctly collected
  def __del__( self ) :
    print( "Thread '{}' has been garbage collected".format( self.name ) )


  ##
  # This function performs the "work" of the thread
  def run( self ) :
    period = randint( 10, 20 )
    print( 'start of {}, delaying {} seconds.'.format( self.name, period ) )
    self.delay( period )
