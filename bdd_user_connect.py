import sqlite3

#ref https://www.youtube.com/watch?v=jYUDi83tJXc&list=PLwsAoT89dh3pnuT7dGaG4vdxCpo5tJI8S

conn = sqlite3.connect('bdd/bdd_user.db')
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE user ("
    "name TEXT,"
    "cpf INTEGER,"
    "sex TEXT,"
    "client_class TEXT,"
    "tel INTEGER,"
    "birth INTEGER,"
    "mail TEXT,"
    "username TEXT,"
    "password TEXT,"
    "cep INTEGER, "
    "adress TEXT)"
    "")

conn.commit()
conn.close()