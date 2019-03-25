import sys
import logging
from ConfigParser import ConfigParser

from bacpypes.debugging import Logging, ModuleLogger
from bacpypes.consolelogging import ConsoleLogHandler

from bacpypes.core import run
from bacpypes.app import BIPSimpleApplication
from bacpypes.object import LocalDeviceObject

#
#   SampleApplication
#

class SampleApplication(BIPSimpleApplication, Logging):

    def __init__(self, device, address):
        if _debug: SampleApplication._debug("__init__ %r %r", device, address)
        BIPSimpleApplication.__init__(self, device, address)

def request(self, apdu):
    if _debug: SampleApplication._debug("request %r", apdu)
    BIPSimpleApplication.request(self, apdu)
def indication(self, apdu):
    if _debug: SampleApplication._debug("indication %r", apdu)
def response(self, apdu):
    if _debug: SampleApplication._debug("response %r", apdu)
    BIPSimpleApplication.response(self, apdu)
def confirmation(self, apdu):
    if _debug: SampleApplication._debug("confirmation %r", apdu)
    BIPSimpleApplication.confirmation(self, apdu)

