"""Reexecuta as consultas e análises do autor sem a aplicação de ensino."""
from __future__ import annotations

import json
import sys
from contextlib import closing
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go

from apoio.dados import ROOT, banco_sqlite, carregar_series


def executar() -> None:
    df = carregar_series()
    output = ROOT / "resultados" / "reexecucao"
    output.mkdir(parents=True, exist_ok=True)
    count = 0
    with closing(banco_sqlite(df)) as db:
        for source in sorted((ROOT / "consultas").glob("*.sql")):
            result = pd.read_sql_query(source.read_text(encoding="utf-8"), db)
            result.to_csv(output / f"{source.stem}.csv", index=False)
            print(f"SQL {source.name}: {len(result)} linha(s)")
            count += 1
    for source in sorted((ROOT / "analises").glob("*.py")):
        namespace = {"df": df.copy(), "pd": pd, "go": go}
        exec(compile(source.read_text(encoding="utf-8"), str(source), "exec"), namespace)
        if "resultado" not in namespace:
            raise ValueError(f"{source.name} deve definir resultado")
        result = namespace["resultado"]
        if isinstance(result, go.Figure):
            result.write_html(output / f"{source.stem}.html", include_plotlyjs=True)
        elif isinstance(result, pd.DataFrame):
            result.to_csv(output / f"{source.stem}.csv", index=False)
        elif isinstance(result, pd.Series):
            result.to_csv(output / f"{source.stem}.csv", index=False)
        else:
            (output / f"{source.stem}.json").write_text(json.dumps(result, ensure_ascii=False, default=str), encoding="utf-8")
        print(f"Python {source.name}: OK")
        count += 1
    print(f"{count} análises reproduzidas em resultados/reexecucao/")


if __name__ == "__main__":
    try:
        executar()
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Falha na reprodução: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
