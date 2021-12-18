from flask import render_template, flash, redirect, url_for, request
from app import app
import main

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    n = 3
    return render_template("index.html", title='Determinant', n=n)


@app.route('/index/<int:n>', methods=['GET', 'POST'])
def matrix_size(n):
    return render_template("index.html", title='Determinant', n=n)


# Handle the matrix function
@app.route('/matrix-handler', methods=['GET', 'POST'])
def handle_matrix():
    n = int(request.form.get('n'))
    valid = True
    result = ""
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
                valid = False
                matrix[x][y] = 0
    if (valid):
        determinant = main.det(matrix, n)
        result = "The determinant is " + str(determinant)
    else:
        result = "Input was invalid. Please try again."
    return render_template("index.html", title='Determinant', n=n, matrix=matrix, result=result)


# default normalize page
@app.route('/normalize', methods=['GET', 'POST'])
def normalize():
    size = 2
    vectors = 2
    return render_template("normalize.html", title='Normalize', size=size, vectors=vectors)


# resize normalize page
@app.route('/normalize/<int:size>/<int:vectors>', methods=['GET', 'POST'])
def norm_size(size, vectors):
    return render_template("normalize.html", title='Normalize', size=size, vectors=vectors)


# Handle the normalize function
@app.route('/normalize-set', methods=['GET', 'POST'])
def normalize_set():
    vectors = int(request.form.get('vectors'))
    size = int(request.form.get('size'))
    valid = True
    zero_vector = False
    result = ""
    matrix = [[0 for j in range(size)] for k in range(vectors)]
    normal = []
    for x in range(vectors):
        not_zero_check = False
        for y in range(size):
            row = str(y)
            col = str(x)
            id = row + "_" + col
            try:
                int(request.form.get(id))
                matrix[x][y] = int(request.form.get(id))
                if matrix[x][y] != 0:
                    not_zero_check = True
            except ValueError:
                valid = False
                matrix[x][y] = 0
        if not not_zero_check:
            zero_vector = True
            valid = False
    if (valid):
        normal = main.normalize_set(matrix)
        result = "The determinant is " + str(normal)
    elif (zero_vector):
        result = "The zero vector can't be normalized"
    else:
        result = "Input was invalid. Please try again."
        valid = False
    return render_template("normalize.html", title='Normalize', size=size, vectors=vectors, matrix=matrix, result=result, valid=valid, normal=normal)