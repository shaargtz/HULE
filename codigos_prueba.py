codigo_1 = '''
var ent a, b;
func vacia imprime_x_veces(cadena w, ent veces) {
    var ent cont;
    cont = 0;
    mientras (cont < veces) {
        imprime(w);
        cont = cont + 1;
    }
};
func ent exponente(ent base, ent exp) {
    var ent res;
    res = 1;
    mientras (exp > 0) {
        res = res * base;
        exp = exp - 1;
    }
    regresa res;
};
hule() 
{
    var ent c;
    a = 3;
    b = 4;
    c = a + b;
    mientras (c > b){
        b = b + 1;
        a = a * 2;
    }
    si (a / 3 > 10) {
        imprime('aaa');
    } sino {
        imprime('bbb');
    }
    imprime(c);
    imprime(a);
    imprime_x_veces('hola', 5);
    imprime(exponente(3, exponente(2, 3)));
}
'''

codigo_2 = '''
hule() 
{
    var ent A[5], cont, b, c;
    b = 3;
    A[0] = 13;
    A[1] = 6;
    A[2] = 9;
    A[3] = 2;
    A[4] = A[b * A[3] - 4];

    c = A[0] + A[1] + A[2] + A[3] + A[4];
    imprime(c);

    cont = 0;

    mientras(cont < 5) {
        imprime(A[cont]);
        cont = cont + 1;
    }
}
'''

codigo_3 = '''
hule() 
{
    var ent A[2][3], i, j;

    i = 0;
    j = 0;

    mientras(i < 2) {
        mientras(j < 3) {
            A[i][j] = i + j;
            j = j + 1;
        }
        j = 0;
        i = i + 1;
    }

    i = 0;
    j = 0;

    mientras(j < 3) {
        mientras(i < 2) {
           imprime(A[i][j]);
           i = i + 1;
        }
        i = 0;
        j = j + 1;
    }

    
}
'''

codigo_4 = '''
hule() 
{
    var ent A[2][3][4], i, j, k;

    i = 0;
    j = 0;
    k = 0;

    mientras(i < 2) {
        mientras(j < 3) {
            mientras (k < 4) {
                A[i][j][k] = i + j + k;
                k = k + 1;
            }
            k = 0;
            j = j + 1;
        }
        j = 0;
        i = i + 1;
    }

    i = 0;
    j = 0;
    k = 0;

    mientras(i < 2) {
        mientras(j < 3) {
            mientras (k < 4) {
                imprime(A[i][j][k]);
                k = k + 1;
            }
            k = 0;
            j = j + 1;
        }
        j = 0;
        i = i + 1;
    }

    var ent x;
    x = 8;

    imprime('-----');
    imprime(A[0][0][0]);
    imprime(A[(x / 2) - 3][A[0][x - 8][0]][3]);
}
'''

codigo_5 = '''
hule() {
    var ent A[5];
    por(i en 5) {
        A[i] = i * i;
    }

    por(j en 5) {
        imprime(A[4 - j]);
    }
}
'''

codigo_6 = '''
hule() {
    var ent A[5];
    var flot B[5];
    por(i en 5) {
        A[i] = aleatorio(5, 10);
    }

    por(j en 5) {
        imprime(A[4 - j]);
    }

    imprime('-------');

    imprime(poder(2, 4));

    imprime('-------');

    imprime(min(A[4], A[3]));

    imprime('-------');

    imprime(largo(A));

    imprime('-------');

    imprime(media(A));
    imprime(moda(A));
    imprime(mediana(A));

    imprime('-------');

    graficar(A);
}
'''

codigo_7 = '''
hule() {
    var ent A[5];
    por(i en 5) {
        A[i] = aleatorio(1, 5);
    }

    var cadena B[5];
    B[0] = 'aaa';
    B[1] = 'bbb';
    B[2] = 'ccc';
    B[3] = 'ddd';
    B[4] = 'eee';

    graficar(A, B);
}
'''

codigo_8 = '''
func vacia f(ent a) {
    imprime(a);
    f(a + 1);
};
hule() {
    f(1);
}
'''

codigo_9 = '''
hule() {
    var ent A[1001];
    por (i en 1001) {
        A[i] = i;
    }
}
'''

codigo_10 = '''
hule() {
    var ent a;
    imprime('numero:');
    a = ent(lee());
    imprime('-------');
    por(i en 5) {
        imprime(a + i);
    }
}
'''

fib_rec = '''
func ent fib(ent a) {
    si (a == 1 | a == 2) {
        regresa 1;
    } sino {
        regresa fib(a - 1) + fib(a - 2);
    }
};

hule() {
    imprime(fib(10));
}
'''

fib_iter = '''
func ent fib(ent a) {
    si (a == 1 | a == 2) {
        regresa 1;
    }
    var ent A[2], acum;
    acum = 0;
    A[0] = 1;
    A[1] = 1;
    por(i en a) {
        si (i > 1) {
            acum = A[0] + A[1];
            A[0] = A[1];
            A[1] = acum;
        }
    }
    regresa A[1];
};

hule() {
    imprime(fib(10));
}
'''

fact_rec = '''
func ent fact(ent a) {
    si (a == 1 | a == 0) {
        regresa 1;
    } sino {
        regresa a * fact(a - 1);
    }
};
hule() 
{
    imprime(fact(10));
}
'''

fact_iter = '''
func ent fact(ent a) {
    var ent acum;
    acum = 1;
    por (i en a) {
        acum = acum * (i + 1);
    }
    regresa acum;
};
hule() 
{
    imprime(fact(10));
}
'''

sort = '''
hule() {
    var ent arreglo[10], aux;
    por (a en largo(arreglo)) {
        arreglo[a] = aleatorio(1, 10);
        imprime(arreglo[a]);
    }
    imprime('sorteado:');
    por (i en largo(arreglo) - 1) {
        por (j en largo(arreglo) - i + 1) {
            si (arreglo[j] > arreglo[j + 1]) {
                aux = arreglo[j + 1];
                arreglo[j + 1] = arreglo[j];
                arreglo[j] = aux;
            }
        }
    }
    por (b en largo(arreglo)) {
        imprime(arreglo[b]);
    }
}
'''

find = '''
hule() {
    var ent arreglo[10], aux, busqueda, indice;
    por (a en largo(arreglo)) {
        arreglo[a] = aleatorio(1, 10);
        imprime(arreglo[a]);
    }
    indice = -1;
    imprime('valor a buscar:');
    busqueda = ent(lee());
    por (i en largo(arreglo)) {
        si (arreglo[largo(arreglo) - (i + 1)] == busqueda) {
            indice = largo(arreglo) - (i + 1);
        }
    }
    imprime('--------');
    si (indice == -1) {
        imprime('no se encontro el valor');
    } sino {
        imprime(indice);
    }
}
'''

matrix_mult = '''
hule() {
    var ent A[3][3], B[3][3], res[3][3];
    var cadena a, b, c;
    imprime('MATRIZ A');
    por (x1 en 3) {
        a = '| ';
        por (y1 en 3) {
            A[x1][y1] = aleatorio(1, 10);
            a = a + cadena(A[x1][y1]) + ' ';
        }
        imprime(a);
    }
    imprime('MATRIZ B');
    por (x2 en 3) {
        b = '| ';
        por (y2 en 3) {
            B[x2][y2] = aleatorio(1, 10);
            b = b + cadena(B[x2][y2]) + ' ';
        }
        imprime(b);
    }
    imprime('MATRIZ AxB');
    por (i en 3) {
        c = '| ';
        por (j en 3) {
            res[i][j] = 0;
            por (k en 3) {
                res[i][j] = res[i][j] + A[i][k] * B[k][j];
            }
            c = c + cadena(res[i][j]) + ' ';
        }
        imprime(c);
    }
}
'''

grafica_edades = '''
hule() {
    var ent frecuencias[5];
    var cadena edades[5];
    por (i en largo(frecuencias)) {
        frecuencias[i] = aleatorio(5, 10);
    }
    por (j en largo(edades)) {
        edades[j] = cadena(j + 18) + ' años';
    }
    graficar(frecuencias, edades);
}
'''

calculos_estadisticos = '''
hule() {
    var cadena c;
    c = 'estaturas: ';
    var ent estaturas[10];
    por (i en largo(estaturas)) {
        estaturas[i] = aleatorio(160, 200);
        c = c + cadena(estaturas[i]) + ', ';
    }
    imprime(c);
    imprime('media: ' + cadena(media(estaturas)));
    imprime('moda: ' + cadena(moda(estaturas)));
    imprime('mediana: ' + cadena(mediana(estaturas)));
}
'''

calculos_aritmeticos = '''
hule() {
    var cadena a, b;
    imprime('a:');
    a = lee();
    imprime('b:');
    b = lee();

    imprime(a + ' ^ ' + b + ' = ' + cadena(poder(ent(a), ent(b))));
    imprime('log ' + b + ' = ' + cadena(log(ent(b))));
    imprime('abs(' + a + ') = ' + cadena(abs(ent(a))));
}
'''