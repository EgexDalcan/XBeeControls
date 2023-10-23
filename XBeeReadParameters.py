from digi.xbee.devices import XBeeDevice
from digi.xbee.models.mode import OperatingMode
from digi.xbee.packets.common import ATCommPacket

#Reads all the parameters an XBee device has
inpPort = input("Enter Port:")

#Port of the XBee
port = inpPort

#Openning the XBee
xbee=XBeeDevice(port,9600)
xbee.open(force_settings=True)

#Getting data from XBee
print("Node Identifier:       " + str(xbee.get_node_id()))
print("Mac Address:           " + str(xbee.get_64bit_addr()))
print("XBee Role:             " + str(xbee.get_role()))
print("Destination Address:   " + str(xbee.get_dest_address()))
print("XBee Hardware Version: " + str(xbee.get_hardware_version()))
print("XBee Firmware Version: " + str(xbee.get_firmware_version()))

#Preparing the packet that will make the XBee to go to AT mode
frameno = xbee.get_next_frame_id()
packet = ATCommPacket(frameno, "AP", parameter=bytearray([OperatingMode.AT_MODE.code]))
out = packet.output(False)

#Turning the XBee back to AT mode
xbee.comm_iface.write_frame(out)

xbee.close()