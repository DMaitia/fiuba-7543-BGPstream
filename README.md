# fiuba-7543-BGPstream

## 0 Instalación

Por favor vaya a [https://bgpstream.caida.org/v2-beta] y siga las instrucciones

## 1 Ejemplos

Es probable que antes de ejecutar el código deba insertar en siguiente comando en la terminal

```
export LD_LIBRARY_PATH=/usr/local/lib
```

### 1.1 Entrando en calor

[Ejemplo #1](../master/ejemplo_1.py)

### 1.2 Buscar upstream providers de la UBA (AS3449)

[Ejemplo #2](../master/ejemplo_2.py)

### 1.3 Buscar upstream providers del MIT (AS3)

[Ejemplo #3](../master/ejemplo_3.py)

### 1.4 Encontrar AS origen y AS-PATHS para un prefijo

[Ejemplo #4](../master/ejemplo_4.py)

## 2 Manos a la obra

**ANTES DE EMPEZAR**: Hallar el ASN de su proveedor de Internet. Se recomiendo utilizar https://bgp.he.net

Se pide que haga lo siguiente
1. Hallar todos los prefijos anunciados por su ISP residencial el día del cumpleaños del alumno en 2017
2. Explicar si se observaron prefijos desagregados (superposicion o prefijos contiguos)
3. Se pide averiguar quien es el AS origen de ```167.56.0.0/13```
4. Continuando con el punto anterior, se pide determinar quienes son los Transit Providers del AS origen

## Referencias

* Orsini, C., King, A., Giordano, D., Giotsas, V., & Dainotti, A. (2016, November). BGPStream: a software framework for live and historical BGP data analysis. In Proceedings of the 2016 Internet Measurement Conference (pp. 429-444). ACM.
* Demostración de BGPstream en TMA 2017 [https://github.com/CAIDA/bgpstream-tma-phdschool]
* Página web de BGPstream [https://bgpstream.caida.org] 
