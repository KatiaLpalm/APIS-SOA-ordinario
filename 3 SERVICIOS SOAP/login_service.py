from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class AuthService(ServiceBase):
    """
    Servicio SOAP de autenticación simple.
    """
    @rpc(Unicode, Unicode, _returns=Unicode)
    def login(ctx, username, password):
        """
        Valida usuario y contraseña.

        Retorna:
        - 'LOGIN_OK' si son correctos.
        - 'LOGIN_FAIL' si no.
        """
        usuarios = {
            "admin": "1234",
            "luis": "password",
            "usuario": "abc123"
        }

        if username in usuarios and usuarios[username] == password:
            return "LOGIN_OK"
        else:
            return "LOGIN_FAIL"

# Aplicación SOAP solo para login
soap_app = Application(
    [AuthService],
    tns='http://example.com/login',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':
    # Servidor SOLO de login en puerto 8001
    server = make_server('0.0.0.0', 8001, wsgi_app)
    print("Servicio LOGIN corriendo en http://localhost:8001")
    server.serve_forever()

#<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#                  xmlns:log="http://example.com/login">
#   <soapenv:Header/>
#   <soapenv:Body>
#      <log:login>
#         <username>admin</username>
#         <password>1234</password>
#      </log:login>
#   </soapenv:Body>
#</soapenv:Envelope>