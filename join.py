"""
Script permettant de mettre bout à bout des fichiers source java

Utilisation :
"join.py [ {fichiers} destination ]"

	fichiers : liste de fichiers, si non vide alors utilisée

	destination : fichier de destination (avec extension java)

exemples :
	"join.py"
	"join.py fichier1.java fichier2.java res.java"

Installation :
	A placer dans le dossier contenant le dossier <srcFolder>

-------------
Date de création : 13/11/2014
Auteur : Yann ROLLAND / TidyMaze

"""

import sys
import os

print(os.getcwd())

prefixImport = 'import '
prefixPackage = 'package '
srcFolder = 'src'
dstName = 'packed.java'
suffixSrc = '.java'

tabPaths = []

if len(sys.argv) == 1:
	pathDest = dstName
	for fileName in os.listdir(srcFolder):
		if fileName.endswith(suffixSrc):
			tabPaths.append(os.path.join(srcFolder,fileName))
elif len(sys.argv) >= 3:
	tabPaths = sys.argv[1:-1]
	pathDest = sys.argv[len(sys.argv)-1]


print("fichiers : ", str(tabPaths))

fDest = open(pathDest, 'w+')

print('dest :', fDest.name)

tabImport = []
tabCode = []

# met le contenu des fichiers dans le tableau 
for path in tabPaths:
	print('examen de ', path)
	f = open(path,'r')

	# pour chaque ligne : enregitrer ou passer
	for ligne in f:
		if ligne.startswith(prefixImport):
			if ligne not in tabImport:
				tabImport.append(ligne)
			"""
			else:
				print("ligne d'import '", ligne, "' déjà présente")
			"""
		elif ligne.startswith(prefixPackage):
			continue
		else:
			tabCode.append(ligne)

	f.close()

# recopie des imports
for ligne in tabImport:
	fDest.write(ligne)

# recopie des lignes de code
for ligne in tabCode:
	fDest.write(ligne)

# fini
fDest.close()

input("Fin !")
