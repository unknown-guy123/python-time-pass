# Accessing Class Variable from outside Class
class Mobile:
	fp = 'Yes'								# Class Variable
	
	def __init__(self):
		self.model = 'RealMe X'					# Instance Variable
	
	def show_model(self):						# Instance Method
		print("Model:",self.model)				# Accessing Instance Variable
		
	@classmethod								# Class Method
	def is_fp(cls):
		print("Finger Print:", cls.fp)		# Accessing Class Variable

		
realme = Mobile()
realme.show_model()
Mobile.is_fp()
print()
Mobile.fp = 'No'			# Accessing Class Variable from outside Class
Mobile.is_fp()
print("\nhelllllllo")
Mobile.is_fp()


