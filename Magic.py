import matplotlib.image as mping
import numpy as np

def main():
	init = ["x", "x", "_", "x", "_", "x", "x", "x"]
	print(init)
	x=3000
	y=4000
	trials = x
	img = np.zeros((x, y, 3), dtype=np.float32)
	try:
		file = open("life.txt", 'a')
		file.write("\n~~~~~~~~~~HAA~~~~~~~~~~~\n")
	except:
		file = open("life.txt", 'w')
	init1 = []
	count = 0
	file.write("\n" + str(count) + ":	")
	for a in init:
			file.write(a)
	for i in range(trials):
		for a in range(len(init)):
			try:
				if init[a-1] == init[a+1]:
					init1.append("_")
				else:
					init1.append("x")
			except:
				if a == 0:
					if init[a] == "x":
						if init[a+1] == "x":
							init1.append("x")
							init1.append("x")
						if init[a+1] == "_":
							init1.append("_")
				if a == len(init)-1:
					if init[a] == "x":
						if init[a-1] == "x":
							init1.append("x")
							init1.append("x")
						if init[a-1] == "_":
							init1.append("_")
			#print(init1)
		init = init1
		init1 = []
		file.write("\n" + str(count) + ":	")
		c = 0
		for a in init:
			file.write(a)
			if a == "x":
				img[count, c] = 1
				img[x-count-1, y-c-1] = 1
			else:
				img[count, c] = 0
				img[x-count-1, y-c-1] = 0
			c += 1
		count += 1
	file.close()
	mping.imsave("overed.png", img)





if __name__ == '__main__':
	main()
		
		
