
import subprocess
import platform
import time

def ping_host(host):
    try:
        if platform.system().lower() == 'windows':
            subprocess.run(["ping", "-n", "4", host], check=True)
        else:
            subprocess.run(["ping", "-c", "4", host], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    #hosts_to_ping = ['10.145.49.25', '10.145.49.24', '10.145.49.27', 'silcal.lotuswireless.com']
    hosts_to_ping = ['10.100.76.101', '10.100.76.103', 'silcal.lotuswireless.com']
    while True:
        for host_to_ping in hosts_to_ping:
            if ping_host(host_to_ping):
                print(f"Connection to {host_to_ping} is successful.")
            else:
                print(f"Connection to {host_to_ping} failed. Check your network connection.")

        # Adjust the sleep time according to your needs (in seconds)
        time.sleep(60)

if __name__ == "__main__":
    main()
