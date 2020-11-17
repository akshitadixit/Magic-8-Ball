import random

c1 = []
c2 = []

positive = ['images/glow ('+str(x)+').png' for x in range(10)]
neutral = ['images/glow ('+str(x)+').png' for x in range(10,15)]
negative = ['images/glow ('+str(x)+').png' for x in range(15,20)]

def ANSWER():
	c1 = random.choice([positive, negative, neutral])
	c2 = random.choice(c1)
	return c2