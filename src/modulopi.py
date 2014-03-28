#!/usr/bin/pytho
import sys
def aproximacion(n):
   PI=3.1415926535897931159979634685441852
   suma=0.0
   for i in range(1,n+1):
      x_i=float(i-1.0/2)/(n)
      fx_i=4.0/(1+x_i**2)
      suma=suma + fx_i
   pi=(1.0/float(n))*suma
   return pi
   
def error (nro_intervalos, nro_test, umbral):
   intervalo = nro_intervalos
   lista = []
   for i in range (nro_test):
      valor_pi = calcular_pi (intervalo)
      intervalo += nro_intervalos
      lista.append (valor_pi)
   pi35= []
   for i in range (nro_test):
      pi35.append (pi35DT)
      dif35 = []
      for i in range (nro_test):
	  dif35.append (abs(pi35[i] -lista[i]))
      valor=0
   for i in range (nro_test):
      if (dif35[i]<= umbral1):
	valor = valor + 1
   porcentaje= 100.0*(1.0-(float (valor) / float(nro_test)))
   return (porcentaje)
    
if __name__ == "__main__":     
  if len (sys.argv)==3:
    n=sys.argv[1]
    m=sys.argv[2]
  else:
    print 'El modo de uno es:modulo1.py valor 1 y 2'
    n=5
    m=10
   for repetir in range(1,veces+1):
     api=aproximacion(n)
     a=a+[api]
     resta=aproximacion(n) - Pi
     print'%d %1.35f | %1.35f | %1.35f' % (repetir, Pi, aproximacion(n), resta)
     n=n*2
   print a