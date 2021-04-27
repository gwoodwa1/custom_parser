from custom_parser import CustomParsers
from genie.conf import Genie
import pprint

parser = CustomParsers()

testbed = Genie.init("../testbeds/genie_testbed.yml")

for device in testbed.devices:
    # Connect to the device
    print(f" Connecting to Device: {device}")
    testbed.devices[device].connect()

    # Fetch raw output
    output = testbed.devices[device].execute("show service-routing database")
    output = output.replace("\r\n", "\n")

    # Return parsed output
    result = parser.show_serv_database(
        device_name=device,
        output=output,
        yaml_out=f"outputs/show_service_routing_{device}.yml",
    )

    pprint.pprint(result, width=2)
