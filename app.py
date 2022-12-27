from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def submit():
    if request.method == "POST":
        try:
            row = request.form.get('row')
            row = int(row)
            mat = []
            items = request.form.get('item')
            items = items.split(' ')
            lst_items = list(items)
            for i in range(len(lst_items)):
                lst_items[i] = int(lst_items[i])
            while lst_items != []:
                mat.append(lst_items[:row])
                lst_items = lst_items[row:]

            inv_mat = np.linalg.inv(mat)
        except:
            inv_mat = "Inverse is not possible"
    return render_template('index.html', inv_mat = inv_mat)