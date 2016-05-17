#!/usr/bin/python
# Filename: __init__.py
import numpy as np 

import humidity as hum
from radiation import *
from air import *
from physdyn import *
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == '__main__':
	
	temperatures_C=np.arange(-50,50,1)
	temperatures_K=temperatures_C+273.
	
	# in Pascal
	psat_Pa=hum.esat(temperatures_K) 
#	psat2_Pa=hum.esat2(temperatures_K) 
	psat_hPa=psat_Pa/100.
#	psat2_hPa=psat2_Pa/100.
	plt.plot(temperatures_C,psat_hPa,label='full formula')
#	plt.plot(temperatures_C,psat2_hPa,label='approxilated formula')
	plt.xlabel('Temperature in $^o$C')
	plt.ylabel('Saturating Pressure in hPa')
	plt.title('Saturating pressure')
	plt.legend()
	