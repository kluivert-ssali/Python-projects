import tkinter as tk
import requests
import platform

# Function to get the external IP address
def get_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        ip = response.json()["ip"]
        return ip
    except Exception as e:
        return f"Error: {e}"

# Function to get device information
def get_device_info():
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    return f"System: {system}\nNode: {node}\nRelease: {release}\nVersion: {version}\nMachine: {machine}\nProcessor: {processor}"

# Function to update the display with IP and device info
def display_info():
    ip_address = get_ip()
    device_info = get_device_info()
    ip_label.config(text=f"IP Address: {ip_address}")
    device_info_label.config(text=f"Device Info:\n{device_info}")

# Create the GUI window
root = tk.Tk()
root.title("IP and Device Info")

# Set window size
root.geometry("400x300")

# Create and place labels
ip_label = tk.Label(root, text="IP Address: Loading...", font=("Arial", 12))
ip_label.pack(pady=10)

device_info_label = tk.Label(root, text="Device Info: Loading...", font=("Arial", 10), justify=tk.LEFT)
device_info_label.pack(pady=10)

# Create and place a button to refresh info
refresh_button = tk.Button(root, text="Refresh Info", command=display_info)
refresh_button.pack(pady=20)

# Initial display of IP and device info
display_info()

# Start the GUI event loop
root.mainloop()