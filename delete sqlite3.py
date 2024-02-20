import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Remplacez 'NomDeLaTable' par le nom de la table que vous voulez supprimer

tables_names = ['polls_ods_player',
                'polls_ods_club',
                'polls_f_club',
                'polls_f_licence',
                'polls_d_agegrp',
                'polls_d_date',
                'polls_d_federation',
                'polls_d_sex',
                'polls_d_type',
                'polls_d_departement']

# Exécute la commande SQL pour supprimer la table

cursor.execute(f"DROP TABLE IF EXISTS polls_ods_clubs;")

# Validez la transaction
conn.commit()

# Ferme la connexion
conn.close()
