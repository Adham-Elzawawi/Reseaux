import pyshark
import subprocess
import matplotlib.pyplot as plt

def extract_dns_queries(file_path):
    capture = pyshark.FileCapture(file_path, display_filter='dns')
    domain_names = set()
    for packet in capture:
        try:
            # Check if this is a DNS query
            if hasattr(packet.dns, 'qry_name'):
                domain_names.add(packet.dns.qry_name)
                
                #print(f'Time: {packet.sniff_time}, Domain: {packet.dns.qry_name}')
                
        except AttributeError as e:
            print(f"Error processing packet: {e}")
    print(f'Total unique domain names resolved: {len(domain_names)}')
    return len(domain_names)

def plot_dns_queries(ethernet_dns_queries, wifi_dns_queries):
    fig, ax = plt.subplots()
    bar_width = 0.35
    x = range(len(ethernet_dns_queries))
    
    # Adjusting x-coordinates for side-by-side bars
    x_ethernet = [i - bar_width/2 for i in x]
    x_wifi = [i + bar_width/2 for i in x]
    
    bars1 = ax.bar(x_ethernet, ethernet_dns_queries.values(), bar_width, label='Ethernet')
    bars2 = ax.bar(x_wifi, wifi_dns_queries.values(), bar_width, label='WiFi')
    
    ax.set_xlabel('Action')
    ax.set_ylabel('Number of DNS Queries')
    ax.set_title('Ethernet vs WiFi DNS Queries')
    ax.set_xticks(x)
    ax.set_xticklabels(ethernet_dns_queries.keys())
    ax.legend()
    ax.bar_label(bars1)
    ax.bar_label(bars2)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

ethernet_paths = ['../Ethernet/site_launch.pcap',
                  '../Ethernet/file_upload.pcap',
                  '../Ethernet/file_delete.pcap',
                  '../Ethernet/file_modif.pcap',
                  '../Ethernet/file_open.pcap',
                  ]

wifi_paths = ['../Wifi/site_launch.pcap',
              '../Wifi/file_upload.pcap',
              '../Wifi/file_delete.pcap',
              '../Wifi/file_modif.pcap',
              '../Wifi/file_open.pcap',
              ]

if __name__ == "__main__":
    # Collect DNS queries data for Ethernet
    ethernet_dns_queries = {}
    for path in ethernet_paths:
        action = path.split('/')[-1].split('.')[0].replace('_', ' ').title()
        ethernet_dns_queries[action] = extract_dns_queries(path)
    
    # Collect DNS queries data for WiFi
    wifi_dns_queries = {}
    for path in wifi_paths:
        action = path.split('/')[-1].split('.')[0].replace('_', ' ').title()
        wifi_dns_queries[action] = extract_dns_queries(path)
    
    # Plot DNS queries for Ethernet and WiFi on the same graph
    plot_dns_queries(ethernet_dns_queries, wifi_dns_queries)
