"""Leitura dos dados públicos: módulo de apoio, não uma entrega de SQL do autor."""
from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "dados"


def _serie(code: int, column: str) -> pd.DataFrame:
    filename = f"sgs_{code}.json"
    source = (RAW / filename).read_bytes()
    info = json.loads((RAW / "manifest.json").read_text(encoding="utf-8"))["files"][filename]
    if hashlib.sha256(source).hexdigest() != info["sha256"]:
        raise ValueError(f"Snapshot alterado ou incompleto: {filename}")
    data = pd.DataFrame(json.loads(source))
    data["mes"] = pd.to_datetime(data["data"], format="%d/%m/%Y").dt.strftime("%Y-%m-01")
    data[column] = pd.to_numeric(data["valor"], errors="raise")
    if len(data) != 84 or data["mes"].duplicated().any() or data["mes"].iloc[0] != "2019-01-01" or data["mes"].iloc[-1] != "2025-12-01":
        raise ValueError(f"A série {code} não corresponde ao recorte de 84 meses")
    return data[["mes", column]]


def carregar_series() -> pd.DataFrame:
    saldo = _serie(20541, "saldo_milhoes")
    taxa = _serie(21084, "taxa_pct")
    aligned = saldo.merge(taxa, on="mes", validate="one_to_one", how="inner").sort_values("mes").reset_index(drop=True)
    if len(aligned) != 84:
        raise ValueError("As séries não têm os 84 meses alinhados")
    return aligned


def banco_sqlite(df: pd.DataFrame) -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    # REAL é necessário para divisão decimal em LAG/variação: INTEGER/INTEGER trunca no SQLite.
    saldo = df[["mes", "saldo_milhoes"]].copy()
    saldo["saldo_milhoes"] = saldo["saldo_milhoes"].astype(float)
    saldo.to_sql("saldo", db, index=False)
    df[["mes", "taxa_pct"]].to_sql("inadimplencia", db, index=False)
    return db
