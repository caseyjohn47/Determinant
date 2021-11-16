from flask import render_template, flash, redirect, url_for, request
from app import app
import main

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    n = 3
    return render_template("index.html", title='Home', n=n)


@app.route('/index/<int:n>', methods=['GET', 'POST'])
def matrix_size(n):
    return render_template("index.html", title='Home', n=n)


# Handle the matrix
@app.route('/matrix-handler', methods=['GET', 'POST'])
def handle_matrix():
    n = int(request.form.get('n'))
    matrix = [[0 for j in range(n)] for k in range(n)]
    for x in range(n):
        for y in range(n):
            row = str(x)
            col = str(y)
            id = row + "_" + col
            try:
                int(request.form.get(id))
                matrix[x][y] = int(request.form.get(id))
            except ValueError:
                flash("ERROR: An input was not acceptable!")
                return redirect(url_for('matrix_size', n=n))
    determinant = main.det(matrix, n)
    flash("The determinant is " + str(determinant))
    return redirect(url_for('matrix_size', n=n))