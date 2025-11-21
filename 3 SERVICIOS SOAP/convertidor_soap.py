from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class ConvertidorService(ServiceBase):
    """
    Servicio SOAP para conversión de temperaturas.
    """
    @rpc(Float, _returns=Float)
    def c_to_f(ctx, celsius):
        # Celsius a Fahrenheit
        return (celsius * 9/5) + 32

    @rpc(Float, _returns=Float)
    def f_to_c(ctx, fahrenheit):
        # Fahrenheit a Celsius
        return (fahrenheit - 32) * 5/9

    @rpc(Float, _returns=Float)
    def f_to_k(ctx, fahrenheit):
        # Fahrenheit a Kelvin
        return (fahrenheit - 32) * 5/9 + 273.15

    @rpc(Float, _returns=Float)
    def k_to_c(ctx, kelvin):
        # Kelvin a Celsius
        return kelvin - 273.15

# Aplicación SOAP solo para conversiones
soap_app = Application(
    [ConvertidorService],
    tns='http://example.com/convertidor',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':
    # Servidor SOLO de conversión en puerto 8000
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servicio CONVERTIDOR corriendo en http://localhost:8000")
    server.serve_forever()


#<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#                  xmlns:conv="http://example.com/convertidor">
#   <soapenv:Header/>
#   <soapenv:Body>
#      <conv:c_to_f>
#         <celsius>25</celsius>
#      </conv:c_to_f>
#   </soapenv:Body>
#</soapenv:Envelope>