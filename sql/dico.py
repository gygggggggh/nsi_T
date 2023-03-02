from csv import DictReader, DictWriter

def read_dico(filename):
    with open(filename) as f:
        reader = DictReader(f, delimiter=';')
        return [row for row in reader]

titanic = read_dico('sql/titanic.csv')

#print(titanic[1])

def get_passengers_by_class(titanic, classe):
    return [p for p in titanic if p['classe'] == classe]

#print(get_passengers_by_class(titanic,'1'))

def get_passengers_by_age(titanic, age):
    return [p for p in titanic if p['age'] == age]

#print(get_passengers_by_age(titanic, 'adult'))

def get_passengers_by_survived(titanic, survie):
    return [p for p in titanic if p['survie'] == survie]

#print(get_passengers_by_survived(titanic,'1'))

def get_kids(titanic): # age < 18 : 
    return [p for p in titanic if p['age'] < '18']

print(get_kids(titanic))


def write_dico(filename, data):
     with open(filename, 'w') as f:
         writer = DictWriter(f, delimiter=';', fieldnames=data[0].keys())
         writer.writeheader()
         writer.writerows(data)

def sort_by_age(titanic):
    return sorted(titanic, key=lambda p: p['age'])

write_dico('sql/titanic_sorted.csv', sort_by_age(get_passengers_by_class(titanic, '1')))
