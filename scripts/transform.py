import pandas as pd
from utils.helpers import load_csv, save_csv
from scripts.cleaning import drop_missing_values, standardize_column_names, filter_by_age

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transformation simple : mise en majuscules d'une colonne si elle existe.
    """
    if 'name' in df.columns:
        df['name'] = df['name'].str.upper()
    return df

if __name__ == "__main__":
    print("🔄 Chargement du fichier...")
    df = load_csv("data/input_sample.csv")

    print("🧹 Nettoyage des données...")
    df = standardize_column_names(df)
    df = drop_missing_values(df)
    df = filter_by_age(df, min_age=25)

    print("✨ Application des transformations...")
    df = transform_data(df)

    print("💾 Sauvegarde du fichier...")
    save_csv(df, "output/output.csv")

    print("✔ Pipeline terminé avec succès.")
