# Observatorio de Transformaciones Numéricas

> *"Colab fue el cuaderno donde nació el Observatorio. El repositorio es la primera piedra de su edificio."*

[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Un laboratorio computacional para el estudio de transformaciones numéricas, campos temporales y anomalías matemáticas.

**Primera piedra: la órbita de Kaprekar.**

---

## Qué es el Observatorio

El Observatorio nació de una pregunta: ¿qué pasa cuando aplicas la transformación de Kaprekar a todas las fechas de un calendario?

Lo que empezó como un experimento en un notebook de Colab se convirtió en un laboratorio con arquitectura propia, hipótesis falsificables, modelos nulos y una Constitución.

## Estructura

```
observatorio/
│
├── README.md          ← este archivo
├── CONSTITUCION.md    ← filosofía y reglas del laboratorio
├── LAB_NOTEBOOK.md    ← registro cronológico de hipótesis
├── LICENSE
├── pyproject.toml
│
├── observatory/       ← paquete Python
│   ├── core/          ← Trace, Sample, Laboratory
│   ├── transformers/  ← UniversalKaprekarTransformer
│   ├── analyzers/     ← módulos de interpretación
│   ├── fields/        ← campos de observación
│   ├── null_models/   ← modelos nulos (Art. 1 de la Constitución)
│   ├── experiments/   ← experimentos concretos
│   └── visualization/ ← visualización de datos
│
├── notebooks/         ← cuadernos de laboratorio (no el laboratorio)
│   ├── 001_kaprekar_calendar.ipynb
│   ├── 002_temporal_field.ipynb
│   └── 003_base_sweep.ipynb
│
├── tests/
└── papers/
```

## Uso rápido

```bash
# Clonar
git clone https://github.com/AionCore01/observatorio.git
cd observatorio

# Instalar
pip install -e ".[dev]"

# Ejemplo mínimo
python -c "
from observatory.transformers.kaprekar import UniversalKaprekarTransformer

k = UniversalKaprekarTransformer(n_digits=4, base=10)
result = k.orbit(1234)
print(f'Pasos hasta convergencia: {result[\"steps\"]}')
print(f'Punto fijo: {result[\"fixed_point\"]}')
"
```

## Principios (de la Constitución)

1. **Toda anomalía requiere un modelo nulo.**
2. **Toda hipótesis debe intentar refutarse antes de aceptarse.**
3. **Los observadores miden; los analizadores interpretan.**
4. **La base aritmética es un parámetro, no un supuesto.**
5. **El camino intelectual es tan valioso como el destino.**

→ Ver [`CONSTITUCION.md`](CONSTITUCION.md) para el texto completo.
→ Ver [`LAB_NOTEBOOK.md`](LAB_NOTEBOOK.md) para el registro de hipótesis.

## Descubrimientos hasta la fecha

| Hipótesis | Resultado | Consecuencia |
|-----------|-----------|-------------|
| El campo temporal es dinámico | **Falsa** | Se elimina la componente dinámica |
| La base 10 es única para Kaprekar | **Falsa** | La base es un parámetro universal |
| Bases con alta convergencia comparten propiedades algebraicas | **En curso** | — |

## Licencia

MIT — ver [LICENSE](LICENSE).

---

*Fundado el 17 de julio de 2026. Buenos Aires, Argentina.*
