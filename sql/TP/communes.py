'''TP – BDD – Communes de France
Objectif : créer des fichiers csv à partir du fichier : « communes.csv » est encodé en « ansi » afin de
créer des tables reliées dans une base de données.
Note : Les régions dans ce TP correspondent au régions de France en 2015
Exercice 1 :
Créer une fonction python permettant de créer le fichier « lst_region.csv » (encodé en UTF8)
contenant les régions de France à partir du fichier « communes.csv ».
• On ne gardera que les 4 premières colonnes :
EU_circo ; code_région ; nom_région ;chef-lieu_région
• Chaque région ne doit figurer qu’une fois dans le fichier. On ne gardera que la première'''

import csv

def lst_region_ex_1():
    '''Créer le fichier « lst_region.csv » (encodé en UTF8) contenant les régions de France à partir du
    fichier « communes.csv ».'''
    with open('sql/TP/communes.csv', 'r') as f:
        region = {}
        commune_reader = csv.reader(f, delimiter=';')
        for row in commune_reader:
            region[row[1]]=';'.join(row[:4])
        with open('sql/TP/lst_region.csv', 'w', encoding='utf8') as f2:
            for code_region in region:
                f2.write(region[code_region] + '\n')
#lst_region_ex_1()


"""Exercice 2 :
Créer une fonction python permettant de créer le fichier « lst_departement.csv » (encodé en UTF8)
tableau contenant les départements de France à partir du fichier « communes.csv »
• On ne gardera que les colonnes B, E, F et G.
code_région ; numéro_département ;nom_département ; préfecture (la colonne B
permettra la liaison entre le département et la région)
• Chaque département ne doit figurer qu’une fois dans le fichier"""

def lst_departement():
    '''Créer le fichier « lst_departement.csv » (encodé en UTF8) contenant les départements de France
    à partir du fichier « communes.csv ».'''
    with open('sql/TP/communes.csv', 'r') as f:
        departement = {}
        commune_reader = csv.reader(f, delimiter=';') 
        for row in commune_reader:
            departement[row[4]]=';'.join([row[1]] + row[4:7])
        with open('sql/TP/lst_departement.csv', 'w', encoding='utf8') as f2:
            for code_departement in departement:
                f2.write(departement[code_departement] + '\n')

#lst_departement()

"""exercice 3 :
Créer une fonction python permettant de créer le fichier « lst_commune.csv » (encodé en UTF8)
tableau contenant les communes de France à partir du fichier « communes.csv »
On ne gardera que les colonnes E,H,I,J,K,L et M. La colonne E permettant de lier la commune au
département et la colonne H permettant d’indiquer à quelle circonscription appartient la commune"""

def lst_commune():
    '''Créer le fichier « lst_commune.csv » (encodé en UTF8) contenant les communes de France à partir
    du fichier « communes.csv ».'''
    with open('sql/TP/communes.csv', 'r') as f:
        commune = {}
        commune_reader = csv.reader(f, delimiter=';')
        for row in commune_reader:
            commune[row[12]]=';'.join([row[4]] +  row[7:13])
        with open('sql/TP/lst_commune.csv', 'w', encoding='utf8') as f2:
            for code_commune in commune:
                f2.write(commune[code_commune] + '\n')

lst_commune()

"""Exercice 4 : Créer une base de données « communes » et y créer les tables suivantes :
• Table « region »
• Table « departement »
• Table « commune »"""

import sqlite3

def create_db():
    '''Créer une base de données « communes » et y créer les tables suivantes :
    • Table « region »
    • Table « departement »
    • Table « commune »'''
    conn = sqlite3.connect('sql/TP/communes.db')
    c = conn.cursor()
    # c'est pas les bonnes données
    c.execute('''CREATE TABLE region
                 (EU_circo text,code_region text, nom_region text, chef_lieu_region text)''')
    c.execute('''CREATE TABLE departement
                 (code_region text,code_departement text, nom_departement text, prefecture text)''')
    c.execute('''CREATE TABLE commune
                 (code_commune text, nom_commune text, code_postal text, libelle_acheminement text,
                 ligne_5 text, latitude text, longitude text)''')
    conn.commit()
    conn.close()

def insert_db():
    '''Insérer les données des fichiers csv dans les tables de la base de données'''
    conn = sqlite3.connect('sql/TP/communes.db')
    c = conn.cursor()
    with open('sql/TP/lst_region.csv', 'r', encoding='utf8') as f:
        region_reader = csv.reader(f, delimiter=';')
        for row in region_reader:
            c.execute("INSERT INTO region VALUES (?, ?, ?, ?)", row)
    with open('sql/TP/lst_departement.csv', 'r', encoding='utf8') as f:
        departement_reader = csv.reader(f, delimiter=';')
        for row in departement_reader:
            c.execute("INSERT INTO departement VALUES (?, ?, ?,?)", row)
    with open('sql/TP/lst_commune.csv', 'r', encoding='utf8') as f:
        commune_reader = csv.reader(f, delimiter=';')
        for row in commune_reader:
            c.execute("INSERT INTO commune VALUES (?, ?, ?, ?, ?, ?, ?)", row)
    conn.commit()
    conn.close()

#create_db()
insert_db()