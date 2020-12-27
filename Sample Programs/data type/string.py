
# double  quote
name = "test"
print(name)
print(type(name))
# single quote
name = 'testz1'
print(name)
print(type(name))
print(len(name))

print(name[4])
print(name[-2])

name = "123abc123abc"
print(name)
print(name[0:10:2])
print(type(name))
name = "123\tabc\t123\tabc"
print(name)

name = "123\nabc\n123\nabc"
print(name)
print(len(name))

name = "deepak"
print(name[::1])
print(name[::-1])
print(2+3)
print("2"+"3")
print("2" * 3)
print(2 * "3")

name = "This is a sample string"

print(name.split())
print(type(name.split()))

name = "This is a sample {}"
print(name.format("pen"))

name = "This is a {} {}"
print(name.format("Deepak","Pesumalani"))

name = "This is a {1} {0}"
print(name.format("Deepak","Pesumalani"))

name = "This is a {0} {0}"
print(name.format("Deepak","Pesumalani"))

Name = "This is a {name} {lastname}"
print(Name.format(name="Deepak",lastname= "Pesumalani"))

number = 800/7
print(number)
##print("result " + number)
print("result is {}".format(number))
print("result is {r}".format(r=number))
print("result is 1 {r:1.2f}".format(r=number))
print("result is 2 {r:2.2f}".format(r=number))
print("result is 3 {r:9.2f}".format(r=number))

name = "deepak"
last = f'name is {name}'
print(f'name is {name}')
print(last)

name = "pesumalani"
last = f'name is {name}'
print(last)
