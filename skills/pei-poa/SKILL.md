---
name: pei-poa
description: "Arma el PEI, el POM y el POA de una institución pública de Guatemala con Gestión por Resultados, alineados a las Prioridades Nacionales y a los lineamientos de SEGEPLAN. Úsala cuando digas «arma el POA del próximo año», «alinea nuestro PEI a las prioridades nacionales» o «baja el plan estratégico a metas anuales»."
---

# PEI y POA

Convierte el mandato y los problemas de tu institución en un Plan Estratégico Institucional (PEI),
un Plan Operativo Multianual (POM) y un Plan Operativo Anual (POA) con la lógica de Gestión por
Resultados (GpR), listos para revisar con planificación y financiero.

## Cuándo usarla

- «Tenemos que entregar el POA a SEGEPLAN y no sé por dónde empezar».
- «Alinea nuestros resultados a las Prioridades Nacionales de Desarrollo».
- «Baja el PEI de cinco años a metas del POM y del POA».
- «Revisa si nuestra cadena de resultados tiene sentido».

## Qué necesito de ti

- Mandato legal de la institución (ley o acuerdo de creación) y su misión y visión si ya existen.
- El problema central que atiende y la población a la que sirve (con cifras y su fuente).
- El PEI vigente, el POA anterior o su ejecución, si existen.
- Techo presupuestario aproximado en quetzales (Q) y los productos que ya entrega.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Leo el mandato y anoto qué le corresponde hacer a la institución y qué no (para no prometer
   resultados ajenos).
2. Hago el diagnóstico corto: problema central, causas, población afectada y datos de línea base.
   Si hace falta, armo el árbol de problemas con `logical-framework`.
3. Vinculo el problema con la Política General de Gobierno vigente, las Prioridades Nacionales de
   Desarrollo y sus Metas Estratégicas de Desarrollo (MED), el Plan K'atun 2032 y los ODS. Indico
   «verificar en segeplan.gob.gt» para cada vínculo.
4. Armo la cadena de resultados de la GpR: insumos (lo que se compra) → actividades → productos
   (bienes o servicios que se entregan) → resultado institucional (cambio en la población) →
   resultado estratégico o meta nacional.
5. Redacto cada resultado con la fórmula de SEGEPLAN: «Para el año X, se ha [incrementado o
   disminuido] [la condición] en [la población] de [línea base] a [meta]».
6. Para cada producto defino unidad de medida, meta física y quién lo recibe. Para cada resultado,
   un indicador con fórmula (detalle con `indicators`).
7. PEI (5 años o más): resultados y metas de largo plazo. POM (3 años): metas físicas por año.
   POA (1 año): productos, subproductos, metas por cuatrimestre y costo estimado por renglón con
   `budget-classifier`.
8. Reviso coherencia: cada producto contribuye a un resultado, cada insumo a un producto, y nada
   queda huérfano.

## Lo que te entrego

```
1. Vinculación estratégica
| Prioridad Nacional | MED | Política / eje | Resultado institucional |

2. Cadena de resultados
| Insumo | Actividad | Producto | Resultado institucional | Resultado estratégico |

3. Matriz PEI
| Resultado | Indicador | Línea base (año, fuente) | Meta final | Responsable |

4. Matriz POM (3 años)
| Producto | Unidad de medida | Meta año 1 | Meta año 2 | Meta año 3 | Costo estimado (Q) |

5. Matriz POA
| Producto | Subproducto | Unidad | C1 | C2 | C3 | Meta anual | Renglón | Monto (Q) | Responsable |

6. Supuestos y riesgos
7. Pendientes por verificar con planificación, financiero y SEGEPLAN
```

## Reglas

- Usa siempre la guía y los formatos vigentes de SEGEPLAN y del MINFIN para el año que se
  planifica: los nombres de matrices, plazos de entrega y sistemas (SIPLAN, SICOIN, SIGES) pueden
  cambiar. Marca «verificar en segeplan.gob.gt y minfin.gob.gt; revisado: noviembre de 2026».
- Nunca inventes una línea base: si no hay dato, escribe «Pendiente: línea base» y sugiere la
  fuente (INE, registros propios, encuestas).
- Un producto es lo que la institución entrega; un resultado es el cambio en la población. No los
  confundas («capacitaciones impartidas» es producto, no resultado).
- Las metas deben ser alcanzables con el techo presupuestario indicado; si no cuadran, avisa.
- Si el diagnóstico trae nombres, DPI o datos de beneficiarios, propone primero `data-shield`.
- Para cifras nacionales usa `source-researcher` y deja la fuente y la fecha de cada dato.
- La IA prepara; la autoridad de la institución aprueba y firma el plan.

## Ejemplo

**Pedido:** «Somos una dirección municipal de agua. Arma el POA 2027 con lo que te pego».
**Entrega (resumen):** vinculación con la prioridad nacional de acceso a agua potable y
saneamiento (por verificar); resultado «Para 2027 se ha incrementado la cobertura de agua
domiciliar en el casco urbano de 68 % a 75 %»; productos como «Hogares conectados a la red» con
meta de 900 conexiones repartidas por cuatrimestre; insumos en renglones 2 y 3; tres pendientes:
línea base del censo municipal, techo presupuestario y aprobación del concejo.
