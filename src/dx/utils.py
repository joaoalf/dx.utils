import ConfigParser
import os
import time
import string

class Config(object):
    """
    classe: Utils
    Utilitarios gerais.
    """    
    ##getConfigDefaults = staticmethod(getConfigDefaults)
    ##leConfig = staticmethod(leConfig)
    
    def getConfigDefaults():
        if os.name == 'nt':
            return self._ConfigDefaultsWin32
        else:
            return self._ConfigDefaultsLinux
    getConfigDefaults = staticmethod(getConfigDefaults)
	
    def leConfig(arquivo, config={}):
        """
        Retorna um dicionario com os valores do arquivo de configuracao.
        """

        config = config.copy()
        cp = ConfigParser.ConfigParser()
        cp.read(arquivo)
        for sec in cp.sections():
            name = string.lower(sec)
            for opt in cp.options(sec):
                config[name + '.' + string.lower(opt)] = string.strip(cp.get(sec, opt))
        return config

    leConfig = staticmethod(leConfig)

class Log(object):
	"""
	classe: Log

	Loga os eventos do sistema.
	"""

	def __init__(self, lf, size_to_rotate=100000):
		if os.path.exists(lf):
			if os.path.getsize(lf) > size_to_rotate:
				import zipfile
				zfile = zipfile.ZipFile(lf[:-4]+'.zip', 'w')
				zfile.write(lf)
				zfile.close()
				os.unlink(lf)
		self.log = file(lf, 'a+')
		        	
	def __del__(self):
		self.log.flush()
		self.log.close()

	def logEvento(self,evento):
		self.log.write(time.strftime('%c') + ': ' + evento + '\n')
		self.log.flush()
		return 0

if os.name == 'nt':
    import win32con, win32file, pywintypes
    LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
    LOCK_SH = 0
    LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
    __overlapped = pywintypes.OVERLAPPED()

    def lock(file, flags):
        try:
            hfile = win32file._get_osfhandle(file.fileno())
            win32file.LockFileEx(hfile, flags, 0, 0xffff0000, __overlapped)
        except:
            pass

    def unlock(file):
        try:
            hfile = win32file._get_osfhandle(file.fileno())
            win32file.UnlockFileEx(hfile, 0, 0xffff0000, __overlapped)
        except:
            pass

elif os.name == 'posix':
    import fcntl
    from fcntl import LOCK_EX, LOCK_SH, LOCK_NB

    def lock(file, flags):
        fcntl.flock(file.fileno(), flags)

    def unlock(file):
        fcntl.flock(file.fileno(), fcntl.LOCK_UN)


            
