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
    os.chdir('./public')

    ip = get_ip()
    port = 8080
    addr = f"http://{ip}:{port}"

    qr = QRCode(border=1)
    qr.add_data(addr)
    qr.make(fit=True)

    print(f"Server open at {addr}")
    qr.print_ascii()
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
