from effects import get_effect_names, get_generator_names

def web_page(colors, index):
    rgb=str(colors['rgb'])
    effect=colors['effect']
    generator=colors['generator']
    effects_list = get_effect_names()
    generators_list = get_generator_names()

    # COLOR SLIDERS
    if index == 0:
        return b'''<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>
            <h1>Light Panel Control</h1><form method="POST"><h3>Hue:</h3>
            <div><label for="colorWell">Color:</label>
            <input type="color" value="{}" id="colorWell" name="rgb">
            <output class="colorOutput" for="colorWell" id="colorOutput"></output></div>'''.format(rgb)
    
    # EFFECT SELECTOR
    if index == 1:
        return b'''<div><label for="effect">Select an effect</label><select id="effect" name="effect">'''
    
    if index == 2:
        return "".join(['<option value="{}">{}</option>'.format(effect, effect) for effect in effects_list])
    
    if index == 3:
        return b'''</select>'''
    
    # GENERATOR SELECTOR
    if index == 4:
        return b'''<div><label for="generator">Select a generator</label><select id="generator" name="generator">'''

    if index == 5:
        return "".join(['<option value="{}">{}</option>'.format(generator, generator) for generator in get_generator_names()])

    if index == 6:
        return b'''</select><button type="submit">POST</button></form>'''

    # JAVA SCRIPT
    if index == 7:
        return b'''<script>
            const rgbSelector = document.querySelector('#colorWell');
            const rgbOutput = document.querySelector('.colorOutput');
            rgbOutput.textContent = rgbSelector.value;
            
            rgbSelector.addEventListener('input', function() {{
                rgbOutput.textContent = this.value;
            }});
            
            document.querySelector('#effect').value="{}";
            document.querySelector('#generator').value="{}";
            </script></body></html>'''.format(effect, generator)
