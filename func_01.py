from collections import Counter

group_number = []

def summ(n_customers, n_first_id):
	for n in range(n_first_id, n_first_id+n_customers):
		group_number.append(sum(map(int,str(n))))
	d = dict(Counter(group_number))
	return d