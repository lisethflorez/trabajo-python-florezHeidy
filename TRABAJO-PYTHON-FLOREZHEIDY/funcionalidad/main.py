import os
import compras
import ventas
import funcionalidad
def menuprincipal(op : int):
    title = """
    *****************************
    *    PANADERIA PANCAMP   *
    *****************************
    """
    menuStudentOp = '1.gestion de compras \n2.gestion de ventas\n3.fecha \n4. Salir'
    if (op != 4):
        print(title)
        print(menuStudentOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            menuprincipal(0)
        else:
            match (op):
                case 1:
                    compras(0)
                case 2:
                    ventas(0)
                case _:
                    print()
                    menuprincipal