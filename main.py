import uasyncio as asyncio
import machine, sys, wifimgr, time, ujson, trickLED, effects
from trickLED import animations, generators, animations32
from web_page import web_page

COLOR_PROFILE = "colors.json"

def read_color_profiles():
    with open(COLOR_PROFILE) as f:
        return ujson.load(f)  

def write_color_profiles(colors):
    with open(COLOR_PROFILE, "w") as f:
        f.write(ujson.dumps(colors))

def qs_parse(qs):
    """return parameters parsed from URL snippet as dict"""
    parameters = {}
    ampersandSplit = qs.split("&")
    for element in ampersandSplit:
        equalSplit = element.split("=")
        print(equalSplit)
        parameters[equalSplit[0]] = equalSplit[1]
    return parameters

def parse_get(request):
    """Parse GET URL for config data"""
    data = request.split(" ")
    for d in data:
        if d.startswith("/colors?"):
            parsed = qs_parse(d[8:])
            print("Updated color profile to ", colors)
            return parsed
        if d.startswith("/effects?"):
            parsed = qs_parse(d[9:])
            print("Updated effect to ", parsed)
            return parsed

def main():
    # pixel setup
    p = 12
    n = 58
    pin = machine.Pin(12, machine.Pin.OUT)
    leds = trickLED.TrickLED(pin, n, timing=1)
    leds.repeat_n = 29
    leds.repeat_mode = leds.REPEAT_MODE_MIRROR
    
    # set the default color profile
    try:
        colors = read_color_profiles()
    except:
        print(f"Could not load {COLOR_PROFILE}. Continue with default settings.")
        colors = {"r":1,"g":1,"b":1, "br":10, "effect":"solid_color"}
    print(colors)
    
    # the wifi setup
    # connect to known wifi (wifi.dat) or connect to new wifi via web interface
    try:
        import usocket as socket
    except:
        import socket

    wlan = wifimgr.get_connection()
    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            pass  # you shall not pass :D
    print("ESP OK")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', 80))
        s.listen(5)
    except OSError as e:
        machine.reset()
    
    # the main loop
    # wait for request from a client and parse forms to update LED settings. respond with updated html
    while True:
        try:
            if gc.mem_free() < 102000:
                  gc.collect()
            conn, addr = s.accept()
            conn.settimeout(3.0)
            print(f'Got a connection from {addr}')
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            
            colors.update(parse_get(request))
            effects.run(leds, colors)
            
            response = web_page(colors)
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
        except OSError as e:
            conn.close()
            print('Connection closed')
        
if __name__ == '__main__':
    main()    