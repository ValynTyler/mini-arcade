#!/usr/bin/env python3

import os
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from qrcode import QRCode


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    ip = s.getsockname()[0]
    return ip


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(os.path.join(path, 'public'))

    ip = get_ip()
    port = 8080
    addr = f"http://{ip}:{port}"

    qr = QRCode(border=1)
    qr.add_data(addr)
    qr.make(fit=True)

    qr.print_ascii()
    
    print(f"Opening server at {addr}")
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)

    try:
        httpd.serve_forever()
    except:
        httpd.server_close()

    print("\nClosing server...")


if __name__ == "__main__":
    main()
