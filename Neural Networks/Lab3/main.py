import copy
import math
import pathlib
import re
from typing import Any


def load_system(path) -> tuple[list[list[float]], list[float]]:
    a=[]
    b=[]
    with open(path, "r") as file:
        content = file.read().splitlines()
        for line in content:
            line = line.strip().replace(" ","")
            left, right = line.split("=")
            b.append(float(right))

            row = []

            for var in ['x','y','z']:
                match = re.search(rf'([+-]?\d*){var}', left)
                if match:
                    coef = match.group(1)
                    if coef in ("", "+"):
                        row.append(1)
                    elif coef == "-":
                        row.append(-1)
                    else:
                        row.append(float(coef))
                else:
                    row.append(0)
            a.append(row)
    return a,b


def determinant_3x3(a:list[list[float]]) -> float:
    return a[0][0]*(a[1][1]*a[2][2] - a[1][2]*a[2][1]) - a[0][1]*(a[1][0]*a[2][2] - a[1][2]*a[2][0]) + a[0][2]*(a[1][0]*a[2][1] - a[1][1]*a[2][0])

def determinant_2x2(m: list[list[float]]) -> float:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def trace_3x3(a:list[list[float]]) -> float:
    return a[0][0]+a[1][1]+a[2][2]

def vector_norm_3x3(a:list[float]) -> float:
    return math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])

def transpose_3x3(a:list[list[float]]) -> list[list[float]]:
    return [[a[0][0],a[1][0],a[2][0]],
            [a[0][1],a[1][1],a[2][1]],
            [a[0][2],a[1][2],a[2][2]]]

def multiply_3x3(a:list[list[float]],b:list[float]) -> list[float]:
    return [a[0][0]*b[0] + a[0][1]*b[1] + a[0][2]*b[2],
            a[1][0]*b[0] + a[1][1]*b[1] + a[1][2]*b[2],
            a[2][0]*b[0] + a[2][1]*b[1] + a[2][2]*b[2]]

def replace(a:list[list[float]],b:list[float],rep:int) -> list[list[float]]:
    a_copy = copy.deepcopy(a)
    match rep:
        case 1: a_copy[0] = b; return a_copy
        case 2: a_copy[1] = b; return a_copy
        case 3: a_copy[2] = b; return a_copy
        case _: return []

def cramer(a:list[list[float]], b:list[float]) -> list[float]:
    if determinant_3x3(a) == 0:
        raise ZeroDivisionError("Determinant cannot be zero")
    return [determinant_3x3(replace(a,b,1)) / determinant_3x3(a),
            determinant_3x3(replace(a,b,2)) / determinant_3x3(a),
            determinant_3x3(replace(a,b,3)) / determinant_3x3(a)]

def minor(a:list[list[float]],i:int,j:int) -> list[list[float]]:
    return [[a[r][c] for c in range(3) if c!=j] for r in range(3) if r!=i]

def cofactor(a:list[list[float]]) -> Any:
    cofactors = [[0] * 3 for _ in range(3)]
    for i in range (3):
        for j in range (3):
            sub_matrix = minor(a,i,j)
            cofactors[i][j] = determinant_2x2(sub_matrix) * pow(-1,i+j)
    return cofactors

def adjoint(a:list[list[float]]) -> list[list[float]]:
    return transpose_3x3(cofactor(a))

def solve(a:list[list[float]],b:list[float]) -> Any:
    if determinant_3x3(a) == 0:
        raise ZeroDivisionError("Determinant cannot be zero")
    adj = adjoint(a)
    mult = multiply_3x3(adj,b)
    return [val / determinant_3x3(a) for val in mult]

A, B = load_system(pathlib.Path("C:/Users/colin/Desktop/Repos/Python Repo/Neural Networks/Lab3/text"))
print(f"{A=}\n{B=}")
print(f"Determinant:{determinant_3x3(A)}")
print(f"Trace:{trace_3x3(A)}")
print(f"Vector norm:{vector_norm_3x3(B)}")
print(f"Transpose:{transpose_3x3(A)}")
print(f"Multiply:{multiply_3x3(A,B)}")

print(f"Replace:{replace(A,B,1)}")
print(f"Cramer:{cramer(A,B)}")
print(f"Minor:{minor(A,1,1)}")
print(f"Cofactor{cofactor(A)}")
print(f"Adjoint{adjoint(A)}")
print(f"Solve:{solve(A,B)}")
