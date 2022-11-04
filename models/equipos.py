from utils.db import db

# Criogénica 1
class PAY_3220(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_3230(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_3120A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_3120B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_3770(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_3775(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_3780A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_3780B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4210(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4220(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_4140(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4920(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4925(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4930(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_4910(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_4910B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_4250(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_4260(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario
# Criogénica 2
class PAY_3420(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_3430(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_3320A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_3320B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_3970(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_3975(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_3980A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_3980B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4410(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_4420(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_4340(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_5020(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_5025(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_5030(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_5010(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_5010B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_4450(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_4460(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario
# Criogénica 3
class PAY_13220(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_13230(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_13120A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_13120B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_13770(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_13775(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_13780A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_13780B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14210(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14225(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_14140(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14920(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14925(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14930(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_14910(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_14910B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_14250(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_14260(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario
# Criogénica 4
class PAY_13420(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_13430(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_13320A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_13320B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_13970(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_13975(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_13980A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_13980B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14410(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_14425(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_14340(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_15020(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_15025(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_15030(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_15010(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_15010B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_14450(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_14460(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario
# Criogénica 5
class PAY_23220(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_23230(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_23120A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_23120B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_23770(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_23775(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_23780A(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAE_23780B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_24210(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_24225(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class KAE_24140(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_24920(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_24925(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PAY_24930(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class PBB_24930(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_24910(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_24910B(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_24250(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario

class EAL_24260(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    estado = db.Column(db.String(35))
    titulo = db.Column(db.String(35))
    detalle = db.Column(db.String(500))
    fechaReporte = db.Column(db.Date)
    fechaCreada = db.Column(db.Date)
    usuario = db.Column(db.String(35))

    def __init__(self,estado,titulo,detalle,fechaReporte,fechaCreada,usuario):
        self.estado = estado
        self.titulo = titulo
        self.detalle = detalle
        self.fechaReporte = fechaReporte
        self.fechaCreada = fechaCreada
        self.usuario = usuario