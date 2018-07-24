bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#print(bicycles[0])
#print(bicycles[-1])
#message="my first bicycle is:"+bicycles[0].title()+'.'
#print(message)
#names=['ymy','wxj','sjq','dlrb']
#print(names[0])
#print(names[1])
#print(names[2])
#print(names[3])
#message='Hello,'
#print(message+names[0])
#print(message+names[1])
#print(message+names[2])
#print(message+names[3])
#traffic=['bicycle','car','plane','train']
#print("I would like to own a "+traffic[1])
bicycles[0]='ducati'
print(bicycles)
bicycles.append('honda')
print(bicycles)
bicycles.insert(1,'yamaha')
print(bicycles)
del bicycles[0]
print(bicycles)
a=bicycles.pop()
print(a)
print(bicycles)
bicycles.remove('yamaha')
print(bicycles)
