"""
trace.py - Registro del viaje de una muestra a través del laboratorio.

El Trace es la unidad fundamental de trazabilidad del Observatorio.
Registra el historial completo de transformaciones aplicadas a una Sample.
"""

from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Sample:
    """Una muestra: la unidad mínima que el laboratorio puede procesar."""
    value: Any
    metadata: dict = field(default_factory=dict)


@dataclass
class Trace:
    """
    Registra el viaje completo de una Sample a través del laboratorio.

    El Trace es inmutable por convenio: cada transformación agrega un paso,
    nunca modifica los pasos anteriores.
    """
    sample: Sample
    history: List[dict] = field(default_factory=list)
    features: dict = field(default_factory=dict)

    def add_step(self, transformer_name: str, input_value: Any, output_value: Any,
                 metadata: Optional[dict] = None) -> None:
        """Agrega un paso al historial del Trace."""
        step = {
            "transformer": transformer_name,
            "input": input_value,
            "output": output_value,
            "metadata": metadata or {},
        }
        self.history.append(step)

    def add_feature(self, key: str, value: Any) -> None:
        """Agrega una feature extraída al Trace."""
        self.features[key] = value

    def final_value(self) -> Any:
        """Retorna el valor final del Trace (el último output en el historial)."""
        if self.history:
            return self.history[-1]["output"]
        return self.sample.value

    def __repr__(self) -> str:
        return f"Trace(steps={len(self.history)}, features={list(self.features.keys())})"
