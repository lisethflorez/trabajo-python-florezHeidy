import os
import funcionalidad
import compras
import ventas
def menuprincipal(op)
    os.system("cls")
    menuStudentOp = '1. nombre del producto \n2.cantidad\n3 precio\n4. Salir'
    if (op != 4):
        print(menuStudentOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            menuprincipal(0)
menuprincipal(1)
                  