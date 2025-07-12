import socket
import argparse

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(f"Port {port} is OPEN ({service})")
            s.close()
        except KeyboardInterrupt:
            print("\nScan aborted by user.")
            break
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
        scan_ports(target_ip, args.start, args.end)
    except socket.gaierror:
        print("Could not resolve hostname.")
