import machine, sys, time, wifimgr, ujson, trickLED, picoweb, effects, gc

import uasyncio as asyncio
from web_page import web_page

gc.enable()

req = bytearray(4096)
COLOR_PROFILE = "colors.json"
c = 0
colors = {}

def write_color_profiles(colors):
    with open(COLOR_PROFILE, "w") as f:
        f.write(ujson.dumps(colors))
        print("Profile updated to ", colors)

def get_colors_from_file():
    with open(COLOR_PROFILE) as f:
        try:
            return ujson.load(f)
            print(f"Colors loaded successfully: {colors}")
        except:
            print(f"Could not load {COLOR_PROFILE}. Continue with default settings.")
            return get_default_colors()

def get_default_colors():
    return {"rgb":0, "effect":"ani_solid_color", "generator":None}


## MAIN SCRIPT
# pixel setup
p = const(12)
n = const(58)
leds = trickLED.TrickLED(machine.Pin(p, machine.Pin.OUT), n, timing=1)

# The running animation task
colors = get_colors_from_file()
task = asyncio.create_task(effects.get_effect(leds, colors).play())

def get_task():
    return task

def set_task(t):
    global task
    task = t

# wifi setup
wlan = wifimgr.get_connection()
if wlan is None:
    while True:
        pass
app_host = wlan.ifconfig()[0]
app_port=const(80)

# Handle HTML request 
def index(req, resp):
    if req.method == "POST":
        yield from req.read_form_data()
    else:  # GET, apparently
        req.parse_qs()
    yield from picoweb.start_response(resp, content_type = "text/html")
    gc.collect()
    global colors
    if req.form:
        colors.update(req.form)
        print(req.form)
        print(colors)
        colors["rgb"] = effects.color_to_int(colors["rgb"]) # save web color code as int 
    get_task().cancel()
    try:
        set_task(asyncio.create_task(effects.get_effect(leds, colors).play()))
        write_color_profiles(colors)
    except Exception as e:
        sys.print_exception(e)
        colors = get_colors_from_file()
        set_task(asyncio.create_task(effects.get_effect(leds, colors).play()))
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
