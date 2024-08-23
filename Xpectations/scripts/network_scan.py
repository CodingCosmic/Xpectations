import pyshark
from core.log import setup_logging, log_message
from core.shellcode import ShellcodeDetector
from core.report import generate_report

def analyze_network_traffic(pcap_path):
    setup_logging()
    log_message(f"Starting network traffic analysis on {pcap_path}")

    packets = pyshark.FileCapture(pcap_path)
    suspicious_packets = []

    for packet in packets:
        if 'DATA' in packet:
            raw_data = bytes.fromhex(packet['DATA'].data.replace(':', ''))
            shellcode_detector = ShellcodeDetector(raw_data)
            if shellcode_detector.detect_shellcode():
                suspicious_packets.append(packet)

    report = generate_report([str(pkt) for pkt in suspicious_packets])
    report_file = f"{pcap_path}_network_report.json"
    with open(report_file, 'w') as rf:
        rf.write(report)

    log_message(f"Network traffic analysis complete. Report saved to {report_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python network_scan.py <path_to_pcap_file>")
        sys.exit(1)
    analyze_network_traffic(sys.argv[1])
