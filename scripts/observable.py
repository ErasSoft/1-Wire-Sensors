class Observable(object):
	__DEBUG = False	

	def __init__(self):
		self._observers = []

	def attach(self, observer):
		if observer not in self._observers:
			self._observers.append(observer)
			if Observable.__DEBUG:
				print("[Observable] attached " + str(observer))

	def detach(self, observer):
		try:
			self._observers.remove(observer)
		except ValueError:
			pass

	def notify(self, modifier=None):
		for observer in self._observers:
			if modifier != observer:
				if Observable.__DEBUG:
					print ("[Observable] update " + str(observer))
				observer.update(self)
