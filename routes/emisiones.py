from flask import Blueprint, redirect, render_template

emisiones = Blueprint('emisiones', __name__)

@emisiones.route("/emisionesDemo")
def emisionesDemo():
    return render_template('emisionesDemo.html')