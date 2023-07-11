

try:
 5/0
 print("division exitosa")
except:
 print("No se puede dividir por cero")

class testing:
    def fail(self, argumentos):
      pass

try:
    prueba1 = testing.fail()
    print("Prueba exitosa")
except TypeError:
   print("Error de tipo")
except: #generico
    print("No se pudo realizar la ejecución del método")

"""
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print message
"""

