# -*- coding: utf-8 -*-
from report import report_sxw

class mi_reporte2(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(mi_reporte2, self).__init__(cr, uid, name, context=context)

report_sxw.report_sxw('report.mi_modulo.mi_reporte2', 'mi_modulo.mi_tabla', 'addons/mi_modulo/report/mi_reporte2.rml', parser=mi_reporte2, header=True)
