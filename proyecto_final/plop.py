import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from flask import Flask, render_template 




# Root URL 
@app.route('/contactenos', methods=['GET', 'POST'])
def pag_contacto():
	pregunta = ""
 if request.method == 'POST'
pregunta = request.form.get ('pregunta')
with open ("salida.csv", "a", newline="") as: archivo 
	# Save the figure in the static directory 
plot.savefig(os.path.join('static', 'images', 'plot.png')) 

return render_template('contactenos.html') 
