import sys 


fichier = open(sys.argv[1], "r") # ouverture du fichier directement sur un terminal
ID = fichier.readline().lstrip('>').strip()
seq = fichier.read().replace('\n', '')
fichier.close()

out = open('Nom du fichier_fasta.fasta','w') #stockage de fichier en format fasta
out.write(seq[5536:]+seq[:5536]) # mettre la position du gene COI
