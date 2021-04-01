import ComplexL as cm
import numpy as np
import math as m
from matplotlib import pyplot as pl


def ProbabilidadParticula(ket, pos):
    prob = cm.ModuloComplejos(ket[pos]) ** 2 / cm.NormaVector(ket) ** 2
    return prob



def AmplitudTransicion(ket1, ket2):
    bra = cm.AdjuntaVector(ket2)
    amplitud = cm.MultiplicacionVectores(bra, ket1)
    normaket1 = cm.NormaVector(ket1)
    normaket2 = cm.NormaVector(ket2)
    am = cm.DivisionComplejos(amplitud, cm.MultiplicacionComplejos((normaket1, 0),(normaket2, 0)))
    return am


def ValorEsperadoVarianza(mat, ket):
    if cm.PruebaSiHermitiana(mat):
        bra = cm.AdjuntaVector(ket)
        miu = cm.MultiplicacionVectores(bra, ket)
        iden = cm.MatrizIdentidad(len(mat))
        matmiu = cm.EscalarPorMatriz(miu, iden)
        suma = cm.SumaMatrices(mat, cm.InversaAditMat(matmiu))
        cuad = cm.MultiplicacionMatrices(suma, suma)
        varianza = cm.MatVec(cm.MatVec(cuad, ket))
        res = miu[0], varianza[0][0]
    else:
        res = 'La matriz no es hermitiana'
    return res


def ValoresPropios(observable):
    mat = np.array(observable)
    val = np.linalg.eig(mat)
    valores = list()
    for i in range(0, len(val[0])):
        valores += [(val[0][i].real, val[0][i].imag)]
    return valores


def NormalizaVec(vec):
    vecN = list()
    vc = list()
    norma = cm.NormaVector(vec)
    for i in range(0, len(vec)):
        vc.append(cm.MultiplicacionComplejos((1/norma,0), vec[i]))
    return vc


def VecNormalizado(observable):
    mat = np.array(observable)
    val = np.linalg.eig(mat)
    vectores = list()
    for i in range(0, len(val[1])):
        vec = list()
        for j in range(0, len(val[1][i])):
            vec.append((val[1][i][j].real, val[1][i][j].imag))
        vectores.append(vec)
    VectsNorm = []
    for i in range(0, len(vectores)):
        VectsNorm.append(NormalizaVec(vectores[i]))
    return VectsNorm


def ProbabilidadValPropios(vecEstado, vecPropio):
    probabilidad = list()
    bra = cm.AdjuntaVector(vecEstado)
    for i in range(0, len(vecPropio)):
        probabilidad.append([((cm.ModuloComplejos(cm.MatVec(vecPropio, bra)[0]))**2, 0)])
    vec = list()
    for i in probabilidad:
        vec.append(i[0])
    return vec


def ValorMedio(prob, valProp):
    med = list()
    resp = (0, 0)
    for i in range(0, len(prob)):
        med.append(cm.MultiplicacionComplejos(prob[i], valProp[i]))
    for j in range(0, len(med)):
        resp = cm.SumaComplejos(med[i], resp)
    return resp


def Graficar(vec):
    probabilidad = [i for i in range(0, len(vec))]
    vector = [vec[i][0] for i in range(0, len(vec))]
    pl.bar(probabilidad, vector, color= 'red')
    pl.show()


def UnitariaDinamica(pasos, mat, estadoInicial):
    if cm.PruebaSiUnitaria(mat):
        if pasos == 1:
            res = cm.MatVec(mat, estadoInicial)
        else:
            for i in range(0, pasos):
                mat = cm.MultiplicacionMatrices(mat, mat)
            res = cm.MatVec(mat, estadoInicial)
    else:
        res = 'Matriz no unitaria'
    return res


def Probabilidad(c):
    return cm.ModuloComplejos(c)**2