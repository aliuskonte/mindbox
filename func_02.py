from collections import Counter

group_number = []

def summ(n_customers):
	for n in range(0, n_customers):
		group_number.append(sum(map(int,str(n))))
	c = dict(Counter(group_number))
	return c

n_customers = int(input('Введите  количество клиентов: '))
print(summ(n_customers))