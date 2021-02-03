from Simpleclass import Person

class man(Person):
	def test(self):
		print('child')
		super(man,self).greet()
		#Person.greet()

deepak = man()
print("sample")
deepak.test()