import sys 
import os
import numpy
import h5py
import matplotlib.pyplot as plt


def ClearXML(folder):
    f=[]
    contador=0
    for files in os.listdir(folder):
        if files.endswith('.xml'):
            f.append(folder+'/'+files)
            os.remove(folder+'/'+files)
            contador=contador+1
    salida='Se han borrado '+str(contador)+' archivos .xml'
    return salida 

def ClearH5(folder):
    f=[]
    contador=0
    for files in os.listdir(folder):
        if files.endswith('.h5'):
            f.append(folder+'/'+files)
            os.remove(folder+'/'+files)
            contador=contador+1
    salida='Se han borrado '+str(contador)+' archivos .h5'
    return salida 


def Data(file):
    """extrae la magnetizacion y la energia del gs de un archivo que se pasa como entrada """
    h5files=h5py.File(file,'r')
    energias=h5files['spectrum/energies'].value
    m=h5files['parameters/Sz_total'].value
    return [m,energias[0]]


def Datamps(file,iterations):
    """extrae la magnetizacion y la energia del gs"""
    h5files=h5py.File(file,'r')
    energias=h5files['spectrum/results/Energy/mean/value'].value
    m=h5files['parameters/Sz_total'].value
    return [m,energias[0]]	


def Datafiles(folder):
    f=[]
    for files in os.listdir(folder):
        if files.endswith('.out.h5'):
            f.append(folder+'/'+files)
    return f 

def Clearfiles(folder,ext):
    f=[]
    for files in os.listdir(folder):
        if files.endswith('.'+str(ext)):
            os.remove(folder+'/'+files)
    return f   
   

def result(folder):
    """
    result(folder):
    Extrae la magnetizacion y la energia del gs de todos los archivos que estan en la carpeta que se pasa como entrada 
    
    Dependencias:
    Usa la funcion Data(file):
    """
    f=[]
    for files in os.listdir(folder):
        if files.endswith('h5'):
            f.append(folder+'/'+files)            
    archivos=[]
    for files in f:
        archivos.append(Data(files))    
    final=numpy.array(archivos)        
#    np.savetxt(folder+'/'+str(name)+'.dat',final)
    return final

def resultmps(folder,iterations):
    f=Datafiles(folder)  
    archivos=[]  
    for files in f:
        archivos.append(Datamps(files,iterations))    
    final=numpy.array(archivos)        
#    np.savetxt(folder+'/'+str(name)+'.dat',final)
    return final

def hs(array,h):  
    """recibe de argumentos el array con columnas (m,E0) y h es un array con los campos"""
    puntos=[]
    for i in h:
        rectas=array.T[1]-array.T[0]*i
        minimo=numpy.min(rectas)
        pos=array.T[0][numpy.argmin(rectas)]
        puntos.append([i,minimo,pos])
    pun=numpy.array(numpy.array(puntos))
    return numpy.array([pun[:,0],pun[:,2]]).T


def alerta():
	os.system('beep -f 349; sleep 0.30; beep -f 415.3; sleep 0.165; beep -f 349; beep -f 349 -l 170; beep -f 466.2; sleep 0.05; beep -f 349; sleep 0.05; beep -f 311.1; sleep 0.05; beep -f 349; sleep 0.33; beep -f 523.2; sleep 0.165; beep -f 349; beep -f 349 -l 170; beep -f 550; sleep 0.05; beep -f 523.2; sleep 0.05; beep -f 415.3; sleep 0.05; beep -f 349; sleep 0.05; beep -f 523.2; sleep 0.05; beep -f 698.4; sleep 0.03; beep -f 349 -l 170; beep -f 311.1 ; beep -f 311.1 -l 170; sleep 0.05; beep -f 261.6; sleep 0.03; beep -f 392; sleep 0.03; beep -f 349 -l 750;')
	return 0
