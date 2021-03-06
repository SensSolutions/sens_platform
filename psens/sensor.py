"""
This module read data from sensors loading specific driver for every sensor

created on Mon Sep 07 10:12:58 2015

@author: mcollado

        http://stackoverflow.com/a/5391245
        try:
            func = getattr(modulename, funcname)
        except AttributeError:
            print 'function not found "%s" (%s)' % (funcname, arg)
        else:
            func(arg)


        http://stackoverflow.com/a/15004155
        The gettattr function has an optional third argument for a default
        value to return if the attribute does not exist, so you could use that:

        fun = getattr(modulename, funcname, None)

        if fun is None:
            print 'function not found "%s" (%s)' % (funcname, arg)
        else
            fun(arg)

"""

import importlib
import logging
# import custom modules
from sensors import bogus

logger = logging.getLogger('PSENSv0.1')


def readSensor(SensorDict):
    '''
    This funtion loads correct driver for every sensor
    and returns the read values.

    readSensor() returns a list whith sensor data, usualy a row for every
    value:
    [{"name": "air", "temperature": 25.5, "type": "sensor", "what": "sensors"},
     {"name": "air", "humidity": 50.5, "type": "sensor", "what": "sensors"}]

    '''
    try:

        module_name = str("sensors." + SensorDict['subtype'])
        logger.debug('Loading Sensor module %s with driver "%s"',
                     module_name, SensorDict['driver'])
        sen_module = importlib.import_module(module_name, package=None)
        try:
            # print s_module
            # print my_module
            sen_function = getattr(sen_module, SensorDict['driver'])
            logger.debug("%s", sen_module)
            # except AttributeError:
            # logger.warning("Function not found %s (%s)", SensorDict['driver'], SensorDict)
        except Exception, err:
            logger.warning("Error: %s", err)
        sen_result = sen_function(SensorDict)

    except Exception, err:
        logger.warning("Error importing custom module: %s No driver for: %s",
                       str(err), sen_module)
        logger.debug("Using Bogus function")
        sen_result = bogus.bogus(SensorDict)

    return sen_result

