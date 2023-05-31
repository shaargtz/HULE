codigo_1 = '''
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
    imprime(3 - (4 * (5 - 2)));
}
'''

codigo_2 = '''
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

codigo_3 = '''
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

codigo_4 = '''
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

codigo_5 = '''
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

codigo_6 = '''
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

codigo_7 = '''
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