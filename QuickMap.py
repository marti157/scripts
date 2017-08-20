#!/usr/bin/env python

"""QuickMap - A simple host scanner
By Marti157"""

import socket
import sys

try:
    print "\nQuickMap v1.0 beta\n\nInput target IP.\n"
    scanTarget = raw_input("Target IP: ")
    scanTarget = str(scanTarget)
    targetIP  = socket.gethostbyname(scanTarget)
    targetCheck = list(scanTarget)
    targetLength = len(scanTarget)

    if '.' not in targetCheck:
        print "\nError: invalid IP"
        sys.exit()
    else:
        print "\nChoose scan protocol (only TCP atm):\n(Input number)\n\n[1] TCP\n[2] UDP\n"
        scanProtocol = input("Protocol: ")
        scanProtocol = str(scanProtocol)
        if scanProtocol == "1":
            print "\nChoose scan type:\n(Input number)\n\n[1] Quick Scan (Ports 1 - 100)\n[2] Normal Scan (Ports 1 - 1,000)\n[3] Deep Scan (Ports 1 - 100,000)\n"
            scanType = input("Type: ")
            scanType = str(scanType)
            if scanType == "1" or scanType == "2" or scanType == "3":
                print "\nStarting QuickMap scan. This may take a while.\n"
                if scanType == "1":
                    try:
                        for port in range(1,101):
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = sock.connect_ex((targetIP, port))
                            if result == 0:
                                print "Port {}: 	 Open".format(port)
                                sock.close()
                    except socket.gaierror:
                        print 'Hostname could not be resolved. Stopping...'
                        sys.exit()
                    except socket.error:
                        print "Couldn't connect to server. Stopping..."
                        sys.exit()
                elif scanType == "2":
                    try:
                        for port in range(1,1001):
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = sock.connect_ex((targetIP, port))
                            if result == 0:
                                print "Port {}: 	 Open".format(port)
                                sock.close()
                    except socket.gaierror:
                        print 'Hostname could not be resolved. Stopping...'
                        sys.exit()
                    except socket.error:
                        print "Couldn't connect to server. Stopping..."
                        sys.exit()
                else:
                    try:
                        for port in range(1,100001):
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = sock.connect_ex((targetIP, port))
                            if result == 0:
                                print "Port {}: 	 Open".format(port)
                                sock.close()
                                print "\n"
                    except socket.gaierror:
                        print 'Hostname could not be resolved. Stopping...'
                        sys.exit()
                    except socket.error:
                        print "Couldn't connect to server. Stopping..."
                        sys.exit()
except KeyboardInterrupt:
   print "Stopping..."
   sys.exit()
