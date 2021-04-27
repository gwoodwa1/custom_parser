from genie.utils import Dq
import yaml
import pprint

device_name = "R1"

with open(f"outputs/show_service_routing_{device_name}.yml") as file:
    output = yaml.load(file, Loader=yaml.FullLoader)

failed_entries = (
    Dq(output)
    .not_contains("Connected", level=-1)
    .contains("trust", level=-1)
    .reconstruct()
)

pprint.pprint(failed_entries)

if failed_entries:
    with open(f"outputs/FAILED_show_service_{device_name}.yml", "w") as file:
        yaml.dump(failed_entries, file, allow_unicode=True)
