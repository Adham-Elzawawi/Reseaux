import pyshark
import matplotlib.pyplot as plt

ethernet_paths = [
    '../Ethernet/site_launch.pcap',
    '../Ethernet/file_upload.pcap',
    '../Ethernet/file_delete.pcap',
    '../Ethernet/file_modif.pcap',
    '../Ethernet/file_open.pcap',
]

wifi_paths = [
    '../Wifi/site_launch.pcap',
    '../Wifi/file_upload.pcap',
    '../Wifi/file_delete.pcap',
    '../Wifi/file_modif.pcap',
    '../Wifi/file_open.pcap',
]

def count_dns_packets(paths):
    dns_packets = []
    for path in paths:
        capture = pyshark.FileCapture(path, display_filter='dns')
        dns_packets.append(len(list(capture)))
    return dns_packets

# Count DNS packets for Ethernet and Wi-Fi
ethernet_dns_packets = count_dns_packets(ethernet_paths)
wifi_dns_packets = count_dns_packets(wifi_paths)

# Plotting
activities = ['Site Launch', 'File Upload', 'File Delete', 'File Modif', 'File Open']
plt.figure(figsize=(10, 6))
plt.bar(activities, ethernet_dns_packets, width=0.4, label='Ethernet', align='center')
plt.bar(activities, wifi_dns_packets, width=0.4, label='WiFi', align='edge')
plt.ylabel('Number of DNS Packets')
plt.title('DNS Packet Counts by Activity and Connection Type')

plt.legend()
#plt.show()

plt.savefig('dns_packets.png')