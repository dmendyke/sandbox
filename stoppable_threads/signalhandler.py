
#
# Required Modules
from signal import getsignal, signal #, SIGKILL, SIGINT, SIGTERM  # signals


#
# Written by Daniel Mendyke [dmendyke@jaguarlandrover.com]
__author__ = 'dmendyke'


#
# Wrapper around chain of handler functions for a specific system level signal.
# Often used to trap Ctrl-C for specific application purposes.
class Signal(object):  # python 3+ class Signal

    '''
    Capture and replace a signal handler with a user supplied function.
    The user supplied function is always called first then the previous
    handler, if it exists, will be called.  It is possible to chain several
    signal handlers together by creating multiply instances of objects of
    this class, providing a  different user functions for each instance.  All
    provided user functions will be called in LIFO order.
    '''

    #
    # Constructor
    # Get the previous handler function then set the passed function
    # as the new handler function for this signal
    def __init__(self, sig_value, func):
        '''
        Create an instance of the signal handler class.

        sig_value:  The ID value of the signal to be captured.
        func:  User supplied function that will act as the new signal handler.
        '''
        super(Signal, self).__init__()  # python 3+ 'super().__init__()
        self.__sig_value = sig_value
        self.__user_func = func  # store user passed function
        self.__previous_func = getsignal(sig_value)  # get current handler
        signal(sig_value, self)

    #
    # Called to handle the passed signal
    def __call__(self, signame, sf):
        '''
        Allows the instance of this class to be called as a function.
        When called it runs the user supplied signal handler than
        checks to see if there is a previously defined handler.  If
        there is a previously defined handler call it.
        '''
        self.__user_func()  # call user function
        try:
            if self.__previous_func:
                self.__previous_func(signame, sf)
        except KeyboardInterrupt as kbi:
            pass

    #
    # reset the signal handler
    def __del__(self):
        '''
        Class destructor.  Called during garbage collection.
        Resets the signal handler to the previous function.
        '''
        signal(self.__sig_value, self.__previous_func)

    # End class Signal


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
