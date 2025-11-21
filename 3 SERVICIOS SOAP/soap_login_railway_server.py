from spyne import Application, rpc, ServiceBase, Unicode, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import psycopg2

# ===============================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ===============================

DB_CONFIG = {
    "host": "ballast.proxy.rlwy.net",  #VALOR_DE_PGHOST#
    "port": "28935", #VALOR_DE_PGPORT#
    "database": "railway", #VALOR_DE_PGDATABASE#
    "user": "postgres", #VALOR_DE_PGUSER#
    "password": "NEmevOwuoNoONrIbwYlOHnVlpEEZvlrP" #VALOR_DE_PGPASSWORD#
}

# ===============================
# SERVICIO SOAP
# ===============================
class LoginDBService(ServiceBase):


    @rpc(Unicode, Unicode, _returns=Boolean)
    def login(ctx, username, password):
        """
        Verifica las credenciales contra la base de datos PostgreSQL en Railway.
        Retorna True si el usuario existe y la contraseña coincide.
        """
        try:
            conn = psycopg2.connect(**DB_CONFIG, sslmode="require")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()
            conn.close()

            if user:
                print(f"[OK] Usuario '{username}' autenticado.")
                return True
            else:
                print(f"[ERROR] Credenciales incorrectas para '{username}'.")
                return False

        except Exception as e:
            print(f"[DB ERROR] {e}")
            return False


# ===============================
# CONFIGURACIÓN DEL SERVIDOR SOAP
# ===============================
application = Application(
    [LoginDBService],
    tns='spyne.examples.login.railway',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    print("🔐 Servidor SOAP de Login con Railway DB activo")
    print("📄 URL del servicio: http://localhost:8000")
    print("📄 WSDL disponible en: http://localhost:8000/?wsdl")

    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
