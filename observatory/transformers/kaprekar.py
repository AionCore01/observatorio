"""
kaprekar.py - Universal Kaprekar Transformer

Implementa la transformación de Kaprekar para una base aritmética arbitraria.
Dados n dígitos en base b, la transformación consiste en:
  1. Ordenar los dígitos de mayor a menor para formar el número máximo.
  2. Ordenar los dígitos de menor a mayor para formar el número mínimo.
  3. Calcular la diferencia: kaprekar(n) = max - min.

En base 10 con 4 dígitos, el punto fijo es 6174 (constante de Kaprekar).
"""

from typing import Tuple


class UniversalKaprekarTransformer:
    """
    Transformer de Kaprekar que opera en base b arbitraria con n dígitos.

    Cumple con el Artículo 6 de la Constitución del Observatorio:
    la base aritmética es un parámetro, no un supuesto.
    """

    def __init__(self, n_digits: int = 4, base: int = 10):
        """
        Args:
            n_digits: Número de dígitos a usar.
            base: Base aritmética del sistema de representación.
        """
        if base < 2:
            raise ValueError(f"La base debe ser >= 2. Recibida: {base}")
        if n_digits < 2:
            raise ValueError(f"Número de dígitos debe ser >= 2. Recibido: {n_digits}")

        self.n_digits = n_digits
        self.base = base
        self.name = f"KaprekarTransformer(n={n_digits}, b={base})"

    def to_digits(self, n: int) -> list[int]:
        """Convierte un entero a lista de dígitos en la base dada, con padding."""
        digits = []
        if n == 0:
            digits = [0]
        else:
            temp = n
            while temp > 0:
                digits.append(temp % self.base)
                temp //= self.base

        # Pad to the requested width and normalize to the conventional order:
        # most significant digit first.
        while len(digits) < self.n_digits:
            digits.append(0)
        digits = digits[:self.n_digits]
        return list(reversed(digits))

    def from_digits(self, digits: list[int]) -> int:
        """Convierte una lista de dígitos en la base dada a un entero."""
        result = 0
        for i, d in enumerate(digits):
            result += d * (self.base ** (len(digits) - 1 - i))
        return result

    def transform(self, n: int) -> Tuple[int, int, int]:
        """
        Aplica un paso de la transformación de Kaprekar.

        Returns:
            (resultado, max_value, min_value)
        """
        digits = self.to_digits(n)
        sorted_desc = sorted(digits, reverse=True)
        sorted_asc = sorted(digits)

        max_val = self.from_digits(sorted_desc)
        min_val = self.from_digits(sorted_asc)
        return max_val - min_val, max_val, min_val

    def orbit(self, n: int, max_steps: int = 500) -> dict:
        """
        Calcula la órbita completa de n bajo la transformación de Kaprekar.

        Returns:
            dict con:
                - 'sequence': lista de valores en la órbita
                - 'steps': número de pasos hasta convergencia/ciclo
                - 'converged': True si encontró punto fijo
                - 'fixed_point': valor del punto fijo (si existe)
                - 'cycle': lista del ciclo (si no hay punto fijo)
        """
        sequence = [n]
        seen = {n: 0}

        current = n
        for step in range(1, max_steps + 1):
            next_val, _, _ = self.transform(current)
            sequence.append(next_val)

            if next_val == current:
                # Punto fijo
                return {
                    'sequence': sequence,
                    'steps': step,
                    'converged': True,
                    'fixed_point': next_val,
                    'cycle': None,
                }

            if next_val in seen:
                # Ciclo detectado
                cycle_start = seen[next_val]
                return {
                    'sequence': sequence,
                    'steps': step,
                    'converged': False,
                    'fixed_point': None,
                    'cycle': sequence[cycle_start:],
                }

            seen[next_val] = step
            current = next_val

        return {
            'sequence': sequence,
            'steps': max_steps,
            'converged': False,
            'fixed_point': None,
            'cycle': None,
        }

    def __repr__(self) -> str:
        return self.name
