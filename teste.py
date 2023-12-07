import MySQLdb
db = MySQLdb.connect(
    host="aws.connect.psdb.cloud",
    user="brif3h2xssy0y808ptp4",
    passwd="pscale_pw_uzIYNxeewsAm7zDQiay8V5noWRThn0uveLKa1nWdX2K",
    db="luisao",
    autocommit=True,
    ssl_mode="VERIFY_IDENTITY",
    ssl={"ca": r"C:\Users\luisg\Downloads\myself\cacert.pem"}
)

# Crie um cursor
cursor = db.cursor()

# Execute a consulta SQL
cursor.execute("SELECT * FROM usuario")

# Busque todos os registros
usuarios = cursor.fetchall()

# Feche o cursor
cursor.close()

# Imprima os usuários
for usuario in usuarios:
    print(usuario)
