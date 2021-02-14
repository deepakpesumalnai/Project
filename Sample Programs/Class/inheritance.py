from Simpleclass import Person

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

class man(Person):
	def test(self):
		print('child')
		super(man,self).greet()
		#Person.greet()

deepak = man()
print("sample")
deepak.test()