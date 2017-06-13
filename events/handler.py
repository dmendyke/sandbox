

##
# Required modules
#------------------------------------------------------------------------------
from importlib import import_module
from glob import glob  # used to read files
from re import match  # regex matching
from constants import FIRST_MATCH  # first indexed REGEX match


class EventBag( object ) :


  FILTER = 'content/[!_]*.py'
  PATTERN = r"content/(.+).py"
  MODULE = 'content.{}'


  def __init__( self ) :
    super( EventBag, self ).__init__()
    self.parse_events()



  ##
  # Return array of all event modules in the directory 'content'
  def _all_events_in_directory( self ) :
    return glob( self.FILTER )

  ##
  # All system level event code must define a class 'Event', derived
  # from 'SystemEvent'
  # Dynamically, at runtime, load a named event module (written in python)
  # found in the directory (./content)
  def _import( self, name ) :
    return import_module( self.MODULE.format( name ) ).Event()


  ##
  # Find the name of the module
  def _event_name( self, module ) :
    return match( self.PATTERN, module ).group( FIRST_MATCH )


  def parse_events( self ) :
    self._bag = {}  # start with empty bag
    for module in self._all_events_in_directory( ) :
      name = self._event_name( module )
      self._bag[ name ] = self._import( name )


  ##
  # Run the function 'func' on each element in the bag
  def on_all( self, func ) :
    for element in self._bag :
      getattr( self._bag[ element ], func )()




##
#
#------------------------------------------------------------------------------
class Handler( object ) :


  ##
  # Constants


  def __init__( self ) :
    super( Handler, self ).__init__()
    self._event_bag = EventBag()


  def start_events( self ) :
    self._event_bag.on_all( 'main' )


  def unload_events( self ) :
    self._event_bag.on_all( 'unload' )
