import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Realiza um LEFT JOIN com base na coluna "personId"
    df = pd.merge(person, address, on="personId", how="left")
    
    # Seleciona as colunas no formato desejado
    return df[["firstName", "lastName", "city", "state"]]