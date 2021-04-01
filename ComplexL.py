import math as m


#                               Operaciones con números complejos


def SumaComplejos(c1, c2):
    '''
    Los parametros c1 y c2 son números complejos
    Función que suma números complejos
    '''
    return c1[0] + c2[0], c1[1] + c2[1]


def MultiplicacionComplejos(c1, c2):
    '''
    Los parametros c1 y c2 son números complejos
    Función que multiplica números complejos
    '''
    return c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1]


def RestaComplejos(c1, c2):
    '''
    Los parametros c1 y c2 son números complejos
    Función que resta números complejos
    '''
    return c1[0] - c2[0], c1[1] - c2[1]


def DivisionComplejos(c1, c2):
    '''
    Los parametros c1 y c2 son números complejos
    Función que divide números complejos
    '''
    r1 = c1[0] * c2[0] + c1[1] * c2[1]
    r2 = c2[0] * c1[1] - c1[0] * c2[1]
    div = c2[0] ** 2 + c2[1] ** 2
    return r1 / div, r2 / div


def ModuloComplejos(c):
    '''
    El parámetro c es un número complejo
    Función que calcula el modulo de un número complejo
    '''
    return m.sqrt(c[0] ** 2 + c[1] ** 2)


def ConjugadoComplejos(c):
    '''
    El parámetro c es un número complejo
    Función que calcula el conjugado de un número complejo
    '''
    return c[0], -c[1]


#                               Transformaciones entre Grados y Radianes


def GradosRad(dat):
    '''
    El parámetro dat es un ángulo
    Función que transforma de grados a radianes
    '''
    return (dat * m.pi) / 180


def RadGrados(dat):
    '''
    El parámetro dat es un radian
    Función que transforma de radianes a grados
    '''
    return (dat * 180) / m.pi


#                               Transformaciones entre Cartesianas y Polares


def CartesianaPolar(c):
    '''
    El parámetro c es un número complejo
    Función que transforma de coordenadas cartesianas a polares
    '''
    return m.sqrt(c[0] ** 2 + c[1] ** 2), RadGrados(m.atan2(c[1], abs(c[0])))


def PolaCartesiano(p):
    '''
    El parámetro p es una coordenada polar
    Función que transforma de coordenadas polares a cartesianas
    '''
    return p[0] * m.cos(GradosRad(p[1])), p[0] * m.sin(GradosRad(p[1]))


def fase(c):
    '''
    El parámetro c es un número complejo
    Función que calcula la fase de un número complejo
    '''
    return m.atan2(c[1], c[0])


#                               Operaciones adicionales


def InvesoAditivoComplejo(c):
    '''
    El parámetro c es un número complejo
    Función que calcula el inverso aditivo de un número complejo
    '''
    return c[0] * -1, c[1] * -1


def MultiplicacionVectores(v1, v2):
    com = (0, 0)
    for i in range(0, len(v1)):
        com = SumaComplejos(com, MultiplicacionComplejos(v1[i], v2[i]))
    return com


def RestaVectores(v1, v2):
    '''
    Los parámetros v1 y v2 son vectores de mismo tamaño compuestos por números complejos
    Función que suma vectores
    '''
    vec = list()
    for i in range(0, len(v1)):
        vec.append(RestaComplejos(v1[i], v2[i]))
    return vec


#                               Operaciones para vectores y matrices complejas


def SumaVectores(v1, v2):
    '''
    Los parámetros v1 y v2 son vectores de mismo tamaño compuestos por números complejos
    Función que suma vectores
    '''
    vec = list()
    for i in range(0, len(v1)):
        vec.append(SumaComplejos(v1[i], v2[i]))
    return vec


def InversoAditivoVec(v):
    '''
    El parámetro v es un vector compuesto de números complejos
    Función que calcula el inverso aditivo de un vector complejo
    '''
    vec = list()
    for i in range(0, len(v)):
        vec.append(InvesoAditivoComplejo(v[i]))
    return vec


def VecEscalar(e, v):
    '''
    Los parámetros e y v son un número complejo y un vector de complejos respectivamente
    Función que multiplica un número complejo por un vector de complejos
    '''
    vec = list()
    for i in range(0, len(v)):
        vec.append(MultiplicacionComplejos(e, v[i]))
    return vec


def SumaMatrices(m1, m2):
    Mres = list()
    for i in range(0, len(m1)):
        vec = list()
        for j in range(0, len(m1)):
            vec.append(SumaComplejos(m1[i][j], m2[i][j]))
        Mres.append(vec)
    return Mres


def InversaAditMat(mat):
    Mres = list()
    for i in range(0, len(mat)):
        vec = list()
        for j in range(0, len(mat)):
            vec.append(InvesoAditivoComplejo(mat[i][j]))
        Mres.append(vec)
    return Mres


def EscalarPorMatriz(c, mat):
    resu = list()
    for i in range(0, len(mat)):
        vec = list()
        for j in range(0, len(mat)):
            vec.append(MultiplicacionComplejos(c, mat[i][j]))
        resu.append(vec)
    return resu


def TraspuestaMat(mat):
    resu = [[0] * len(mat) for i in range(0, len(mat[0]))]
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            resu[j][i] = mat[i][j]
    return resu


def ConjugadaVector(v):
    vec = list()
    for i in v:
        vec.append(ConjugadoComplejos(i))
    return vec


def ConjugadaMatriz(m):
    mat = list()
    for i in range(0, len(m)):
        mat.append(ConjugadaVector(m[i]))
    return mat


def AdjuntaVector(v):
    return ConjugadaVector(v)


def AdjuntaMatTransConj(m):
    return TraspuestaMat(ConjugadaMatriz(m))


def AdjuntaMatConjTrans(m):
    return ConjugadaMatriz(TraspuestaMat(m))


def MultiplicacionMatrices(m1, m2):
    mat = list()
    for i in range(0, len(m1)):
        fila = list()
        for j in range(len(m2[0])):
            complejo = (0, 0)
            for k in range(len(m2)):
                mult = MultiplicacionComplejos(m1[k][i], m2[j][k])
                complejo = SumaComplejos(mult, complejo)
            fila.append(complejo)
        mat.append(fila)
    return TraspuestaMat(mat)


def ProductoInternoVectores(v1, v2):
    vec = AdjuntaVector(v1)
    return MultiplicacionVectores(vec, v2)


def NormaVector(v):
    norma = ProductoInternoVectores(v, v)
    return m.sqrt(norma[0])


def DistanciaVectores(v1, v2):
    return NormaVector(RestaVectores(v1, v2))


def MatrizIdentidad(a):
    mat = [[(0, 0) for i in range(0, a)] for j in range(0, a)]
    for i in range(0, a):
        mat[i][i] = (1, 0)
    return mat


def PruebaSiUnitaria(m):
    mat = MultiplicacionMatrices(m, AdjuntaMatConjTrans(m))
    ide = MatrizIdentidad(len(m))
    matN = list()
    for i in range(0, len(mat)):
        vec = list()
        for j in range(0, len(mat)):
            pro = round(mat[i][j][0]), round(mat[i][j][1])
            vec.append(pro)
        matN.append(vec)
    if matN == MatrizIdentidad(len(m)):
        res = True
    else:
        res = False
    return res


def PruebaSiHermitiana(m):
    adjunta = AdjuntaMatTransConj(m)
    if adjunta == m:
        res = True
    else:
        res = False
    return res


def ProductoTensorVectores(v1, v2):
    vec = list()
    for i in range(0, len(v1)):
        for j in range(0, len(v2)):
            vec.append(MultiplicacionComplejos(v1[i], v2[j]))
    return vec


def ProductoTensorMatrices(m1, m2):
    m = len(m1)
    mn = len(m1[0])
    n = len(m2)
    nn = len(m2[0])
    mr = m * n
    nr = mn * nn
    matTensor = [[0 for i in range(mr)] for j in range(nr)]
    print(matTensor)
    for i in range(0, mr):
        for j in range(0, nr):
            matTensor[i][j] = MultiplicacionComplejos(m1[i // n][j // nn], m2[i % n][j % n])
    return matTensor


def MatVec(mat, vec):
    resu = list()
    trans = TraspuestaMat(mat)
    for i in range(0, len(mat)):
        sum = (0, 0)
        for j in range(0, len(mat)):
            mult = MultiplicacionComplejos(trans[i][j], vec[j])
            sum = SumaComplejos(sum, mult)
        resu.append(sum)
    return resu