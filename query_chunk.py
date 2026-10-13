import astropy.time as ti 
import astropy.table as tb
from astroquery.jplhorizons import Horizons

def query_chunk(table, objname, ndata = 50):
	res = []
	for i in range(int(len(table)/ndata) + 1):
		obj = Horizons(objname, location = 'X05', epochs = table[i * ndata : (i+1)*(ndata)]['obstime'].jd)
		e = obj.ephemerides()
		res.append(e)
	res = tb.vstack(res)
	return res
        
