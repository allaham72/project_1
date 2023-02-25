import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5, 6]
y1 = [2, 4, 6, 18, 16, 22]
x2 = [4, 5, 7, 8]
y2 = [ 8, 9, 10, 15]
plt. plot(x1, y1, linestyle='dotted')
plt. plot(x2, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("allaham", fontsize=40, color='blue')
plt.show()

