from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import ATStringCommand
from digi.xbee.exception import XBeeException
import sys
#Resets the XBee

inpPort = input("Enter Port:")

#Port of the XBee
port = inpPort

#Openning the XBee
xbee=XBeeDevice(port,9600)
xbee.open(force_settings=True)

#Resets the XBee
try:
  xbee.execute_command(ATStringCommand.RE, apply=False)
  xbee.write_changes()
  print("XBee default configuration restored!")
except XBeeException as exc:
  print("Error restoring XBee default configuration: %s" % str(exc))
  sys.exit(1)

try:
  xbee.reset()
except XBeeException as exc:
# This is expected if the previous XBee connection parameters
# are different to the default ones
  print("   [Expected error, proves XBeeReset is successful] Error resetting the XBee: %s" % str(exc))
finally:
  xbee.close()
