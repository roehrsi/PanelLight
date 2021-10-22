def web_page(colors, index):
    r=str(colors['r'])
    g=str(colors['g'])
    b=str(colors['b'])
    br=str(colors['br'])
    effect=str(colors['effect'])

    if index == 0:
        return b'''<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>
            <h1>Light Panel Control</h1><h2>Solid Color</h2><form action="/colors" method="GET"><h3>Hue:</h3>
            <div class="slidecontainer"><label for="rSlider">R:</label>
                <input type="range" id="rSlider" name="r" min="0" max="255" value="{}">
                <output class="rOutput" for="rSlider" id="rOutput"></output>
            </div><div class="slidecontainer"><label for="gSlider">G:</label>
                <input type="range" id="gSlider" name="g" min="0" max="255" value="{}">
                <output class="gOutput" for="gSlider" id="gOutput"></output>
            </div><div class="slidecontainer"><label for="bSlider">B:</label>
                <input type="range" id="bSlider" name="b" min="0" max="255" value="{}">
                <output class="bOutput" for="bSlider" id="bOutput"></output></div><h3>Brightness:</h3>
            <div class="slidecontainer"><label for="brSlider">B:</label>
                <input type="range" id="brSlider" name="br" min="0" max="100" value="{}">
                <output class="brOutput" for="brSlider" id="brOutput"></output>
            </div>'''.format(r,g,b,br)
    if index == 1:
        return b'''<div><label for="effect">Select an effect</label><select id="effect" name="effect">
            <option value="solid_color">Solid Color</option>
            <option value="stepped_color_wheel">stepped_color_wheel</option>
            <option value="striped_color_wheel">striped_color_wheel</option>
            <option value="fading_color_wheel">fading_color_wheel</option>
            <option value="color_compliment">color_compliment</option>
            <option value="random_vivid">random_vivid</option>
            <option value="random_pastel">random_pastel</option>
            <option value="lit_bits">LitBits</option>
            <option value="next_gen">NextGen</option>
            <option value="jitter">Jitter</option>
            <option value="side_swipe">SideSwipe</option>
            <option value="divergent">Divergent</option>
            <option value="onvergent">Convergent</option>
            <option value="fire">Fire</option>
            <option value="conjuction">Conjuction</option>
            </select><button type="submit">POST</button></form>'''
    if index == 2:
        return b'''<script>
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
            rSlider.addEventListener('input', function() {{
                rOutput.textContent = this.value;
            }});
            gSlider.addEventListener('input', function() {{
              gOutput.textContent = this.value;
            }});
            bSlider.addEventListener('input', function() {{
              bOutput.textContent = this.value;
            }});
            brSlider.addEventListener('input', function() {{
              brOutput.textContent = this.value;
            }});
            document.querySelector('#effect').value={}
            </script></body></html>'''.format(effect)