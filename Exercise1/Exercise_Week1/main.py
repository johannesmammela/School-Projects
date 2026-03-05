from my_random_number_generator import My_Random
import matplotlib.pyplot as plt


my_rand = My_Random()
my_rand.set_seed(8975)

num_list = []
for i in range(0,100000):
    num = my_rand.dice()
    num_list.append(num)


luvut = [1,2,3,4,5,6]
counts = []
for numero in luvut:
    counter = 0
    for k in num_list:
        if numero == k:
            counter+=1
    counts.append(counter)
print(counts)


fig, ax = plt.subplots()

ax.bar(luvut, counts, width=1, edgecolor="white", linewidth=0.7)
plt.show()