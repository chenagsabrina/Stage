import sys 

fichier = open(sys.argv[1], "r")# ouverture fichier fasta directement à partir du termial
ID = fichier.readline().lstrip('>').strip()
seq = fichier.read().replace('\n', '')
fichier.close()

out = open( 'fichier_fasta.fasta','w')#stokage du fichier de sortie en format fasta
out.write(seq[:11321]+seq[1388:])# postition que l'on souhaite récuperer


