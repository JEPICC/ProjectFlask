import sqlalchemy

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@189.156.123.95:3306/proyect_flask'

# Test if it works
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
print(engine.table_names())


string = '150000$tIsFVWBp$6785f376565a5780d421b6cf0891fe36eb8a655a520d22c84dfdb27616ac67c8'

cont = 0
for a in string:
    cont += 1

print(cont)