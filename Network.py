
import subprocess
import platform
import time

App_Server = '10.124.16.101'
DB_Server = '10.124.76.103'
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
    
    hosts_to_ping = [App_Server, DB_Server, 'silcal.lotuswireless.com']
    while True:
        for host_to_ping in hosts_to_ping:
            if ping_host(host_to_ping):
                print(f"Connection to {host_to_ping} is successful.")
            else:
                print(f"Connection to {host_to_ping} failed. Check your network connection.")

       
        time.sleep(60)

if __name__ == "__main__":
    main()
