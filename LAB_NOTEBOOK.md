# CUADERNO DE LABORATORIO
## Observatorio de Transformaciones Numéricas

> *"El camino intelectual es tan valioso como el destino."*
> — Constitución del Observatorio, Artículo 7

---

## Cómo usar este cuaderno

Cada entrada sigue el formato:

```
### YYYY-MM-DD

**Hipótesis:** ...
**Experimento:** ...
**Resultado:** ...
**Consecuencia:** ...
```

Se registra tanto lo que funciona como lo que *no* funciona.
Las hipótesis falsas son tan valiosas como las verdaderas.

---

## Entradas

---

### 2026-07-15

**Hipótesis:** El campo temporal tiene una componente dinámica: las frecuencias de convergencia de Kaprekar varían a lo largo del año de forma no aleatoria.

**Experimento:** Se calculó la distribución de `convergence_steps` para cada fecha del calendario 2024 y se buscó correlación con la posición en el año.

**Resultado:** Falsa. La variación observada es consistente con el modelo nulo (distribución esperada por estructura del calendario). No hay componente dinámica significativa.

**Consecuencia:** Se elimina el componente dinámico del modelo del campo temporal. El campo es estático en primera aproximación.

---

### 2026-07-16

**Hipótesis:** La base decimal (base 10) es única en producir el fenómeno de Kaprekar. La convergencia es una propiedad exclusiva de la representación decimal.

**Experimento:** Se implementó `UniversalKaprekarTransformer` capaz de operar en base `b` arbitraria. Se ejecutó un sweep sobre bases 2–16.

**Resultado:** Falsa. Múltiples bases producen convergencia. La base 10 no es especial: es un caso particular de un fenómeno más general. Bases con mayor número de dígitos tienden a tener mayor `fixed_point_rate`.

**Consecuencia:** La base aritmética pasa a ser un parámetro explícito del Observatorio (Constitución, Artículo 6). Se abre la línea de investigación: ¿qué determina qué bases son "cristales" vs. "caóticas"?

---

### 2026-07-17

**Hipótesis:** (Abierta) Las bases que producen alta `fixed_point_rate` comparten propiedades algebraicas identificables (e.g., altamente compuestas, potencias de primos).

**Experimento:** Pendiente. Requiere cruzar datos del base sweep con propiedades numéricas de cada base.

**Resultado:** En curso.

**Consecuencia:** TBD.

---

*El Observatorio nació en Google Colab. El repositorio es su primera piedra permanente.*
*Fecha de fundación: 17 de julio de 2026, 1:00 AM (GMT-3, Buenos Aires).*
