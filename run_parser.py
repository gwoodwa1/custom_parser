from custom_parser import custom_parsers
import pprint

parser = custom_parsers()

device_name = "R1"

output = """
R1#  show service-routing database
Service-Routing Database
Service ID (Service:Subservice:Instance)         Trust     Domain Owner Size
------------------------------------------------ --------- ------ ----- -----
      100:1:31000000-0000-0000-0000-520000000000 Connected *      1       392
      100:2:31000000-0000-0000-0000-520000000000 Connected *      1      1074
      101:2:675952D8-B2F9-38A8-AE06-8CE5000160D1 Connected 1      2       565
      101:2:933EF17C-54BA-5610-0325-B23200019D2E Connected 1      4       387
      102:2:933EF17C-54BA-5610-0325-B23200019D2E Connected 1      4       387
"""

result = parser.show_serv_database(
    device_name=device_name,
    output=output,
    yaml_out=f"./show_service_routing_{device_name}.yml",
)
pprint.pprint(result, width=20)
