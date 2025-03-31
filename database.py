import mysql.connector

# Senha do banco de dados
#senhabd = "123456789"
senhabd = "univasf"

# Função para criar o banco de dados
def CreateDataBase():

    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senhabd
    )

    cursor = db.cursor()

    # Criando o banco de dados
    cursor.execute("DROP DATABASE IF EXISTS cidirsy")
    cursor.execute("CREATE DATABASE IF NOT EXISTS cidirsy;")

# Função para criar as tabelas do banco de dados
def CreateTables():

    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senhabd,
        database="cidirsy"
    )

    cursor = db.cursor()

    # Criando a tabela doencas
    cursor.execute("CREATE TABLE IF NOT EXISTS doencas(id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, dnome VARCHAR(100) NOT NULL );")

    # Criando a tabela sintomas
    cursor.execute("CREATE TABLE IF NOT EXISTS sintomas(id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, snome VARCHAR(100) NOT NULL);")

    # Criando a tabela doencas_sintomas
    cursor.execute("CREATE TABLE IF NOT EXISTS doencas_sintomas (id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, did BIGINT UNSIGNED NOT NULL, sid BIGINT UNSIGNED NOT NULL, FOREIGN KEY(did) REFERENCES doencas(id), FOREIGN KEy(sid) REFERENCES sintomas(id));")

    # Criando a view pesquisa
    cursor.execute("CREATE VIEW pesquisa AS SELECT dnome, snome FROM doencas_sintomas LEFT JOIN doencas ON  doencas_sintomas.did = doencas.id LEFT JOIN sintomas ON doencas_sintomas.sid = sintomas.id;")

# Função para popular as tabelas
def InsertData():

    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senhabd,
        database="cidirsy"
    )

    cursor = db.cursor()

    # Populando a tabela doencas
    cursor.execute("""INSERT INTO doencas(dnome) VALUES 
                    ('Ortézia'),
                    ('Minador das folhas'),
                    ('Escama farinha'),
                    ('Coleobroca'),
                    ('Mosca branca'),
                    ('Pulgão preto'),
                    ('Ácaro da ferrugem'),
                    ('Ácaro branco');
                """)
    
    db.commit()

    # Populando a tabela sintomas
    cursor.execute("""INSERT INTO sintomas(snome) VALUES
                    ('Folhas pretas'),
                    ('Queda dos frutos'),
                    ('Queda das folhas'),
                    ('Emrolamento das folhas'),
                    ('Caminhos em ziguezague na folha'),
                    ('Casca do tronco rachado'),
                    ('Tronco com manchas esbranquiçadas'),
                    ('Morte de galhos'),
                    ('Furos no tronco'),
                    ('Murchamento dos ramos'),
                    ('Secamento dos ramos'),
                    ('Folhas deformadas'),
                    ('Folhas amareladas exceto nas nervuras'),
                    ('Queda dos botões florais'),
                    ('Encarquilhamento das folhas'),
                    ('Manchas escuras no fruto'),
                    ('Manchas escuras nas folhas'),
                    ('Folhas com aspecto corticoso'),
                    ('Frutos com a coloração cinza prateada'),
                    ('Margens das folhas dobradas para baixo');
                """)

    db.commit()

    # Populando a tabela doencas_sintomas
    cursor.execute("""INSERT INTO doencas_sintomas(did, sid) VALUES
                    ('1', '1'),
                    ('1', '2'),
                    ('1', '3'),
                    ('2', '4'),
                    ('2', '3'),
                    ('2', '5'),
                    ('3', '6'),
                    ('3', '7'),
                    ('3', '8'),
                    ('4', '9'),
                    ('4', '10'),
                    ('4', '11'),
                    ('5', '1'),
                    ('5', '12'),
                    ('5', '13'),
                    ('6', '3'),
                    ('6', '14'),
                    ('6', '15'),
                    ('7', '16'),
                    ('7', '3'),
                    ('7', '17'),
                    ('8', '18'),
                    ('8', '19'),
                    ('8', '20');
                """)

    db.commit()

# Função para retornar os sintomas
def ShowSintomas():

    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senhabd,
        database="cidirsy"
    )

    cursor = db.cursor()

    # Pegando os sintomas
    cursor.execute("SELECT * FROM sintomas")
    result = cursor.fetchall()

    return result
    
# Função para retornar as doenças
def ShowDoencas(escolhas = []):

    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senhabd,
        database="cidirsy"
    )

    cursor = db.cursor()
    # Gerador dos placeholders
    placeholders = ', '.join(['%s'] * len(escolhas))

    query = f"SELECT dnome, COUNT(dnome) AS sn FROM pesquisa WHERE snome IN ({placeholders}) GROUP BY (dnome) ORDER BY (sn) DESC LIMIT 3;"

    # Pegando as doenças que mais tem os sintomas que o usuário escolheu
    cursor.execute(query, escolhas)
    result = cursor.fetchall()

    return result