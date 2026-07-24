<<<<<<< HEAD
import MySQLdb


try:
    conn = MySQLdb.connect(
        host="193.203.175.250",
        user="u799109175_cestas_present",
        passwd="Ccap2004",
        db="u799109175_cestas_present",
        port=3306
    )
    cursor = conn.cursor()

    print("✅ Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("❌ Erro:", e)
=======
import MySQLdb



try:
    conn = MySQLdb.connect(
        host="193.203.175.250",
        user="u799109175_cestas_present",
        passwd="Ccap2004",
        db="u799109175_cestas_present",
        port=3306
    )
    cursor = conn.cursor()

    print("✅ Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("❌ Erro:", e)
>>>>>>> 0e55895f93f44ec8fd1c355af29c4c5ef6a3027e
