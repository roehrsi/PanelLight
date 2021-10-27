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
    def gen_none():
        return None
    
    def gen_stepped_color_wheel(colors):  
        return generators.stepped_color_wheel(hue_stride=10, stripe_size=20, start_hue=0)
        
    def gen_striped_color_wheel(colors):
        return generators.striped_color_wheel(hue_stride=10, stripe_size=10, start_hue=0)
    
    def gen_fading_color_wheel(colors):
        return generators.fading_color_wheel(hue_stride=10, stripe_size=20, start_hue=0, mode=trickLED.FADE_OUT)
            
    def gen_color_compliment(colors):
        return generators.color_compliment(hue_stride=10, stripe_size=5, start_hue=0)
           
    def gen_random_vivid(colors):
        return generators.random_vivid()
           
    def gen_random_pastel(colors):
        return generators.random_pastel(mask=(int(colors['r']),int(colors['g']),int(colors['b'])))
    
    # ANIMATIONS   
    # no animation, only color
    def ani_solid_color(leds, colors):
        ani = animations.SolidColor(leds, colors)
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        return ani

    # Base options: leds, interval=50, palette=None, generator=None, brightness=200
    def ani_lit_bits(leds, colors):
        ani = animations.LitBits(leds, interval=50, palette=None, generator=None, brightness=200, lit_percent=50)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        # anim specific settings
        ani.settings['lit_percent'] = 40
        print(f'LitBits settings: {ani.settings}')
        return ani
    
    # Options: blanks=0, scroll_speed=1
    def ani_next_gen(leds, colors):
        ani = animations.NextGen(leds)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        # anim specific settings
        ani.settings['blanks'] = 0
        ani.settings['scroll_speed'] = 1 # (-1,1) for forwards/backwards
        print(f'NextGen settings: {ani.settings}')
        return ani
    
    
    def ani_jitter(leds, colors):
        ani = animations.Jitter(leds)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        # anim specific settings
        ani.settings['background'] = rgb_to_hex(colors) # Background color of unsparked pixels
        ani.settings['fade_percent'] = 40 # Percent to fade colors each cycle
        ani.settings['sparking'] = 25 # Odds / 255 of sparking more pixels
        ani.settings['lit_percent'] = 15 # Approximate percent of pixels to be lit when sparking
        ani.settings['fill_mode'] = trickLED.FILL_MODE_SOLID #fill sparked with either same color (solid) or generate new color for each (multi).
        print(f'Jitter settings: {ani.settings}')
        return ani

    def ani_side_swipe(leds, colors):
        ani = animations.SideSwipe(leds)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        print(f'SideSwipe settings: {ani.settings}')
        return ani
    
    def ani_divergent(leds, colors):
        ani = animations.Divergent(leds, fill_mode=fill_mode)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        # anim specific settings
        ani.settings['fill_mode'] = trickLED.FILL_MODE_MULTI
        print(f'Divergent settings: {ani.settings}')
        return ani
    
    def ani_convergent(leds, colors):
        ani = animations.Convergent(leds)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_MIRROR
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        # anim specific settings
        ani.settings['fill_mode'] = trickLED.FILL_MODE_MULTI
        print(f'Convergent settings: {ani.settings}')
        return ani
    
    def ani_fire(leds, colors):
        ani = animations32.Fire(leds)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_STRIPE
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        # anim specific settings
        ani.settings['sparking'] = 32
        ani.settings['cooling'] = 15
        ani.settings['scroll_speed'] = 1
        ani.settings['hotspots'] = 1
        print(f'Fire settings: {ani.settings}')
        return ani
    
    def ani_conjuction(leds, colors):
        ani = animations32.Conjunction(leds)
        # base settings
        ani.leds.repeat_mode = leds.REPEAT_MODE_STRIPE
        ani.settings['interval'] = 100 # millisecond pause between each frame
        ani.settings['palette'] = None # color palette
        ani.settings['generator'] = getattr(Effects, colors['generator'])(colors) # color generator
        ani.settings['brightness'] = int(colors['br']) # Brightness
        print(f'Conjuction settings: {ani.settings}')
        return ani

def rgb_to_hex(colors):
    r=int(colors['r'])
    g=int(colors['g'])
    b=int(colors['b'])
    return int("{0:02x}{1:02x}{2:02x}".format(r, g, b), 16)

def get_effect_names():
    """
    @return str the registered effects from Effects class as names
    """
    return [name for name in dir(Effects) if name.startswith('ani_')]

def get_generator_names():
    """
    @return str the registered effects from Effects class as names
    """
    return [name for name in dir(Effects) if name.startswith('gen_')]

def get_animation(leds, colors):
    """
    @return the animation registered to the given effect name
    """
    effect = colors['effect']
    try:
        func = getattr(Effects, effect)
    except:
        print(f"No effect with name '{effect}' in function name space.")
    return func(leds, colors)