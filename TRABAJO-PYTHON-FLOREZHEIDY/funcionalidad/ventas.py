import os
import funcionalidad
import compras
def menuprincipal(Op)
    os.system("cls")
    menuStudentOp = '1.fecha de la compra\n2.informacion del provedor\n3 productos comprados\n4. Salir'
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