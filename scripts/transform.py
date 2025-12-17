import argparse
import logging
from pathlib import Path

import pandas as pd


# ----------------------------
# Logging
# ----------------------------
def setup_logger(verbose: bool) -> logging.Logger:
    logger = logging.getLogger("automation_data_python")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    # évite doublons si relancé
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


# ----------------------------
# Core pipeline
# ----------------------------
def load_csv(input_path: Path, logger: logging.Logger) -> pd.DataFrame:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df


def clean_data(df: pd.DataFrame, logger: logging.Logger) -> pd.DataFrame:
    logger.info("Cleaning data...")

    df = df.copy()

    # Exemples simples : adapte à ton CSV
    if "useless_col" in df.columns:
        logger.info("Dropping column: useless_col")
        df = df.drop(columns=["useless_col"])

    if "date" in df.columns:
        logger.info("Converting 'date' to datetime")
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "amount" in df.columns:
        before = len(df)
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        df = df.dropna(subset=["amount"])
        logger.info(f"Dropped {before - len(df)} rows with invalid amount")

    logger.info(f"After cleaning: {len(df)} rows")
    return df


def transform_data(df: pd.DataFrame, logger: logging.Logger) -> pd.DataFrame:
    logger.info("Transforming data...")

    # Exemple simple : adapte selon tes colonnes
    required = {"client", "category", "amount"}
    if required.issubset(df.columns):
        result = (
            df.groupby(["client", "category"], as_index=False)["amount"]
            .sum()
            .rename(columns={"amount": "total_amount"})
        )
        logger.info(f"Created aggregated report: {len(result)} rows")
        return result

    logger.warning("Missing columns for aggregation. Returning cleaned data only.")
    return df


def save_outputs(clean_df: pd.DataFrame, report_df: pd.DataFrame, outdir: Path, logger: logging.Logger) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    cleaned_path = outdir / "cleaned.csv"
    report_path = outdir / "report.csv"

    logger.info(f"Saving cleaned dataset to: {cleaned_path}")
    clean_df.to_csv(cleaned_path, index=False)

    logger.info(f"Saving report to: {report_path}")
    report_df.to_csv(report_path, index=False)

    logger.info("Outputs saved successfully.")


# ----------------------------
# CLI
# ----------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automation pipeline: load -> clean -> transform -> export"
    )
    parser.add_argument(
        "--input",
        type=str,
        default="data/input_sample.csv",
        help="Path to input CSV file (default: data/input_sample.csv)"
    )
    parser.add_argument(
        "--outdir",
        type=str,
        default="output",
        help="Output directory (default: output)"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logs"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = setup_logger(args.verbose)

    input_path = Path(args.input)
    outdir = Path(args.outdir)

    try:
        df_raw = load_csv(input_path, logger)
        df_clean = clean_data(df_raw, logger)
        df_report = transform_data(df_clean, logger)
        save_outputs(df_clean, df_report, outdir, logger)

        logger.info("Pipeline finished ✅")
        return 0

    except Exception as e:
        logger.error(f"Pipeline failed ❌: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
