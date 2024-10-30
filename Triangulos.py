#Triángulo de Sierpinski

#Importar la libreria
import turtle

#Funcion
#Dibujar el triangulo
def dibujar_el_Triangulo(puntos,color,Tortuga):
    Tortuga.fillcolor(color)
    Tortuga.up()
    Tortuga.goto(puntos[0][0],puntos[0][1])
    Tortuga.down()
    Tortuga.begin_fill()
    Tortuga.goto(puntos[1][0],puntos[1][1])
    Tortuga.goto(puntos[2][0],puntos[2][1])
    Tortuga.goto(puntos[0][0],puntos[0][1])
    Tortuga.end_fill()

def obtenerMitad(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

#Aplicando la SIERPINSKI
def sierpinski(puntos,grado,Tortuga):
    colormap = ['blue','red','green','white','yellow','violet','orange','aqua']
    dibujar_el_Triangulo(puntos,colormap[grado],Tortuga)
    if grado > 0:
        sierpinski([puntos[0],
                        obtenerMitad(puntos[0], puntos[1]),
                        obtenerMitad(puntos[0], puntos[2])],
                   grado-1, Tortuga)
        sierpinski([puntos[1],
                        obtenerMitad(puntos[0], puntos[1]),
                        obtenerMitad(puntos[1], puntos[2])],
                   grado-1, Tortuga)
        sierpinski([puntos[2],
                        obtenerMitad(puntos[2], puntos[1]),
                        obtenerMitad(puntos[0], puntos[2])],
                   grado-1, Tortuga)

#Despues ingresar el valor, se genera la triangulo
def Ejecutar_codigo():
    #Validacion de numero
    while True:
        numero = turtle.numinput("Tipo de triangulo", "Solo genera 1 al 8 tipos triangulos:", default=0, minval=1,maxval=8)
        if numero is not None:
            numero = int(numero)
            return numero
        else:
            exit()

#Crear la interfaz
def main():
   Tortuga = turtle.Turtle()
   miVentana = turtle.Screen()
   miVentana.title("Triángulo de Sierpinski")
   Tipo_triangulo = Ejecutar_codigo()
   misPuntos = [[-150,-50],[0,150],[150,-50]]
   sierpinski(misPuntos,Tipo_triangulo-1,Tortuga)
   miVentana.exitonclick()

main()