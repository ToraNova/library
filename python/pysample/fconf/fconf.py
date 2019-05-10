import os,shutil

#FileConfig module
#supports writing of strings/integer as config values
#to a filesystem

class FileConfig():

	#moduename and a pkgprint define
	moduname = "fconf"
	def pkgprint(self,*args,**kwargs):
		print("[{}]".format(self.moduname),*args)

	CHECKTYPE_FILE = True
	CHECKTYPE_DIR = False

	def checkExist(self,file_dir,bool_file):
		#file_dir : filename/dirname that we check
		#bool_dir : are we checking for a file or a dir ? true for file
		return ( os.path.exists( file_dir ) and (os.path.isdir(file_dir) or bool_file))
		

	def __init__(self,typename,verbose=False):
		self.tname = typename
		self.verboseprint = self.pkgprint if verbose else lambda *a, **k: None
		#check if dir exists (relative to root)
		if(self.checkExist(typename,self.CHECKTYPE_DIR)):
			#already exist, do nothing
			self.verboseprint("Config class already exist. skipping creation")
			pass
		else:
			#create the directory
			self.verboseprint("Creating config class",typename)
			os.makedirs(self.tname,0o777)

	def listconfigs(self):
		#return list of configs in the type
		configs = [f for f in listdir(self.tname) if isfile(join(self.tname, f))]
		return configs
	
	def wipetype(self):
		#wipe clean a configtype - DELETE THIS CONFIG ! WARNING
		wipe = os.path.join(self.tname)
		self.verboseprint("Removing",wipe)
		shutil.rmtree(wipe)

	def wipeconf(self,configname):
		wipe = os.path.join(self.tname,configname)
		if(self.checkExist(wipe,self.CHECKTYPE_FILE)):
			self.verboseprint("Removing",wipe)
			os.remove(wipe)
		else:
			self.verboseprint(wipe,"does not exist")

	def writeconf(self,configname,configitems):
		#writes to fileconfig. configitem must be a dictionary
		write = os.path.join(self.tname,configname)
		if(type(configitems) != dict or not len(configitems) > 0):
			#wrong input
			self.verboseprint("Invalid Input for writeconf")
			return False #return false on error
		else:
			with open(write,'w') as f:
				#overwrite the entire file
				for key,val in configitems.items():
					try:
						if(type(val) == int):
							val = str(val)
						configline = key+'='+str(val)+'\n'
						f.write(configline)
					except Exception as e:
						self.verboseprint("Invalid config dictionary @",key,":",val,":",str(e))
			return True

	def readconf(self,configname):
		#reads the configfile and returns a 
		#dictionary of config items
		read = os.path.join(self.tname,configname)
		outdict = {}
		if(self.checkExist( read, self.CHECKTYPE_FILE)):
			with open(read,'r') as f:
    				configlist = f.readlines()
			for idx,config in enumerate(configlist):
				try:
					outdict[config.split('=')[0]] = config.split('=')[1]
				except Exception as e:
					self.verboseprint("Invalid config statement @ line",idx,"from fconf class",self.tname,
						":",config,"Exception",str(e))
					return None
			if(len(outdict)==0):
				return None
			else:
				return outdict		
		else:
			return None #return none on failure (dir not exist/ config item not exist)
		
if __name__ == "__main__":
	
	cc1 = FileConfig("test",True)
	
	a = cc1.readconf("config0")
	print(a)
	b = {"key0":"val0","key1":3}

	cc1.writeconf("config0",b)
	
	a = cc1.readconf("config1")
	print(a)
	a = cc1.readconf("config0")
	print(a)

	cc1.wipeconf("config0")
	cc1.wipeconf("config1")
	cc1.wipetype()

	
	
	
