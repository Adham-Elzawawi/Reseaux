import pyshark
import matplotlib.pyplot as plt
import numpy as np

# Define paths to the pcap files
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

# Define a function to count the transport protocols
def count_protocols(paths):
    tcp_counts = []
    udp_counts = []
    quic_counts = []
    for path in paths:
        # Initialize counters for each file
        tcp = 0
        udp = 0
        quic = 0
        
        # Read the pcap file
        cap = pyshark.FileCapture(path, only_summaries=False, display_filter="tcp || udp || quic")
        
        # Count the occurrences of each transport protocol
        for packet in cap:
            if 'TCP' in packet:
                tcp += 1
            if 'UDP' in packet:
                udp += 1
            if 'QUIC' in packet:
                quic += 1
            
        
        # Store the results
        tcp_counts.append(tcp)
        udp_counts.append(udp)
        quic_counts.append(quic)
        
        # Close the capture file to free resources
        cap.close()
        
    return tcp_counts, udp_counts, quic_counts

# Calculate the protocol counts for Ethernet and WiFi
#ethernet_tcp, ethernet_udp, ethernet_quic = count_protocols(ethernet_paths)
#wifi_tcp, wifi_udp, wifi_quic = count_protocols(wifi_paths)

# pre-calculated values for the transport protocols
ethernet_tcp, ethernet_udp, ethernet_quic = [1237, 333, 249, 19397, 465], [39, 23, 4, 20, 16], [28, 0, 0, 0, 0]
wifi_tcp, wifi_udp, wifi_quic = [1303, 517, 158, 15995, 751], [13, 182, 75, 588, 43], [13, 5, 33, 17, 19]

# Define the label locations and the width of the bars
n = len(ethernet_paths)  # Number of scenarios
index = np.arange(n)
bar_width = 0.35

# Plotting
fig, ax = plt.subplots(figsize=(15, 8))

# Stacked bar graph for Ethernet
ethernet_tcp_bar = ax.bar(index - bar_width/2, ethernet_tcp, bar_width, label='Ethernet TCP')
ethernet_udp_bar = ax.bar(index - bar_width/2, ethernet_udp, bar_width, bottom=np.array(ethernet_tcp), label='Ethernet UDP')
ethernet_quic_bar = ax.bar(index - bar_width/2, ethernet_quic, bar_width, bottom=np.array(ethernet_tcp) + np.array(ethernet_udp), label='Ethernet QUIC')

# Stacked bar graph for WiFi
wifi_tcp_bar = ax.bar(index + bar_width/2, wifi_tcp, bar_width, label='WiFi TCP')
wifi_udp_bar = ax.bar(index + bar_width/2, wifi_udp, bar_width, bottom=np.array(wifi_tcp), label='WiFi UDP')
wifi_quic_bar = ax.bar(index + bar_width/2, wifi_quic, bar_width, bottom=np.array(wifi_tcp) + np.array(wifi_udp), label='WiFi QUIC')

# Set the y-axis to a logarithmic scale
ax.set_yscale('log')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Scenario')
ax.set_ylabel('Number of Packets')
ax.set_title('Transport Protocol Usage by Scenario and Connection Type')
ax.set_xticks(index)
ax.set_xticklabels(['Site Launch', 'File Upload', 'File Delete', 'File Modif', 'File Open'])
ax.legend(loc='upper left')

def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(ethernet_tcp_bar)
autolabel(ethernet_udp_bar)
autolabel(ethernet_quic_bar)
autolabel(wifi_tcp_bar)
autolabel(wifi_udp_bar)
autolabel(wifi_quic_bar)

#plt.tight_layout()
plt.show()
