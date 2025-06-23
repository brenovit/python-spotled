#!/usr/bin/env python3

import sys
import time
sys.path.insert(0, './')

try:
    import spotled
    print("Spotled library imported successfully")
    
    if len(sys.argv) < 2:
        print("Usage: python3 test_spotled.py <MAC_ADDRESS>")
        sys.exit(1)
    
    mac_address = sys.argv[1]
    print(f"Attempting to connect to device: {mac_address}")
    
    # Try creating connection with shorter timeout
    sender = spotled.LedConnection(mac_address)
    print("Connection established!")
    
    # Try to set basic text
    print("Sending 'Hello World!' to the device...")
    sender.set_text('Hello World!')
    print("Text sent successfully!")
    
    # Try setting brightness
    print("Setting brightness to 50...")
    sender.set_brightness(50)
    print("Brightness set successfully!")
    
except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e).__name__}")
