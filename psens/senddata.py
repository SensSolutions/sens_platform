<<<<<<< HEAD
"""
This module sends data to broker and if it's not possible store-it in a
cache-file to send later.

created on Mon Sep 07 10:12:58 2015

@author: mcollado
"""

#import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
=======
#import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
>>>>>>> df8fadd644727277eb92d1862dc1fc651f0eeac4
import logging
import csv
import os

logger = logging.getLogger('PSENSv0.1')
<<<<<<< HEAD
logger.debug(sendData)

def sendData(d):
    """ This function send data recoverd by sensor to broker """
=======

def sendData(d):
>>>>>>> df8fadd644727277eb92d1862dc1fc651f0eeac4
    """
    Check if broker is alive
    Check if exists a cache file
    Send cache data to broker then send last data
    If no broker, append data to cache file
<<<<<<< HEAD

    Must remove non required keys before send json:
    required_fields = ['name', 'last_name', 'phone_number', 'email']
    dict2 = {key:value for key, value in dict1.items() if key in required_fields}
    """
    try:
        mqttc = mqtt.Client(d['clientId'])
        mqttc.connect(d['brokerIP'], 1883)
        #
        if os.path.isfile(d['cachefile']):
            sendFromCache(d['brokerIP'], d['clientId'], d['cachefile'])
        mqttc.connect(d['brokerIP'], 1883)
        mqttc.publish(d['topic'], d['message'])
        # implement clean disconnect from broker. Maybe
        logger.debug('Topic: %s : %s | Client ID: %s', d['topic'], d['message'], d['clientId'])
    except Exception, err:
        """Implement code to diferenciate connections error from others"""
        logger.warning('Error: %s, %s', str(err), d['brokerIP'])
        sendToCache(d['cachefile'], d['topic'], d['message'])


def sendFromCache(brokerIP, clientId, cachefile):
    """This function send cache file contens to broker"""

    logger.debug('Reading cache file %s', cachefile)

    with open(cachefile, "r") as csvfile:
        f = csv.reader(csvfile, delimiter=';')
        count = 0
        try:
            mqttc = mqtt.Client(clientId)
            mqttc.connect(brokerIP, 1883)

            for row in f:
                # logger.warning('Read line: %i - topic: %s msg: %s',f.line_num, row[0], str(row[1]))
                mqttc.publish(row[0], row[1])
                # publish.single(row[0] , row[1], brokerIP, client_id= clientId, will=None, auth=None, tls=None)
                count += 1
                logger.debug('Send line: %i - topic: %s msg: %s',
                             f.line_num, row[0], str(row[1]))

            logger.warning("%i lines sent, removing cachefile: %s",
                           count, cachefile)
            os.remove(cachefile)

        except Exception, err:
            logger.warning('Error trying to send cache: %s', str(err))
            # csv.Error as e:
            # logger.warning('Error reading %s, line %d: %s' % (cachefile, f.line_num, csv.Error))

def sendToCache(cachefile, topic, message):
    """Convert dictionary in CSV data before write-it to cache file?"""
    try:
        """
        save data not send in JSON format

        d = {'Topic': topic, 'Message': message, 'Date': hora}
        with open(cachefile + ".json", 'a') as jsonfile:
            jsontext = '{"Topic":' + topic + ', "Message":"' + message + '"}'
            print(d)
            json.dump(d,jsonfile, sort_keys = True, ensure_ascii=False)
        """
        with open(cachefile + ".csv", 'a') as csvfile:
            cachewriter = csv.writer(csvfile, delimiter=';')
            cachewriter.writerow([topic, message])
        logger.debug('Writing CSV line to cache file: %s', cachefile)

    except Exception, err:
        logger.warning('Error %s', err)

=======
    """



def sendFromCache(brokerIP, clientId, cachefile):

    logger.debug(sendCache)
    logger.warning ('Reading cache file %s', cachefile)

    with open (cachefile, "r") as csvfile:
        f = csv.reader(csvfile, delimiter =';')
        try:
            mqttc=mqtt.Client(clientId)
            mqttc.connect(brokerIP, 1883)

            for row in f:
                logger.warning('Read line: %i - topic: %s msg: %s',f.line_num, row[0], str(row[1]))
                mqttc.publish(row[0], row[1])
                #publish.single(row[0] , row[1], brokerIP, client_id= clientId, will=None, auth=None, tls=None)
                logger.warning('Send line: %i - topic: %s msg: %s',f.line_num, row[0], str(row[1]))

            logger.debug("Cache sent, removing cachefile: %s",cachefile)
            os.remove(cachefile)

        except Exception, e:
            logger.warning('Error trying to send cache: %s', str(e))
            # csv.Error as e:
            # logger.warning('Error reading %s, line %d: %s' % (cachefile, f.line_num, csv.Error))

def sendToCache(d):
    """Convert dictionary in CSV data before writ-it to cache file"""
    with open(cachefile + ".csv", 'a') as csvfile:
        cachewriter = csv.writer(csvfile, delimiter=';')
        cachewriter.writerow([topic, message, hora])
    logger.debug('Writing CSV line to cache file: %s', cachefile)
>>>>>>> df8fadd644727277eb92d1862dc1fc651f0eeac4

