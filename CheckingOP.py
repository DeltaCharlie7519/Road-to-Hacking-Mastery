import subprocess
import optparse


def mac_changer(interface, mac_add):
    print(subprocess.call("ifconfig " + str(interface) + " down", shell=True))


    print(subprocess.call("ifconfig " + str(interface) + " hw ether " + str(mac_add), shell=True))

    print(subprocess.call("ifconfig " + str(interface) + " up", shell=True))
    return None


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="new_interface", help="Selects Interface")
    parser.add_option("-m", "--MAC", dest="new_mac", help="Changes the Mac Address")
    (info, arguments) = parser.parse_args()
    if not info.new_interface:
        parser.error("No interface specified")
    elif not info.new_mac:
        parser.error("No Mac address found in command line")

    return info


options = get_args()
#mac_changer(options.new_interface, options.new_mac)
ifconfig_result = subprocess.check_output(["ifconfig", options.new_interface])
print(ifconfig_result)

