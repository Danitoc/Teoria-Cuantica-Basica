import Retos as r
import ComplexL as cm
import math as m


def Sim4_1():
    vector = [(-3, -1), (0, -2), (0, 1), (2, 0)]
    ket1 = [(1, 0), (0, -1)]
    ket2 = [(0, 1), (1, 0)]
    prob = r.ProbabilidadParticula(vector, 2)
    amp = r.AmplitudTransicion(ket1, ket2)
    print('Probabilidad que la particula se encuentre en la posicion 2:', prob)
    print("Amplitud transitar del ket 1 al ket 2: ", amp)
    print("Probabilidad de transitar del ket 1 al ket 2: ", round(r.Probabilidad(amp)))


def Ejer4_3_1():
    Sx = [[0, 1], [1, 0]]
    SxC = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    inicio = [(1, 0), (0, 0)]
    valores = r.ValoresPropios(Sx)
    vectores = r.VecNormalizado(Sx)
    final = cm.MatVec(SxC, inicio)
    print('Valores propios: ', valores)
    print('Vectores propios normalizados: ', vectores)
    print('Estado final: ', final)


def Ejer4_3_2():
    Sx = [[0, 1], [1, 0]]
    inicio = [(1, 0), (0, 0)]
    valores = r.ValoresPropios(Sx)
    vectores = r.VecNormalizado(Sx)
    probabilidad = r.ProbabilidadValPropios(inicio, vectores)
    medio = r.ValorMedio(probabilidad, valores)
    print('Probabilidad: ', probabilidad)
    print('Valor medio: ', medio)
    r.Graficar(probabilidad)


def Ejer4_4_1():
    U1 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    U2 = [[(m.sqrt(2) / 2, 0), (m.sqrt(2) / 2, 0)], [(m.sqrt(2) / 2, 0), (-m.sqrt(2) / 2, 0)]]
    if cm.PruebaSiUnitaria(U1) and cm.PruebaSiUnitaria(U2):
        MultiplcaU1U2 = cm.MultiplicacionMatrices(U1, U2)
        MultiplcaU2U1 = cm.MultiplicacionMatrices(U2, U1)
        if cm.PruebaSiUnitaria(MultiplcaU1U2) and cm.PruebaSiUnitaria(MultiplcaU2U1):
            print('Las matrices U1 y U2 al igual que su producto son unitarias')
    else:
        print('Las matrices no son unitarias')


def Ejer4_4_2():
    mapaUnitario = [[(0, 0), (1 / (2 ** 0.5), 0), (1 / (2 ** 0.5), 0), (0, 0)],
                    [(0, 1 / (2 ** 0.5)), (0, 0), (0, 0), (1 / (2 ** 0.5), 0)],
                    [(1 / (2 ** 0.5), 0), (0, 0), (0, 0), (0, 1 / (2 ** 0.5))],
                    [(0, 0), (1 / (2 ** 0.5), 0), (-1 / (2 ** 0.5), 0), (0, 0)]]
    inicial = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]
    if cm.PruebaSiUnitaria(mapaUnitario):
        dina = r.UnitariaDinamica(3, mapaUnitario, inicial)
        pos = r.ProbabilidadParticula(dina, 3)
        print('El estado final despues de 3 pasos es: ', dina)
        print('La probabilidad de que este en la posicion 3 es de: ', pos)
    else:
        print('El mapa no es unitario')


def main():
    Sim4_1()
    Ejer4_3_1()
    Ejer4_3_2()
    Ejer4_4_1()
    #Ejer4_4_2()  Presenta fallos.


main()
