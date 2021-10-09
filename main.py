from machine import Pin
import machine, neopixel, wifimgr, time, ujson


try:
    import usocket as socket
except:
    import socket

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

def read_color_profiles():
    with open(COLOR_PROFILE) as f:
        return ujson.load(f)  

def write_color_profiles(colors):
    with open(COLOR_PROFILE, "w") as f:
        f.write(ujson.dumps(colors))

def web_page(colors):
    #the html file that is served. Formatted with persisted rgb values.
    return '''<!DOCTYPE html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
            <form action="/colors" method="GET">
            <h1>Light Panel Control</h1>  
            <h2>Hue:</h2>
                <div class="slidecontainer">
                <label for="rSlider">R:</label>
                <input type="range" id="rSlider" name="red" min="0" max="255" value="1">
                <output class="rOutput" for="rSlider" id="rOutput"></output>
            </div>
            <div class="slidecontainer">
                <label for="gSlider">G:</label>
                <input type="range" id="gSlider" name="green" min="0" max="255" value="1">
                <output class="gOutput" for="gSlider" id="gOutput"></output>
            </div>
            <div class="slidecontainer">
                <label for="bSlider">B:</label>
                <input type="range" id="bSlider" name="blue" min="0" max="255" value="1">
                <output class="bOutput" for="bSlider" id="bOutput"></output>
            </div>
            <h2>Brightness:</h2>
            <div class="slidecontainer">
                <label for="brSlider">B:</label>
                <input type="range" id="brSlider" name="bright" min="0" max="255" value="10">
                <output class="brOutput" for="brSlider" id="brOutput"></output>
            </div>
                <Button type="submit">POST</Button>
            </form>
          
            <script>
                const rSlider = document.querySelector('#rSlider');
                const rOutput = document.querySelector('.rOutput');
                const gSlider = document.querySelector('#gSlider');
                const gOutput = document.querySelector('.gOutput');
                const bSlider = document.querySelector('#bSlider');
                const bOutput = document.querySelector('.bOutput');
                const brSlider = document.querySelector('#brSlider');
                const brOutput = document.querySelector('.brOutput');

                rOutput.textContent = rSlider.value;
                gOutput.textContent = gSlider.value;
                bOutput.textContent = bSlider.value;
                brOutput.textContent = brSlider.value;

                rSlider.addEventListener('input', function() {
                      rOutput.textContent = this.value;
                });
                gSlider.addEventListener('input', function() {
                      gOutput.textContent = this.value;
                });
                bSlider.addEventListener('input', function() {
                      bOutput.textContent = this.value;
                });
                brSlider.addEventListener('input', function() {
                      brOutput.textContent = this.value;
                });
            </script>

            </body>
            </html>'''

# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

#set the default color profile
COLOR_PROFILE = "colors.json"
#try:
colors = read_color_profiles()
#except:
#    print(f"Could not load {COLOR_PROFILE}. Continue with default settings.")
#    colors = {"r":1,"g":1,"b":1, "br":10}
print(colors)

#pixel setup
p = 12
n = 58
pin = Pin(12, Pin.OUT)
np=neopixel.NeoPixel(pin, n)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 80))
    s.listen(5)
except OSError as e:
    machine.reset()

def qs_parse(qs):
    parameters = {}
    ampersandSplit = qs.split("&")
    for element in ampersandSplit:
        equalSplit = element.split("=")
        parameters[equalSplit[0]] = equalSplit[1]
    return parameters

#the main loop
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
        print(f'Content = {request}')
        if request.find("/colors?"):
            data = request.split(",")
            for d in data:
                if d.startswith("/colors?"):
                    qs_parse(d)
        
        response = web_page(colors)
        write_color_profiles(colors)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')