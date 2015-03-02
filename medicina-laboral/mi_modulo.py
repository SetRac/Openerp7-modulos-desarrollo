# -*- coding: utf-8 -*-
from osv import fields, osv
from random import randint, random
from datetime import datetime
import urllib

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _order= 'name'
    _columns = {
        'name': fields.many2one('res.partner', required=True, help='Datos del paciente', select=1, string="Paciente"),
        'active': fields.boolean('Activo'),
        'quantity': fields.integer('cantidad'),
	'forma': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'date': fields.date('fecha'),
        'datetime': fields.datetime('fecha y hora'),
        'description': fields.text('descripcion'),
        'price': fields.float('precio', digits = (10,4)),
        'tabla_relacionada_id': fields.many2one('mi_modulo.mi_tabla_relacionada', 'Tabla Relacionada', domain="[('state','=','active')]", ondelete='set null'),
        'partner_ids': fields.many2many('res.partner', 'mi_modulo_partner_rel', 'mi_tabla_id', 'partner_id', 'Proveedores'),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
                #Datos del Paciente

        'empresa': fields.many2one('res.partner', required=True, size=100 ,  help='Nombre de la Empresa de donde Viene', string='Empresa'),
        'nombres': fields.char('Nombres y Apellidos',size=128 ,  help='Nombres y Apellidos'),
        'cedula': fields.char('C.I.',size=10 ,  help='Cedula de Identidad'),
        'edad': fields.integer('Edad',size=2,  help='Edad del Paciente'),
        'edocivil': fields.selection([('Casado(a)','Casado(a)'),('Soltero(a)','Soltero(a)')],'Estado Civil', help='Edad del Paciente'),
        'direccion': fields.char('Direccion',size=150 ,  help='Direccion del Paciente'),
        'telefono': fields.char('Telefono',size=30 ,  help='Telefono del Paciente'),
        'celular': fields.char('Celular',size=30 ,  help='Celular del Paciente'),
        'aspiracargo': fields.char('Aspirante al Cargo',size=64 ,  help='Aspirante al Cargo'),
        'ocupacargo': fields.char('Cargo que ocupa',size=64 ,  help='Cargo que Ocupa'),
        'fechaegreso': fields.date('Fecha de Ingreso',  help='Fecha de egreso'),
        'fechadia': fields.date('Fecha',  help='Fecha del Dia'),

        #Antecedentes familiares
        'papavive': fields.selection([('si','si'),('no','no')],'Padre Vive',  help='El Padre Vive?'),
        'mamavive': fields.selection([('si','si'),('no','no')],  help='La madre Vive?'),
        'papacondicion': fields.char('Condicion Padre',size=64 ,  help='Condicion Padre'),
        'mamacondicion': fields.char('Condicion Madre', digits=64 ,  help='Condicion Madre'),
        'nrohermanosvarones': fields.integer('Nro Hermanos',  help='Nro Hermanos'),
        'nrohermanoshembras': fields.integer('Nro Hermanas',  help='Nro Hermanas'),
        'hermanoscondicion': fields.char('Condicion Hermanos',size=64 ,  help='Condicion Hermanos'),
        'nrohijosvarones': fields.integer('Nro Hijos' ,  help='Nro Hijos'),
        'nrohijoshembras': fields.integer('Nro Hijas' ,  help='Nro Hijas'),
        'hijoscondicion': fields.char('Condicon Hijos',size=64 ,  help='Condicion Hijos'),
        #Antecedentes Medicos
        'eci': fields.selection([('si','si'),('no','no')], 'ECI',  help='ECI elija si o no'),
        'lechina': fields.selection([('si','si'),('no','no')], 'Lechina',  help='Elija si o no'),
        'sarampion': fields.selection([('si','si'),('no','no')],'sarampion',  help='Elija si o no'),
        'paperas': fields.selection([('si','si'),('no','no')],'Paperas',  help='Elija si o no'),
        'rubiola': fields.selection([('si','si'),('no','no')],'Rubiola',  help='Elija si o no'),
        'dengue': fields.selection([('si','si'),('no','no')],'Dengue',  help='Elija si o no'),
        'mononucleosis': fields.selection([('si','si'),('no','no')],'Mononucleosis',  help='Elija si o no'),
        'hepatitis': fields.selection([('si','si'),('no','no')],'Hepatitis',  help='Elija si o no'),
        'inmunizaciones': fields.char('inmunizaciones',size=64 ,  help='Elija si o no'),
        'quirurgicos': fields.selection([('si','si'),('no','no')],'Quirurgicos',  help='Elija si o no'),
        'quirurgicoscual': fields.char('Decriba Cual',size=64 ,  help='Describa cual'),
        #Antecedentes Medicos Alergias
        'alimentos': fields.char('Alimentos',size=64 ,  help='Alergia a alimentos'),
        'oloresfuertes': fields.char('Olores Fuertes',size=64 ,  help='Alergia a Olores Fuertes'),
        'polvos': fields.char('Polvos',size=64 ,  help='Alergias a Polvos'),
        
                #Uso de  Medicamentos

        'medicamentos': fields.selection([('si','si'),('no','no')], 'Medicamentos',  help='Toma Algun Medicamento'),
        'medicamentoscuales': fields.char('Cual Medicamento',size=64 ,  help='Describa Cuales Medicamentos'),
        'gastricos': fields.char('Gastricos',size=64 ,  help='Medicamentos Gastricos'),
        'respiratorios': fields.char('Respiratorios',size=64 ,  help='Medicamentos Respiratorios'),
        'cardiovasculares': fields.char('Cardiovasculares',size=64 ,  help='Medicamentos Cardiovascular'),
        'neurologicos': fields.char('Neurologicos',size=64 ,  help='Medicamentos Neurologicos'),
        'osteomuscular': fields.char('Osteomuscular',size=64 ,  help='Medicamentos Osteomuscular'),
        'orl': fields.char('ORL',size=64 ,  help='Medicamentos ORL'),
        'urinarios': fields.char('Urinarios',size=64 ,  help='Medicamentos Urinarios'),
        'endocrinos': fields.char('Endocrinos',size=64 ,  help='Medicamentos Endocrinos'),
        'psicosocial': fields.char('Psicosocial',size=64 ,  help='Medicamentos Psicosocial'),
                        #Solo  para mujeres
                        
        'menarquia': fields.char('Menarquia',size=64 ,  help='Menarquia'),
        'fur': fields.char('FUR',size=64 ,  help='FUR'),
        'disminorrea': fields.char('Disminorrea',size=64 ,  help='Disminorrea'),
        'mujeresotros': fields.char('OTROs',size=64 ,  help='Otras enfermedades'),
        'gestas': fields.char('Gestas',size=64 ,  help='Gestas'),
        'para': fields.char('Para',size=64 ,  help='Para'),
        'cesarea': fields.char('Cesarea',size=64 ,  help='Cesarea'),
        'abortos': fields.char('Abortos',size=64 ,  help='Abortos'),
        'ultimacitologia': fields.char('Ultima Citologia',size=64 ,  help='Ultima Citologia'),
        'patologia': fields.char('Patologia',size=64 ,  help='Patologia'),
        'secrecionotumaroacionsiono': fields.selection([('si','si'),('no','no')],'secresion tumoracion',  help='Secrecion o Tumoracion?'),
        
        #Antecedentes Laborales
        'empresaantigua': fields.many2one('res.partner', required=True,size=64 ,  help='Empresa donde trabajo anteriormente', string='Empresa Anterior'),
        'cargo': fields.char('Cargo que Ocupo',size=64 ,  help='Cargo que Ocupo'),
        'tiempoenempresa': fields.char('Tiempo en la Empresa',size=64 ,  help='Tiempo en la Empresa en Meses'),
        'implementosdeseguridad': fields.char('Implementos de Seguridad',size=64 ,  help='Utilizaba Implementos de Seguridad'),
        
        #Antecedentes Habitos
        'actividadfisica': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'tabaco': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'alcohol': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'cafe': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'micciones': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'intestinales': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'otroshabitos': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        
         #Sintomas
        'dolordecabeza': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'dificultadparaver': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'usodelentes': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'escuchar': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'asma': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'cansancio': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'opresion': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'hipertension': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'diarrea': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'problemasorinar': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'lesiongenital': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'enfermedadsexual': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'insomnio': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'cambiodepeso': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'dolordeespalda': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'fracturas': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'lesionespiel': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'trabajaporturnos': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'usaequiposproteccion': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'accidentelaboral': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        
        #Examen Fisico
        'peso': fields.char('Componente',size=25 ,  help='Forma Almacenatmiento'),
        'talla': fields.char('Componente',size=12 ,  help='Forma Almacenatmiento'),
        'fc': fields.char('Componente',size=15 ,  help='Forma Almacenatmiento'),
        'pulso': fields.char('Componente',size=20 ,  help='Forma Almacenatmiento'),
        'fr': fields.char('Componente',size=10 ,  help='Forma Almacenatmiento'),
        'ta': fields.char('Componente',size=8 ,  help='Forma Almacenatmiento'),
        'piel': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'cabezacuello': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'orl': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'visioncercana': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'visionlejana': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'visiondecolore': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'visionborro': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'visionusalentes': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'torax': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'toraxsimetrico': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'abdomen': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'herniasumbilicares': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'herniasinguinoescrotales': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
	'columnacervical': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'columnatoraxica': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'columnalumbosacra': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'miembrossuperiores': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'miembrosinferiores': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'neurologicos': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),

#Exame compleentario
        'hematologia': fields.char('Componente',size=25 ,  help='Forma Almacenatmiento'),
        'exudadofaringeo': fields.char('Componente',size=12 ,  help='Forma Almacenatmiento'),
        'glisemia': fields.char('Componente',size=15 ,  help='Forma Almacenatmiento'),
        'acidourico': fields.char('Componente',size=20 ,  help='Forma Almacenatmiento'),
        'colesterol': fields.char('Componente',size=10 ,  help='Forma Almacenatmiento'),
        'orina': fields.char('Componente',size=8 ,  help='Forma Almacenatmiento'),
        'hdl': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'especiales': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'ldl': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'rnmcolumnalumbosacra': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'trigliceridos': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'audiometria': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'heces': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'espirometria': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'vdrl': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),
        'hiv': fields.char('Componente',size=4 ,  help='Forma Almacenatmiento'),

#Diagnostico
        'elegible': fields.char('Componente',size=25 ,  help='Forma Almacenatmiento'),
        'elegibleconlimitaciones': fields.char('Componente',size=12 ,  help='Forma Almacenatmiento'),
        'noelegible': fields.char('Componente',size=15 ,  help='Forma Almacenatmiento'),
        'sugerencias': fields.char('Componente',size=20 ,  help='Forma Almacenatmiento'),
        'idx': fields.text('Componente',  help='Forma Almacenatmiento'),
        
        #
        #prevacacional
        #Edo General
        'resultadosexamencomplementario': fields.text('Resultados Examen Complementario',  help='Resultados Examen Complementario'),
        'peso2': fields.char('Peso',size=25 ,  help='Peso Pre-Vacacional'),
        'talla2': fields.char('Talla',size=12 ,  help='Talla Pre-Vacacional'),
        'ta2': fields.char('T.A.',size=15 ,  help='T.A.  Pre-Vacacional'),
        'fr2': fields.char('FR',size=12 ,  help='FR Pre-Vacacional'),
        'fc2': fields.char('FC',size=15 ,  help='FC Pre-Vacacional'),
        'condicionantesde': fields.selection([('Buenas Condiciones','Buenas Condiciones'),('Regulares Condiciones','Regulares Condiciones'),('Malas Condiciones','Malas Condiciones')],'Condiciones Fisicas', help='Condiciones antes de las vaciones del Paciente'),
#El traajador cumplio con
        #El traajador debe cumplir con
#sus actuales condiciones de salud hacen  necesario

        #
        #postvacacional
        
        #
        #Postempleo
        







        
    }


    def _check_date(self, cr, uid, ids, context = None):
        is_valid_data = True
        present = datetime.now()
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.date or not obj.datetime:
                continue

            date = datetime.strptime(obj.date, '%Y-%m-%d')
            date_time = datetime.strptime(obj.datetime, '%Y-%m-%d %H:%M:%S')
            if(date < present or date_time < present):
                is_valid_data = False

        return is_valid_data

    _constraints = [
        (_check_date,'Fecha debe ser en el futuro',['date','datetime']),
    ]

    def _random_quantity(self, cr, uid, context = None):
        return randint(5,100)

    _defaults = {
         'active': True,
         'state': 'draft',
         'price': lambda *a: random(),
         'quantity': _random_quantity,
    }

    def onchange_active(self, cr, uid, ids, active):
        if not active:
            return {'value': {'state': 'cancelled'} }
        return {
            'warning': {'message': 'Cambiando el estado a "activo"'},
            'value': {'state': 'active'},
        }

    def next_monday_date(self, cr, uid, ids, context=None):
        url = "http://www.timeapi.org/pdt/next+monday?\Y-\m-\d"
        next_monday_date = urllib.urlopen(url).read()
        self.write(cr, uid, ids, {'date': next_monday_date})

mi_modulo_mi_tabla()


class mi_modulo_mi_tabla_relacionada(osv.osv):
    _name = "mi_modulo.mi_tabla_relacionada"
    _columns = {
        'name': fields.many2one('res.partner', required=True, help='Datos del paciente', select=1, string="Paciente"),
        'active': fields.boolean('activo'),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
        'related': fields.one2many('mi_modulo.mi_tabla', 'tabla_relacionada_id', 'Objetos relacionados'),
    }
    _defaults = {
         'active': True,
         'state': 'draft',
    }

mi_modulo_mi_tabla_relacionada()

class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = "res.partner"

    _columns = {
        'mi_tabla_ids': fields.many2many('mi_modulo.mi_tabla', 'mi_modulo_partner_rel', 'partner_id', 'mi_tabla_id', 'Historia Medica Del Paciente'),
    }
