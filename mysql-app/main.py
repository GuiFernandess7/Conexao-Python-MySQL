import pandas as pd

class Connection:

    def __init__(self, db_name):

        self.password = password
        self.conn =  f"mysql+pymysql://root:{self.password}@localhost:3306/{db_name}"
        self.db_connection = create_engine(self.conn)
    
    def get_query(self, query):
        
        try:
            self.df = pd.read_sql(query, con=self.db_connection)
            return self.df
            
        except Exception as ex:
            return f"Erro ao acessar o dataframe: {ex}"

    def get_dict(self, type, df: pd.DataFrame):

        try:
            self.dict = df.to_dict(type)
            return self.dict
        
        except Exception as ex:
            return f"Erro ao criar dicionário: {ex}"

    
def main():
    database_name = 'world'
    world_db = Connection(database_name)
    # Dentro do banco de dados 'world' a função get_query permite acessar a tabela pelo comando SQL
    countries = world_db.get_query('SELECT * FROM country;')
    # Converte a tabela em um dicionário
    country_dict = world_db.get_dict('index', countries)
    
    print(countries)


if __name__=='__main__':
    from sqlalchemy import create_engine
    from config import password
    main()