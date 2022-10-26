from pprint import pprint
import yaml


to_yaml = {
   'access': ['switchport mode access',
              'switchport access vlan',
              'switchport nonegotiate',
              'spanning-tree portfast',
              'spanning-tree bpduguard enable'],
   'trunk': ['switchport trunk encapsulation dot1q',
             'switchport mode trunk',
             'switchport trunk native vlan 999',
             'switchport trunk allowed vlan'],
}

with open("yaml_files/result_15.yaml", "w") as f:
    yaml.dump(to_yaml, f, default_flow_style=False, explicit_start=True)

