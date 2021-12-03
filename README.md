# Reto 1

## 1. Clases, atributos y métodos de instancia
Crear una clase `Empleado`, con los siguientes atributos de instancia:
* `name`.
* `surname`.
* `email`: que debe tener la forma name.surname@email.com.
* `pay`: con una cantidad aleatoria entre 1500 y 2200, y tipo `int`.

La clase también debe tener el método de instancia `pay_rise`. Cuando sea llamada, debe subir el sueldo del empleado un 15%.

Probar que la clase funciona con los empleados **Sergio Pesquera**, **Miguel Betegon** y **Enrique Pernia**

## 2. Atributos de clase
Ahora, cada instancia empleado tendrá un `id`, un número único asignado a ella. El primer empleado será el 1, 2 el siguiente etc.

Probar la nueva funcionalidad como el anterior ejercicio, siendo **Sergio** el empleado 1, **Miguel** el 2, y **Enrique** el 3.

## 3.1 Dunder methods
Si realizamos un `print()` de cualquiera de las instancias anteriores, solo recibiremos la posición en memoria de esta, en formato hexadecimal. Implementar el método adecuado para que, al correr `print(instancia)`, se muestren sus atributos dentro del siguiente mensaje:

**El empleado** `name surname` **cobra** `pay`

## 3.2 Dunder methods
Programar el método necesario para que al correr `print(instancia1 + instancia2)`, se nos muestre en pantalla un entero con la suma del sueldo de ambas instancias

## 4. Constructores, métodos de clase y list comprehension
Ahora mismo cada nueva instancia `Empleado` se crea así:
```
jaled = Empleado("Jaled", "Moustafa", "1600")
```
Añadir un constructor que permita crear una instancia similar a partir del siguiente string de texto:
```
jaled=Empleado("Jaled, Moustafa, 1600")
```
Utilizar este nuevo constructor para leer en bucle el archivo `lista_empleados.txt`, guardando todas las instancias en una lista mediante **list comprehension**.

## 5. Herencias
Crear la clase `CEO`, hija de `Empleado`. Una instancia `CEO` hereda los atributos de su padre, y tiene uno más, una lista  donde guarda los empleados que están bajo su cargo. Una instancias de tipo `Empleado` se añade a la lista usando el metodo `add_employee`, y se elimina con `remove_employee`.
