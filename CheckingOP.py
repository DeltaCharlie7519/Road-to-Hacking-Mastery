import subprocess
import optparse
def mac_changer(mac_add):
    subprocess.call("ifconfig eth0 down", shell=True)
    subprocess.call("ifconfig eth0 hw ether " + str(mac_add), shell=True)
    subprocess.call("ifconfig eth0 up", shell=True)

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-m", "--MAC", dest = "new_mac", help = "Changes the Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.new_mac:
        parser.error("No Mac address found in command line")
    return options

Newmac_add = get_args()
mac_changer(Newmac_add)
ifconfig_result = subprocess.check_output("ifconfig" , Newmac_add.new_mac)
print(ifconfig_result)

