from trickLED import animations, animations32, generators, trickLED
from random import randint
import uasyncio as asyncio

class Effects():
    """
    This class defines the runnable effects.
    New effects can be defined as trikLED objects within named functions.
    The function name will be used to display the select option in the generated html.
    All fuctions must be passed the trickLED 'leds' object on which the animation is destined to play,
    as well as the 'colors' settings dict.
    """   
    
    # GENERATORS
    def gen_none(colors, hue_stride=10, stripe_size=20, start_hue=0):
        return None
    
    def gen_stepped_color_wheel(colors, hue_stride=10, stripe_size=7, start_hue=0):  
        return generators.stepped_color_wheel(hue_stride, stripe_size, start_hue)
        
    def gen_striped_color_wheel(colors, hue_stride=10, stripe_size=10, start_hue=0):
        return generators.striped_color_wheel(hue_stride, stripe_size, start_hue)
    
    def gen_fading_color_wheel(colors, hue_stride=10, stripe_size=28, start_hue=0):
        return generators.fading_color_wheel(hue_stride, stripe_size, start_hue, mode=trickLED.FADE_OUT)
            
    def gen_color_compliment(colors, hue_stride=10, stripe_size=7, start_hue=0):
        return generators.color_compliment(hue_stride, stripe_size, start_hue)
           
    def gen_random_vivid(colors, hue_stride=10, stripe_size=20, start_hue=0):
        return generators.random_vivid()
           
    def gen_random_pastel(colors, hue_stride=10, stripe_size=20, start_hue=0):
        return generators.random_pastel(mask=(colors["rgb"]).to_bytes(3, 'big'))
    
    # ANIMATIONS   
    # no animation, only color
    def ani_solid_color(leds, colors):
        gen = getattr(Effects, colors["generator"])(colors)
        ani = animations.SolidColor(leds, colors["rgb"], gen)
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.leds.repeat_n = leds.n//2
        return ani

    # Base options: leds, interval=50, palette=None, generator=None, brightness=200
    def ani_lit_bits(leds, colors):
        ani = animations.LitBits(leds, palette = None)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.leds.repeat_n = leds.n//2
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(color) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        # anim specific settings
        ani.settings['lit_percent'] = None
        print(f'LitBits settings: {ani.settings}')
        return ani
    
    # Options: blanks=0, scroll_speed=1
    def ani_next_gen(leds, colors):
        ani = animations.NextGen(leds, palette = None)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.leds.repeat_n = leds.n//2
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        # anim specific settings
        ani.settings['blanks'] = 0 
        ani.settings['scroll_speed'] = 1 # (-1,1) for forwards/backwards
        print(f'NextGen settings: {ani.settings}')
        return ani
    
    
    def ani_jitter(leds, colors):
        ani = animations.Jitter(leds, palette = None)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.leds.repeat_n = leds.n
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 10 # millisecond pause between each frame
        # anim specific settings
        ani.settings['background'] = 0x000000 # rgb_to_hex(colors) # Background color of unsparked pixels
        ani.settings['fade_percent'] = 60 # Percent to fade colors each cycle
        ani.settings['sparking'] = 50 # Odds / 255 of sparking more pixels
        ani.settings['lit_percent'] = 30 # Approximate percent of pixels to be lit when sparking
        ani.settings['fill_mode'] = trickLED.FILL_MODE_MULTI if ani.generator else trickLED.FILL_MODE_SOLID #fill sparked with either same color (solid) or generate new color for each (multi).
        print(f'Jitter settings: {ani.settings}')
        return ani

    def ani_side_swipe(leds, colors):
        ani = animations.SideSwipe(leds, palette = None)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.leds.repeat_n = leds.n//2
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        print(f'SideSwipe settings: {ani.settings}')
        return ani
    
    def ani_divergent(leds, colors):
        ani = animations.Divergent(leds, palette = None)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.leds.repeat_n = leds.n//2
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        # anim specific settings
        ani.settings['fill_mode'] = trickLED.FILL_MODE_MULTI
        print(f'Divergent settings: {ani.settings}')
        return ani
    
    def ani_convergent(leds, colors):
        ani = animations.Convergent(leds, palette = None)
        # base settings
        ani.leds.repeat_n = n//2
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        # anim specific settings
        ani.settings['fill_mode'] = trickLED.FILL_MODE_MULTI
        print(f'Convergent settings: {ani.settings}')
        return ani
    
    def ani_fire(leds, colors):
        ani = animations32.Fire(leds, palette = None)
        # base settings
        ani.leds.repeat_mode = None
        ani.leds.repeat_n = None
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        # anim specific settings
        ani.settings['sparking'] = 32
        ani.settings['cooling'] = 15
        ani.settings['scroll_speed'] = 1
        ani.settings['hotspots'] = 4
        print(f'Fire settings: {ani.settings}')
        return ani
    
    def ani_conjuction(leds, colors):
        ani = animations32.Conjunction(leds, palette = None)
        # base settings
        ani.leds.repeat_n = None
        ani.leds.repeat_mode = None
#         ani.palette = None # color palette
        ani.generator = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['interval'] = 100 # millisecond pause between each frame
        print(f'Conjuction settings: {ani.settings}')
        return ani

#Convert html color code (e.g. #0000ff) to int
def color_to_int(color):
    return int(color[1:], 16)

def get_effect_names():
    """
    @return str the registered animation from Effects class as names
    """
    return [name for name in dir(Effects) if name.startswith('ani_')]

def get_generator_names():
    """
    @return str the registered generator from Effects class as names
    """
    return [name for name in dir(Effects) if name.startswith('gen_')]

def get_palette():
    """
    #TODO
    @return palette get a color palette for animations
    """
    pass

def get_effect(leds, colors):
    """
    @return func the effect registered to the given effect name
    """
    try:
        func = getattr(Effects, colors["effect"])
    except:
        print(f"No effect with name '{effect}' in function name space.")
    return func(leds, colors)