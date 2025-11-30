import pandas as pd

def drop_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les lignes contenant des valeurs manquantes.
    """
    return df.dropna()

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Met les noms de colonnes en minuscules et remplace les espaces par des underscores.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def filter_by_age(df: pd.DataFrame, min_age: int = 0) -> pd.DataFrame:
    """
    Filtre les lignes pour ne garder que les personnes dont l'âge est supérieur à min_age.
    """
    if "age" in df.columns:
        return df[df["age"] >= min_age]
    return df
