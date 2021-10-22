# PanelLight
Simple Micropython script to control a series of rgb LEDs via html page. Tested to work on ESP32 MCU with Micropython.

## Dependencies 
- wifi manager from here: https://github.com/tayfunulu/WiFiManager
makes connecting the MC to WiFi really easy

- Uses `uasyncio` to listen for web connections 
- Uses `picoweb` to set up the web server and handle requests: https://github.com/pfalcon/picoweb. Connect your device to the network and use `upip.install('picoweb')` for easiest install, or use the provided library. `picoweb` also depends on `micropython-ulogging` module for optional REPL logging and `utemplate`, if you want to use that to format your html. Refer to `picoweb` doumentation.
- Uses `trickLED` library for fastLED-eque micropython LED driving: https://gitlab.com/scottrbailey/trickLED

## Usage
After setting up your microcontroller, picoweb will create a server on the `wifimgr` provided network and serve a config page. Use any device connected to the same network to send requests to the server. It will schedule a task to run the selected animation.

Animations are provided in `animations.py` (and `animations32.py`) and can be customized to taste. They are initialized and retrieved in `effects.py` and then scheduled to run indefinately, until a new reqest is recieved. See `trickLED` library for effect customization.
