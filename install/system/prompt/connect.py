# connect.py
import os

def change_ip(ip_address, subnet_mask, gateway):
    try:
        # تغییر آیپی برای سیستم‌های Unix-like
        command = f"sudo ifconfig eth0 {ip_address} netmask {subnet_mask} up"
        os.system(command)
        
        # تنظیم دروازه (gateway)
        command = f"sudo route add default gw {gateway}"
        os.system(command)
        
        print(f"IP address changed to {ip_address} with subnet mask {subnet_mask} and gateway {gateway}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_address = input("Enter the new IP address: ")
    subnet_mask = input("Enter the subnet mask: ")
    gateway = input("Enter the gateway: ")
    change_ip(ip_address, subnet_mask, gateway)