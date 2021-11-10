import machine, sys, time, wifimgr, ujson, trickLED, picoweb, effects, gc

import uasyncio as asyncio
from web_page import web_page

gc.enable()

req = bytearray(4096)
COLOR_PROFILE = "colors.json"

def read_color_profiles():
    with open(COLOR_PROFILE) as f:
        return ujson.load(f)

def write_color_profiles(colors):
    with open(COLOR_PROFILE, "w") as f:
        f.write(ujson.dumps(colors))
        print("Profile updated to ", colors)

# MAIN SCRIPT
wlan = wifimgr.get_connection()
if wlan is None:
    while True:
        pass
app_host = wlan.ifconfig()[0]
app_port=const(80)

# pixel setup
p = const(12)
n = const(58)
leds = trickLED.TrickLED(machine.Pin(p, machine.Pin.OUT), n, timing=1)

def get_default_colors():
    return {"r":100,"g":100,"b":100, "br":20, "effect":"solid_color", "generator":None}

try:
    colors = read_color_profiles()
    print(f"Colors loaded successfully: {colors}")
except:
    print(f"Could not load {COLOR_PROFILE}. Continue with default settings.")
    colors = get_default_colors()

task = asyncio.create_task(effects.get_animation(leds, colors).play())

def get_task():
    return task

def set_task(t):
    global task
    task = t

def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    yield from picoweb.start_response(resp, content_type = "text/html")
    gc.collect()
    colors.update(req.form)
    write_color_profiles(colors)
    get_task().cancel()
    set_task(asyncio.create_task(effects.get_animation(leds, colors).play()))
    for i in range(0, 8):
        yield from resp.awrite(web_page(colors, i))

ROUTES = [
    ("/", index),
]

# lastly, run the web server
app = picoweb.WebApp(__name__, ROUTES)
try:
    app.run(debug=1, host=app_host, port=app_port)
finally:
    asyncio.new_event_loop()
    print("Closing event loop")
