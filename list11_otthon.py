Lista1 = ['Játék', 'Kalap', 5, 6, 'Garázs', 'Ruha']
Lista2 = Lista1.copy()

Lista1.reverse()
Lista2.reverse()

Lista1.append('Út')
Lista1.insert(2, 'Tűz')
Lista2.insert(5, 'Parázs')

Lista1.pop(0)
Lista2.pop(-1)
print(Lista1)
print(Lista2)