from trickLED import animations, animations32, generators, trickLED
from random import randint
import uasyncio as asyncio

class Effects():
    """
    This class defines the runnable effects.
    New effects can be defined as trikLED objects within named functions.
    The function name will be used to display the select option in the generated html.
    All fuctions must be passed the trickLED 'leds' object on which the animation is destined to play.
    
    """
    # ANIMATIONS
    def solid_color(leds, **kwargs):
        try:
            colors = kwargs['colors']
            ani = animations.SolidColor(leds, colors)
            return ani
        except:
            print("Error: Solid Color setting needs a valid colors dict passed as parameter")
            pass

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

    def side_swipe(leds):
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

def get_effect_names():
    return [name for name in dir(Effects) if name.startswith('_') == 0]

def get_animation(leds, effect, *colors):
    try:
        func = getattr(Effects, effect)
    except:
        print(f"No effect with name '{effect}' in function name space.")
    func(leds, **kwargs)
