import os
import compras
import ventas

def menuprincipal(op : int):
    title = """
    *******************************************
    *       INFORMACION DEL CLIENTE *
    *******************************************
    """
    menuStudentOp = '1.nombre\n2.direccion\n3 fecha\n4. Salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menuStudentOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            menuprincipal(0)
menuprincipal(1)