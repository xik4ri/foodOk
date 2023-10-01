import mysql.connector

class Registro_de_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='cs.ilab.cl',
                                                database='2_BD_69',
                                                user='2_BD_69',
                                                password='nicolas.matamalal23')
    def buscar_user(self, nombres):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM cajero WHERE nombres = {}".format(nombres)
        cur.execute(sql)
        nomx = cur.fetchall()
        cur.close()
        return nomx
    
    def busca_password(self, contrasena):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM cajero WHERE contrasena = {}".format(contrasena)
        cur.execute(sql)
        conx = cur.fetchall()
        cur.close()
        return conx


