import subprocess
new_mac = input()
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether " + new_mac, shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
