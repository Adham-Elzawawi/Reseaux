import matplotlib.pyplot as plt
import numpy as np

# Your dataset
ethernet_tcp, ethernet_udp, ethernet_quic = [1237, 333, 249, 19397, 465], [39, 23, 4, 20, 16], [28, 0, 0, 0, 0]
wifi_tcp, wifi_udp, wifi_quic = [1303, 517, 158, 15995, 751], [13, 182, 75, 588, 43], [13, 5, 33, 17, 19]

# Define colors for each protocol
colors = {  'wifi_TCP': '#4287f5', 
            'ethernet_TCP': '#254c8a',
            'wifi_UDP': '#bc4ddb', 
            'ethernet_UDP': '#8e3aa6',
            'wifi_QUIC': '#44cf62',
            'ethernet_QUIC': '#2d8740'
          }

# Number of scenarios
n = len(ethernet_tcp)
index = np.arange(n)
bar_width = 0.35

# Create subplots
fig, ax = plt.subplots(figsize=(15, 8))

# Stacked bar graph for Ethernet
ethernet_tcp_bar = ax.bar(index - bar_width/2, ethernet_tcp, bar_width, label='Ethernet TCP', color=colors['ethernet_TCP'])
ethernet_udp_bar = ax.bar(index - bar_width/2, ethernet_udp, bar_width, bottom=ethernet_tcp, label='Ethernet UDP', color=colors['ethernet_UDP'])
ethernet_quic_bar = ax.bar(index - bar_width/2, ethernet_quic, bar_width, bottom=np.array(ethernet_tcp) + np.array(ethernet_udp), label='Ethernet QUIC', color=colors['ethernet_QUIC'])

# Stacked bar graph for WiFi
wifi_tcp_bar = ax.bar(index + bar_width/2, wifi_tcp, bar_width, label='WiFi TCP', color=colors['wifi_TCP'])
wifi_udp_bar = ax.bar(index + bar_width/2, wifi_udp, bar_width, bottom=wifi_tcp, label='WiFi UDP', color=colors['wifi_UDP'])
wifi_quic_bar = ax.bar(index + bar_width/2, wifi_quic, bar_width, bottom=np.array(wifi_tcp) + np.array(wifi_udp), label='WiFi QUIC', color=colors['wifi_QUIC'])

# Set the y-axis to a logarithmic scale
ax.set_yscale('log')
ax.set_ylim(1, 10**5)

# Add labels and title
ax.set_xlabel('Scenario')
ax.set_ylabel('Number of Packets (Log Scale)')
ax.set_title('Transport Protocol Usage by Scenario and Connection Type')
ax.set_xticks(index)
ax.set_xticklabels(['Site Launch', 'File Upload', 'File Delete', 'File Modif', 'File Open'])

# Adding a legend
ax.legend()

# Function to add labels on the bars
def autolabel(bars, protocol):
    for bar in bars:
        height = bar.get_height()
        if height > 50:  # Only label bars with height > 1 to avoid clutter
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',
                        fontsize=8, color='black', fontweight='bold')

# Apply autolabel to each set of bars
autolabel(ethernet_tcp_bar, 'TCP')
autolabel(ethernet_udp_bar, 'UDP')
autolabel(ethernet_quic_bar, 'QUIC')
autolabel(wifi_tcp_bar, 'TCP')
autolabel(wifi_udp_bar, 'UDP')
autolabel(wifi_quic_bar, 'QUIC')

# Show plot with tight layout
plt.tight_layout()
plt.show()
