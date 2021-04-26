from genie.utils import Dq
import yaml
import pprint

device_name = "R1"

with open(f"outputs/show_service_routing_{device_name}.yml") as file:
    output = yaml.load(file, Loader=yaml.FullLoader)


failed_entries = (
    Dq(output).contains("trust").not_contains("Connected").get_values("[3]")
)

failed_dict = {}

for k in failed_entries:
    temp_dict = (
        failed_dict.setdefault("hostname", {})
        .setdefault(device_name, {})
        .setdefault("index", {})
        .setdefault(k, output["hostname"][device_name]["index"][k])
    )

pprint.pprint(failed_dict)

if failed_dict:
    with open(f"outputs/FAILED_show_service_{device_name}.yml", "w") as file:
        yaml.dump(failed_dict, file, allow_unicode=True)
