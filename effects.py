import trickLED.animations
import trickLED.animations32
import trickLED.generators
import trickLED.trickLED
from random import randint
from math import floor

def play(animation, n_frames, **kwargs):
    asyncio.run(animation.play(n_frames, **kwargs))
    print("play animation")
    
def get_absolute(colors):
    print("abs: ",colors['r'], colors['g'], colors['b'])
    return (int(colors['r']), int(colors['g']), int(colors['b']))

def get_dimmed(colors):
    br = colors['br']
    r = floor(int(colors['r'])*br//100)
    g = floor(int(colors['g'])*br//100)
    b = floor(int(colors['b'])*br//100)
    print("dimmed: ", (r, g, b))
    return (r, g, b)

# ANIMATIONS
def solid_color(leds, colors):
    leds.fill(get_dimmed(colors))
    leds.write()
            
def lit_bits(leds, n_frames=200, lit_percent=50):
    ani = animations.LitBits(leds)
    print('LitBits settings: lit_percent={}'.format(lit_percent))
    play(ani, n_frames, lit_percent=lit_percent)
    
def next_gen(leds, n_frames=200, blanks=2, interval=150):
    ani = animations.NextGen(leds)
    print('NextGen settings: blanks={}, interval={}'.format(blanks, interval))
    play(ani, n_frames, blanks=blanks, interval=blanks)
    
def jitter(leds, n_frames=200, background=0x020212, fill_mode=trickLED.FILL_MODE_SOLID):
    ani = animations.Jitter(leds)
    print('Jitter settings: default')
    play(ani, n_frames, background=background, fill_mode=fill_mode)
#     print('Jitter settings: background=0x020212, fill_mode=FILL_MODE_SOLID')
#     ani.generator = generators.random_vivid()
#     play(ani, n_frames, background=0x020212, fill_mode=trickLED.FILL_MODE_SOLID)
    
def side_swipe(leds, n_frames=200):
    ani = animations.SideSwipe(leds)
    print('SideSwipe settings: default')
    play(ani, n_frames)

def divergent(leds, n_frames=200, fill_mode=trickLED.FILL_MODE_MULTI):
    ani = animations.Divergent(leds)
    print('Divergent settings: default')
    play(ani, n_frames, fill_mode=fill_mode)
#     print('Divergent settings: fill_mode=FILL_MODE_MULTI')
#     play(ani, n_frames, fill_mode=trickLED.FILL_MODE_MULTI)

def convergent(leds, n_frames=200, fill_mode=trickLED.FILL_MODE_MULTI):
    ani = animations.Convergent(leds)
    print('Convergent settings: default')
    play(ani, n_frames, fill_mode=fill_mode)
#     print('Convergent settings: fill_mode=FILL_MODE_MULTI')
#     play(ani, n_frames, fill_mode=trickLED.FILL_MODE_MULTI)

def fire(leds, n_frames=200):
    ani = animations32.Fire(leds)
    print('Fire settings: default')
    play(ani, n_frames)

def conjuction(leds, n_frames=200):
    ani = animations32.Conjunction(leds)
    print('Conjuction settings: default')
    play(ani, n_frames)

# GENERATORS
def stepped_color_wheel(leds, n_frames=200):  
    print('stepped_color_wheel')
    ani = animations.NextGen(leds, generator = generators.stepped_color_wheel())
    play(ani, n_frames)
    
def striped_color_wheel(leds, n_frames=200, stripe_size=1):
    print('stepped_color_wheel(stripe_size={})'.format(strip_size))
    ani.generator = generators.striped_color_wheel(stripe_size=strip_size)
    play(ani, n_frames)
    
def fading_color_wheel(leds, n_frames=200, mode=trickLED.FADE_OUT):
    print('fading_color_wheel(mode={})'.format(mode))
    ani.generator = generators.fading_color_wheel(mode=mode)
    play(ani, n_frames)
    
def color_compliment(leds, n_frames=200):
    print('color_compliment()')
    ani = animations.NextGen(generator = generators.color_compliment(stripe_size=10))
    play(ani, n_frames)
    
def random_vivid(leds, n_frames=200):
    print('random_vivid()')
    ani = animations.NextGen(generator = generators.random_vivid())
    play(ani, n_frames)
    
def random_pastel(leds, n_frames=200, mask=(randint(0,254),randint(0,254),randint(0,254))):
    print('random_pastel(mask={})'.format(mask))
    ani.generator = generators.random_pastel(mask=mask)
    play(ani, n_frames)

def run(leds, colors, **kwargs):
    animation = colors['effect']
    if animation == "solid_color":
        solid_color(leds, colors)
    elif animation == "lit_bits":
        lit_bits(leds, n_frames=200, lit_percent=50)
    elif animation == "next_gen":
        next_gen(leds, n_frames=200, blanks=2, interval=150)
    elif animation == "jitter":
        jitter(leds, n_frames=200, background=0x020212, fill_mode=trickLED.FILL_MODE_SOLID)
    elif animation == "side_swipe":
        side_swipe(leds, n_frames=200)
    elif animation == "divergent":
        divergent(leds, n_frames=200)
    elif animation == "convergent":
        convergent(leds, n_frames=200)
    elif animation == "fire":
        fire(leds, n_frames=200)
    elif animation == "conjunction":
        conjuction(leds, n_frames=200)
    elif animation == "stepped_color_wheel":
        stepped_color_wheel(leds, n_frames=200)
    elif animation == "striped_color_wheel":
        striped_color_wheel(leds, n_frames=200)
    elif animation == "fading_color_wheel":
        fading_color_wheel(leds, n_frames=200)
    elif animation == "color_compliment":
        color_compliment(leds, n_frames=200)
    elif animation == "random_vivid":
        random_vivid(leds, n_frames=200)
    elif animation == "random_pastel":
        random_pastel(leds, n_frames=200)
