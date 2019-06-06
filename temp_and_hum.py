# Temperature and Humidity sensor program using DHT11 by Adafruit using
# Adafruit Python DHT Sensor Library
# https://github.com/adafruit/Adafruit_Python_DHT

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import time
import datetime
import Adafruit_DHT

SHADOW_CLIENT = "myShadowClient"

# Hidden host name (Modified for security)
HOST_NAME = "XXXXXXXXXXXXXXXXXXXXXX.amazonaws.com"

# Path to root CA file
ROOT_CA = "AmazonRootCA1.pem"

# Path to private key file
PRIVATE_KEY = "XXXXXXXXXXXXprivate.pem.key"

# Path to certificate file
CERT_FILE = "XXXXXXXXXXXXXXXXXXXXX.pem.crt.txt"
#"yourkeyid-certificate.pem.crt.txt"

# AWS IoT thing name, my RaspberryPi device
SHADOW_HANDLER = "MyRPi"

###########################################################

# Automatically called whenever the shadow is updated.
def myShadowUpdateCallback(payload, responseStatus, token):
    print()
    print('UPDATE: $aws/things/' + SHADOW_HANDLER +
        '/shadow/update/#')
    print("payload = " + payload)
    print("responseStatus = " + responseStatus)
    print("token = " + token)


# Create, configure, and connect a shadow client.
myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()


# Create a programmatic representation of the shadow.
myDeviceShadow = myShadowClient.createShadowHandlerWithName(
    SHADOW_HANDLER, True)


sensor = Adafruit_DHT.DHT11
pin = 17

while True:
    
    # Collecting data from sensor
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    myDeviceShadow.shadowUpdate(
       '{"state":{"reported":{"Temperature":' + str(temp) +
       ', "Humidity":' + str(hum) + '}}}',
      myShadowUpdateCallback, 5)
    #print("\n")
    """
    myDeviceShadow.shadowUpdate(
       '{"state":{"reported":{"Humidity":' + str(hum) + '}}}',
      myShadowUpdateCallback, 5)
      """
    # Print statements
    print("\nThe temperature is " + str(temp) + "C, with a humidity of " + str(hum) + "%")
    time.sleep(20)
