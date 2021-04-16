from customparser import CustomParsers
from genie.conf import Genie
import pprint

parser = CustomParsers()


testbed = Genie.init("./iosxe_testbed.yaml")

for device in testbed.devices:
    # Connect to the device
    print(f' Connecting to Device: {device}')
    testbed.devices[device].connect()
    
    output=testbed.devices[device].execute('show service-routing database')
    output = output.replace('\r\n','\n')
    
    result=parser.showservdatabase(device_name=device,output=output,yaml_out=f'./show_service_routing_{device}.yaml')
    pprint.pprint(result, width=2)
    