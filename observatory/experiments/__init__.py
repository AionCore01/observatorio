"""experiments/ - Experimentos del Observatorio.

Cada experimento es una hipótesis operacionalizada.
Ver LAB_NOTEBOOK.md para el registro de resultados.
"""

from .kaprekar_experiments import base_sweep, summarize_base_sweep

__all__ = ["base_sweep", "summarize_base_sweep"]
