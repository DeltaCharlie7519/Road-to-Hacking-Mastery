import subprocess
import optparse
parser = optparse.OptionParser()
parser.add_option() = ("-m","--MAC", dest = "new_mac", help = "Changes the Mac Address")
(options,arguments) = parser.parse_args()
new_mac = options.new_mac
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether " + new_mac, shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
