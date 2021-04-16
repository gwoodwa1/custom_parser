import re
import yaml

# =============================================#
#                                              #
#  Bespoke Parsers returning structured data : #
#                                              #
#  - Python Dictionary                         #
#  - YAML File                                 #
#                                              #
#                                              #
# =============================================#


class CustomParsers:
    
    def showservdatabase(self, output=None, device_name=None, yaml_out=None):
    
        result = output

        self.output_dict = {}

        # 100:1:31000000-0000-0000-0000-520000000000 Connected *      1       392

        pat1 = re.compile(
            r"(?P<service>\d+):(?P<sub_service>\d+):(?P<instance>\S+)\s+(?P<trust>\w+)\s+(?P<domain>\S+)\s+(?P<owner>\d+)\s+(?P<size>\d+)"
        )

        index = 0

        for line in result.splitlines():

            if line:
                line = line.strip()

            else:
                continue

            match_pattern = pat1.match(line)

            if match_pattern:
                index = index + 1
                group = match_pattern.groupdict()
                
                temp_dict = (
                    self.output_dict.setdefault("hostname", {})
                    .setdefault(device_name, {})
                    .setdefault("index", {})
                    .setdefault(index, {})
                )
                if group['service'] and group['service'].isdigit():
                    temp_dict.update({"service_id": int(group["service"])})
                if group['sub_service'] and group['service'].isdigit():
                    temp_dict.update({"sub_service": int(group["sub_service"])})
                
                
                temp_dict.update({"instance": group["instance"]})
                temp_dict.update({"trust": group["trust"]})
                temp_dict.update({"domain": group["domain"]})
                if group['owner'] and group['owner'].isdigit():
                    temp_dict.update({"owner": int(group["owner"])})
                if group['size'] and group['size'].isdigit():
                   temp_dict.update({"size": int(group["size"])})
                
        if yaml_out:
            
            CustomParsers().yamlwriter(yaml_out=yaml_out, input_dict=self.output_dict)

        return self.output_dict

    def yamlwriter(self, yaml_out=None, input_dict=None):

        with open(f'{yaml_out}', "w") as file:
            
            yaml.dump(input_dict, file, allow_unicode=True)
        
