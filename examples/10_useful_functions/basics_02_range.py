from sys import argv

def convert_macs(mac_list):
    result = []
    for mac_result in mac_list:
        if ":" in mac_result:
            mac_parts = mac_result.split(":")
            new_mac = ["".join(mac_parts[i:i+2]) for i in range(0, 6, 2)]
            result.append(".".join(new_mac))
    return result


macs_argv = argv[1:]
print("ARGV", macs_argv)
print("RESULT", convert_macs(macs_argv))
