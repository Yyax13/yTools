import socket


def get_service_name(port, protocol):
    try:
        service = socket.getservbyport(port, protocol)
        return service
    except socket.error:
        return "Unknown"


def generate_report(ports):
    print("Port Scan Report:")
    print("=================")
    for port, service in ports.items():
        print(f"Port: {port}")
        print(f"Service: {service}")
        print("-----------------")
