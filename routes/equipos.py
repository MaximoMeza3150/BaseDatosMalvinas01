# from sqlite3 import Date
from flask import Blueprint, redirect, render_template, request, flash
from models.equipos import *
from utils.db import db
from common.filters import detalleEstado, registrarEstado, ultimoEstado, allEstados
from datetime import date

equipos = Blueprint('equipos', __name__)
hoy =  date.today()

@equipos.route("/")
def home():
    return render_template('index.html')

@equipos.route("/equiposAreas")
def initEquipos():
    return render_template('equiposAreas.html')

@equipos.route("/equipos/Graficos")
def equiposGraficos():
    return render_template('equiposGraficos.html')

@equipos.route("/equipos/MapaDeCalor")
def equiposMapaCalor():
    return render_template('equiposMapaCalor.html')

@equipos.route("/equiposAreas/todos")
def equiposAreas():

    Ul_Crio1 ={
        'PAY_3220'  : ultimoEstado(PAY_3220),
        'PAY_3230'  : ultimoEstado(PAY_3230),
        'EAL_3120A' : ultimoEstado(EAL_3120A),
        'EAL_3120B' : ultimoEstado(EAL_3120B),
        'KAE_3770'  : ultimoEstado(KAE_3770),
        'KAE_3775'  : ultimoEstado(KAE_3775),
        'EAE_3780A' : ultimoEstado(EAE_3780A),
        'EAE_3780B' : ultimoEstado(EAE_3780B),
        'PAY_4210'  : ultimoEstado(PAY_4210),
        'PAY_4220'  : ultimoEstado(PAY_4220),
        'KAE_4140'  : ultimoEstado(KAE_4140),
        'PAY_4920'  : ultimoEstado(PAY_4920),
        'PAY_4925'  : ultimoEstado(PAY_4925),
        'PAY_4930'  : ultimoEstado(PAY_4930),
        'EAL_4910'  : ultimoEstado(EAL_4910),
        'EAL_4910B'  : ultimoEstado(EAL_4910B),
        'EAL_4250'  : ultimoEstado(EAL_4250),
        'EAL_4260'  : ultimoEstado(EAL_4260)}
    Ul_Crio2 ={
        'PAY_3420'  : ultimoEstado(PAY_3420),
        'PAY_3430'  : ultimoEstado(PAY_3430),
        'EAL_3320A' : ultimoEstado(EAL_3320A),
        'EAL_3320B' : ultimoEstado(EAL_3320B),
        'KAE_3970'  : ultimoEstado(KAE_3970),
        'KAE_3975'  : ultimoEstado(KAE_3975),
        'EAE_3980A' : ultimoEstado(EAE_3980A),
        'EAE_3980B' : ultimoEstado(EAE_3980B),
        'PAY_4410'  : ultimoEstado(PAY_4410),
        'PAY_4420'  : ultimoEstado(PAY_4420),
        'KAE_4340'  : ultimoEstado(KAE_4340),
        'PAY_5020'  : ultimoEstado(PAY_5020),
        'PAY_5025'  : ultimoEstado(PAY_5025),
        'PAY_5030'  : ultimoEstado(PAY_5030),
        'EAL_5010'  : ultimoEstado(EAL_5010),
        'EAL_5010B'  : ultimoEstado(EAL_5010B),
        'EAL_4450'  : ultimoEstado(EAL_4450),
        'EAL_4460'  : ultimoEstado(EAL_4460)}
    Ul_Crio3 ={
        'PAY_13220'  : ultimoEstado(PAY_13220),
        'PAY_13230'  : ultimoEstado(PAY_13230),
        'EAL_13120A' : ultimoEstado(EAL_13120A),
        'EAL_13120B' : ultimoEstado(EAL_13120B),
        'KAE_13770'  : ultimoEstado(KAE_13770),
        'KAE_13775'  : ultimoEstado(KAE_13775),
        'EAE_13780A' : ultimoEstado(EAE_13780A),
        'EAE_13780B' : ultimoEstado(EAE_13780B),
        'PAY_14210'  : ultimoEstado(PAY_14210),
        'PAY_14225'  : ultimoEstado(PAY_14225),
        'KAE_14140'  : ultimoEstado(KAE_14140),
        'PAY_14920'  : ultimoEstado(PAY_14920),
        'PAY_14925'  : ultimoEstado(PAY_14925),
        'PAY_14930'  : ultimoEstado(PAY_14930),
        'EAL_4910'  : ultimoEstado(EAL_14910),
        'EAL_4910B'  : ultimoEstado(EAL_14910B),
        'EAL_14250'  : ultimoEstado(EAL_14250),
        'EAL_14260'  : ultimoEstado(EAL_14260)}
    Ul_Crio4 ={
        'PAY_13420'  : ultimoEstado(PAY_13420),
        'PAY_13430'  : ultimoEstado(PAY_13430),
        'EAL_13320A' : ultimoEstado(EAL_13320A),
        'EAL_13320B' : ultimoEstado(EAL_13320B),
        'KAE_13970'  : ultimoEstado(KAE_13970),
        'KAE_13975'  : ultimoEstado(KAE_13975),
        'EAE_13980A' : ultimoEstado(EAE_13980A),
        'EAE_13980B' : ultimoEstado(EAE_13980B),
        'PAY_14410'  : ultimoEstado(PAY_14410),
        'PAY_14425'  : ultimoEstado(PAY_14425),
        'KAE_14340'  : ultimoEstado(KAE_14340),
        'PAY_15020'  : ultimoEstado(PAY_15020),
        'PAY_15025'  : ultimoEstado(PAY_15025),
        'PAY_15030'  : ultimoEstado(PAY_15030),
        'EAL_15010'  : ultimoEstado(EAL_15010),
        'EAL_15010B'  : ultimoEstado(EAL_15010B),
        'EAL_14450'  : ultimoEstado(EAL_14450),
        'EAL_14460'  : ultimoEstado(EAL_14460)}
    Ul_Crio5 ={
        'PAY_23220'  : ultimoEstado(PAY_23220),
        'PAY_23230'  : ultimoEstado(PAY_23230),
        'EAL_23120A' : ultimoEstado(EAL_23120A),
        'EAL_23120B' : ultimoEstado(EAL_23120B),
        'KAE_23770'  : ultimoEstado(KAE_23770),
        'KAE_23775'  : ultimoEstado(KAE_23775),
        'EAE_23780A' : ultimoEstado(EAE_23780A),
        'EAE_23780B' : ultimoEstado(EAE_23780B),
        'PAY_24210'  : ultimoEstado(PAY_24210),
        'PAY_24225'  : ultimoEstado(PAY_24225),
        'KAE_24140'  : ultimoEstado(KAE_24140),
        'PAY_24920'  : ultimoEstado(PAY_24920),
        'PAY_24925'  : ultimoEstado(PAY_24925),
        'PAY_24930'  : ultimoEstado(PAY_24930),
        'PBB_24930' : ultimoEstado(PBB_24930),
        'EAL_24910'  : ultimoEstado(EAL_24910),
        'EAL_24910B'  : ultimoEstado(EAL_24910B),
        'EAL_24250'  : ultimoEstado(EAL_24250),
        'EAL_24260'  : ultimoEstado(EAL_24260)}

    return render_template('equiposTodos.html',
    Ul_Crio1=Ul_Crio1,Ul_Crio2=Ul_Crio2,Ul_Crio3=Ul_Crio3,Ul_Crio4=Ul_Crio4, Ul_Crio5=Ul_Crio5)
    
@equipos.route("/equiposAreas/estabilizacion")
def equiposEstab():
    return render_template('equiposEstab.html')

@equipos.route("/equiposAreas/form")
def equiposForm():
    return render_template('equiposForm.html')

@equipos.route('/crearRegistro', methods=['POST'])
def newRegistroEquipo():
    tag = request.form['equipo']
    estado = request.form['radio_status_equipos']
    titulo = request.form['titulo']
    detalle = request.form['detalle']
    fechaReporte = date.fromisoformat(request.form['fechaReporte'])
    usuario = 'programadorTEST'
    if titulo == "": titulo = '-'
    if detalle == "": detalle = '-'

    nuevoRegistro = registrarEstado(tag,estado,titulo,detalle,fechaReporte,hoy,usuario)

    db.session.add(nuevoRegistro)
    db.session.commit()
    # flash('El equipo ha sido actualizado')
    return redirect ('/equiposAreas/todos')

@equipos.route("/editarRegistro/<tag>/<id>", methods= ['POST', 'GET'])
def updateRegistroEquipo(tag,id):
    if request.method == 'POST':
        update = detalleEstado(tag,id)

        update.estado = request.form['radio_status_equipos']
        update.titulo = request.form['titulo']
        update.detalle = request.form['detalle']
        update.fechaReporte = date.fromisoformat(request.form['fechaReporte'])
        update.usuario = 'programadorTEST'
        update.fechaCreada = hoy
        if update.titulo == "": update.titulo = '-'
        if update.detalle == "": update.detalle = '-'

        db.session.commit()
        return redirect ('/equiposAreas/todos')

    lista = detalleEstado(tag,id)

    return render_template ('equiposFormEdit.html', lista =lista, tabla=tag )

@equipos.route("/detalleRegistro/<tag>/<id>")
def detalleRegistroEquipo(tag,id):
    lista = detalleEstado(tag,id)

    return render_template('equiposDetalle.html', lista=lista, tabla= tag)

@equipos.route("/historialEquipo/<tag>")
def historialEquipo(tag):
    lista = allEstados(tag)
    return render_template('equiposHistorial.html', lista=lista, tabla=tag)