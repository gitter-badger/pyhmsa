#!/usr/bin/env python
"""
================================================================================
:mod:`instrument` -- Instrument condition
================================================================================

.. module:: instrument
   :synopsis: Instrument condition

.. inheritance-diagram:: pyhmsa.condition.instrument

"""

# Script information for the file.
__author__ = "Philippe T. Pinard"
__email__ = "philippe.pinard@gmail.com"
__version__ = "0.1"
__copyright__ = "Copyright (c) 2013 Philippe T. Pinard"
__license__ = "GPL v3"

# Standard library modules.

# Third party modules.

# Local modules.
from pyhmsa.core.condition import _Condition
from pyhmsa.util.parameter import TextAttribute

# Globals and constants variables.

class Instrument(_Condition):

    TEMPLATE = 'Instrument'

    manufacturer = TextAttribute(True, 'Manufacturer', 'manufacturer')
    model = TextAttribute(True, 'Model', 'model')
    serial_number = TextAttribute(False, 'SerialNumber', 'serial number')

    def __init__(self, manufacturer, model, serial_number=None):
        """
        Describes the type of instrument used to collect a HMSA dataset.
        
        :arg manufacturer: manufacturer (required)
        :arg model: model (required)
        :arg serial_number: serial number (optional)
        """
        _Condition.__init__(self)

        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
