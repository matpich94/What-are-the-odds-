"""
This is the main function to run.
After running this function, you can connect to the local host
http://127.0.0.1:5000/
"""

from model import InputForm
from flask import Flask, render_template, request
from PIL import Image
import os.path


from read_data import *
from prob_computation import *
from display_prob import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
    
        (autonomy, routes) = read_millenium_falcon (form.path_millenium_falcon.data)#read_millenium_falcon (form.path.data)
        paths = create_all_paths(routes)
        (countdown, hunters) = read_empire(form.path_empire.data)
        
        prob = compute_final_prob (paths, autonomy, countdown, hunters)
               
        result = result_image(prob)
    else:
        result = None

    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)