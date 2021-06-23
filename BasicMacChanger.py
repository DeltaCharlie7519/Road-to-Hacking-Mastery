import subprocess
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 11:22:33:44:55:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)