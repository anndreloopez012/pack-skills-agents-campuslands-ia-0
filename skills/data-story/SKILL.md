---
name: data-story
description: "Convierte un análisis, un tablero o una tabla de resultados en una historia clara para quien no es técnico: mensaje principal, tres evidencias, qué significa y qué decisión se pide. Úsala cuando digas «explícale esto a la gerencia», «arma la presentación de los resultados» o «haz un post con este hallazgo»."
---

# Historia con datos

Toma tus números y los ordena en una historia corta: qué pasó, por qué importa y qué hay que
decidir, para una reunión, un correo o una publicación.

## Cuándo usarla

- «Tengo que presentar el tablero de ventas al gerente en 5 minutos».
- «Convierte estos hallazgos en un correo para la dirección».
- «Haz un carrusel o post de LinkedIn con este análisis».
- Después de `experiment-card`, `people-analytics` o `dashboard-designer`.

## Qué necesito de ti

- Los resultados: tabla, capturas del tablero o la ficha del experimento.
- Quién escucha (gerencia, equipo operativo, público en redes) y cuánto tiempo hay.
- Qué quieres que pase después (aprobar presupuesto, cambiar un proceso, que te contacten).
- Si los datos son confidenciales o de personas, usa `data-shield` antes y dime qué no se puede
  mostrar.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Escribo el mensaje principal en una frase con número y periodo: «Las devoluciones subieron
   de 2 % a 5 % en el tercer trimestre y se concentran en una sola línea».
2. Elijo máximo 3 evidencias que lo sostienen, cada una con su gráfico sugerido.
3. Explico qué significa en el idioma de quien escucha: quetzales, clientes, días, personas
   atendidas.
4. Digo lo que no sabemos (limitaciones) sin esconderlo.
5. Cierro con la decisión o acción concreta, con opciones si las hay, y lo que pasa si no se
   decide.
6. Adapto el formato: presentación (una idea por diapositiva), correo (mensaje arriba, detalle
   abajo) o publicación (gancho, dato, aprendizaje, sin datos confidenciales).
7. Reviso que cada número tenga unidad, periodo y fuente, y que el título de cada gráfico diga
   la conclusión.

## Lo que te entrego

```
Historia con datos · Para: ________ · Formato: presentación / correo / publicación · Tiempo: ___

Mensaje principal
- ...

Evidencias
| # | Dato (número, unidad, periodo) | Gráfico sugerido | Título del gráfico (conclusión) | Fuente |

Qué significa para ustedes
- ...

Lo que todavía no sabemos
- ...

Decisión que se pide
- Opción A: ... (efecto esperado)
- Opción B: ...

Guion
1. [Diapositiva o párrafo 1] ...
2. ...
```

## Reglas

- Una idea por diapositiva y un número protagonista por gráfico.
- No exagero: «subió» no es «se disparó», y correlación no es causa.
- Sin jerga técnica (DAX, p-valor, outlier) salvo que el público la use; si aparece, la explico
  en una línea.
- Datos de clientes, empleados o de la institución no se publican sin aprobación; en redes uso
  porcentajes o datos sintéticos.
- La persona decide qué se presenta y publica; yo preparo el borrador.
- Para convertir el guion en diapositivas usa `doc-to-presentation`; para resumir en una página,
  `one-pager`; para que suene natural, `human-voice`.

## Ejemplo

**Pedido:** «Resultados del tablero de cobros: días promedio de cobro subieron de 32 a 41 en seis
meses. Presento al gerente financiero el lunes».
**Entrega (resumen):** mensaje «Tardamos 9 días más en cobrar que en abril, y el 70 % del atraso
está en 12 clientes»; tres evidencias (línea de 6 meses, barras por cliente, tabla de antigüedad
de saldos); decisión propuesta: política de recordatorios y revisión de crédito para esos 12
clientes; guion de 5 diapositivas.
