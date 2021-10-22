from trickLED import animations, animations32, generators, trickLED
from random import randint
from math import floor
import uasyncio as asyncio

# ANIMATIONS
def solid_color(leds, colors):
    ani = animations.SolidColor(leds, colors)
    return ani
            
def lit_bits(leds, lit_percent=50):
    ani = animations.LitBits(leds, lit_percent=lit_percent)
    print('LitBits settings: lit_percent={}'.format(lit_percent))
    return ani
    
def next_gen(leds, blanks=2, interval=150):
    ani = animations.NextGen(leds, blanks=blanks, interval=blanks)
    print('NextGen settings: blanks={}, interval={}'.format(blanks, interval))
    return ani
    
def jitter(leds, background=0x020212, fill_mode=trickLED.FILL_MODE_SOLID):
    ani = animations.Jitter(leds, background=background, fill_mode=fill_mode)
    print('Jitter settings: default')
    return ani
    
def side_swipe(leds, **kwargs):
    ani = animations.SideSwipe(leds)
    print('SideSwipe settings: default')
    return ani

def divergent(leds, fill_mode=trickLED.FILL_MODE_MULTI):
    ani = animations.Divergent(leds, fill_mode=fill_mode)
    print('Divergent settings: default')
    return ani

def convergent(leds, fill_mode=trickLED.FILL_MODE_MULTI):
    ani = animations.Convergent(leds, fill_mode=fill_mode)
    print('Convergent settings: default')
    return ani

def fire(leds):
    ani = animations32.Fire(leds)
    print('Fire settings: default')
    return ani

def conjuction(leds):
    ani = animations32.Conjunction(leds)
    print('Conjuction settings: default')
    return ani

# GENERATORS
def stepped_color_wheel(leds):  
    print('stepped_color_wheel')
    ani = animations.NextGen(leds, generator = generators.stepped_color_wheel())
    return ani
    
def striped_color_wheel(leds, stripe_size=1):
    print('stepped_color_wheel(stripe_size={})'.format(stripe_size))
    ani = animations.NextGen(leds, generator = generators.striped_color_wheel(stripe_size=stripe_size))
    return ani
    
def fading_color_wheel(leds, mode=trickLED.FADE_OUT):
    print('fading_color_wheel(mode={})'.format(mode))
    ani = animations.NextGen(leds, generator = generators.fading_color_wheel(mode=mode))
    return ani
    
def color_compliment(leds):
    print('color_compliment()')
    ani = animations.NextGen(leds, generator = generators.color_compliment(stripe_size=10))
    return ani
    
def random_vivid(leds):
    print('random_vivid()')
    ani = animations.NextGen(leds, generator = generators.random_vivid())
    return ani
    
def random_pastel(leds, mask=(randint(0,254),randint(0,254),randint(0,254))):
    print('random_pastel(mask={})'.format(mask))
    ani = animations.NextGen(leds, generator = generators.random_pastel(mask=mask))
    return ani

def get_animation(leds, colors,  **kwargs):
    animation = colors['effect']
    if animation == "solid_color":
        return solid_color(leds, colors)
    elif animation == "lit_bits":
        return lit_bits(leds, lit_percent=50)
    elif animation == "next_gen":
        return next_gen(leds,  blanks=2, interval=150)
    elif animation == "jitter":
        return jitter(leds, background=0x020212, fill_mode=trickLED.FILL_MODE_SOLID)
    elif animation == "side_swipe":
        return side_swipe(leds)
    elif animation == "divergent":
        return divergent(leds)
    elif animation == "convergent":
        return convergent(leds)
    elif animation == "fire":
        return fire(leds)
    elif animation == "conjunction":
        return conjuction(leds)
    elif animation == "stepped_color_wheel":
        return stepped_color_wheel(leds)
    elif animation == "striped_color_wheel":
        return striped_color_wheel(leds)
    elif animation == "fading_color_wheel":
        return fading_color_wheel(leds)
    elif animation == "color_compliment":
        return color_compliment(leds)
    elif animation == "random_vivid":
        return random_vivid(leds)
    elif animation == "random_pastel":
        return random_pastel(leds)
