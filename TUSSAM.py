# -*- coding: utf-8 -*-
from suds.client import Client
from lxml import etree
print "Utilización de API web con SOAP || TUSSAM"
print ""

cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)
respuesta = cliente.service.GetStatusLinea("34")
print respuesta