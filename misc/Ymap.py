import argparse
import socket

# Function to scan a specific port
def scan_port(target, port, protocol):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, protocol)
        sock.settimeout(1)  # Set the timeout for socket connection

        # Attempt to connect to the target on the specified port
        result = sock.connect_ex((target, port))
        if result == 0:
            # Port is open
            print(f"Port {port} is open")
            try:
                # Try to get the service name if available
                service = socket.getservbyport(port, str(protocol))
                print(f"Service: {service}")
            except socket.error:
                # Service name not available
                print("Service: Unknown")
        else:
            # Port is closed or filtered
            print(f"Port {port} is closed or filtered")

        sock.close()  # Close the socket connection

    except socket.error as e:
        print(f"Error: {e}")


# Function to scan a range of ports
def scan_ports(target, start_port, end_port, protocol):
    print(f"Scanning ports {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port, protocol)


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="PyScan - Port Scanning Tool")

    # Add the target argument
    parser.add_argument("target", help="Target IP address or hostname")

    # Add the protocol argument
    parser.add_argument(
        "-p",
        "--protocol",
        choices=["tcp", "udp", "both"],
        default="both",
        help="Protocol to use for scanning (default: both)",
    )

    # Add the port range arguments
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="Start port for scanning (default: 1)",
    )
    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=65535,
        help="End port for scanning (default: 65535)",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert the target to IP address if it's a hostname
    target = socket.gethostbyname(args.target)

    # Determine the protocol(s) to use
    if args.protocol == "tcp":
        protocols = [socket.SOCK_STREAM]
    elif args.protocol == "udp":
        protocols = [socket.SOCK_DGRAM]
    else:
        protocols = [socket.SOCK_STREAM, socket.SOCK_DGRAM]

    # Scan the ports
    for protocol in protocols:
        scan_ports(target, args.start, args.end, protocol)


if __name__ == "__main__":
    main()
