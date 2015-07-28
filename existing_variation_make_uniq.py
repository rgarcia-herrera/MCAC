all_ids = set()
for linea in open('existing_variation_ids.txt').readlines():
    for ID in linea.strip().split(','):
        if ID.startswith('rs') or ID.startswith('COSM'):
            all_ids.add(ID)


