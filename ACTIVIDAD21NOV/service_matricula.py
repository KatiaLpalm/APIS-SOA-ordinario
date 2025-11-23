from spyne import ServiceBase, rpc, Integer, Unicode, Array, ComplexModel
from database import get_connection


# ====== DEFINIMOS MODELO SOAP CORRECTO ======
class MatriculaType(ComplexModel):
    id_matricula = Integer
    id_estudiante = Integer
    id_grupo = Integer
    fecha_registro = Unicode
    estatus = Unicode


# ====== SERVICIO ======
class MatriculaService(ServiceBase):

    # Crear matrícula
    @rpc(Integer, Integer, Unicode, Unicode, _returns=Unicode)
    def crear_matricula(ctx, id_estudiante, id_grupo, fecha_registro, estatus):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO matricula (id_estudiante, id_grupo, fecha_registro, estatus)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (id_estudiante, id_grupo, fecha_registro, estatus))
        conn.commit()

        cursor.close()
        conn.close()

        return "Matrícula creada exitosamente"

    # Obtener matrícula por ID
    @rpc(Integer, _returns=MatriculaType)
    def obtener_matricula(ctx, id_matricula):
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
            SELECT id_matricula, id_estudiante, id_grupo, fecha_registro, estatus
            FROM matricula 
            WHERE id_matricula = %s
        """

        cursor.execute(sql, (id_matricula,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if not row:
            return MatriculaType(id_matricula=0, id_estudiante=0, id_grupo=0, fecha_registro="NO", estatus="NO EXISTE")

        return MatriculaType(
            id_matricula=row[0],
            id_estudiante=row[1],
            id_grupo=row[2],
            fecha_registro=str(row[3]),
            estatus=row[4]
        )

    # Eliminar matrícula
    @rpc(Integer, _returns=Unicode)
    def eliminar_matricula(ctx, id_matricula):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_matricula FROM matricula WHERE id_matricula=%s", (id_matricula,))
        existe = cursor.fetchone()

        if not existe:
            cursor.close()
            conn.close()
            return "La matrícula no existe"

        cursor.execute("DELETE FROM matricula WHERE id_matricula=%s", (id_matricula,))
        conn.commit()

        cursor.close()
        conn.close()

        return "Matrícula eliminada exitosamente"

    # Listar todas las matrículas
    @rpc(_returns=Array(MatriculaType))
    def listar_matriculas(ctx):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id_matricula, id_estudiante, id_grupo, fecha_registro, estatus FROM matricula")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        resultado = []
        for r in rows:
            resultado.append(
                MatriculaType(
                    id_matricula=r[0],
                    id_estudiante=r[1],
                    id_grupo=r[2],
                    fecha_registro=str(r[3]),
                    estatus=r[4]
                )
            )

        return resultado
