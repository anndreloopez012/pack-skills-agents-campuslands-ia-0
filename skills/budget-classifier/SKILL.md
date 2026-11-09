---
name: budget-classifier
description: "Ubica cada insumo o gasto en su grupo, subgrupo y renglón del Manual de Clasificaciones Presupuestarias del MINFIN y te dice cuándo conviene confirmar. Úsala cuando digas «en qué renglón va esto», «clasifica esta lista de compras» o «arma el presupuesto del POA por renglón»."
---

# Renglones presupuestarios

Clasifica tus insumos, servicios y contrataciones según el clasificador por objeto del gasto del
Manual de Clasificaciones Presupuestarias para el Sector Público de Guatemala (MINFIN), para el POA,
una solicitud de compra o una modificación presupuestaria.

## Cuándo usarla

- «¿En qué renglón va la compra de tóner? ¿Y el mantenimiento del aire acondicionado?».
- «Clasifica esta lista de 40 insumos del POA».
- «¿Esto es 029 o 081?».

## Qué necesito de ti

- La lista de insumos o gastos con descripción, cantidad y costo estimado en quetzales (Q).
- Para qué se usa cada uno (consumo, mantenimiento, inversión, servicio de una persona).
- Tu tipo de institución (gobierno central, descentralizada, municipalidad), porque algunos
  renglones se usan distinto.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Separo cada insumo por naturaleza: personas, servicios, bienes de consumo, bienes duraderos,
   transferencias.
2. Lo ubico primero en el grupo de gasto:
   - 0 Servicios personales (sueldos, salarios y otras remuneraciones del personal).
   - 1 Servicios no personales (energía, agua, teléfono, arrendamientos, mantenimiento y
     reparación, viáticos, capacitación, estudios y servicios técnicos).
   - 2 Materiales y suministros (alimentos, papel, combustible, útiles, repuestos).
   - 3 Propiedad, planta, equipo e intangibles (mobiliario, equipo de cómputo, vehículos,
     construcciones, software).
   - 4 Transferencias corrientes; 5 Transferencias de capital; 6 Activos financieros;
     7 Servicio de la deuda pública; 8 Otros gastos; 9 Asignaciones globales.
3. Bajo al subgrupo y al renglón de tres dígitos que mejor describa el bien o servicio, usando la
   descripción del Manual, no solo el nombre parecido.
4. Aplico las pruebas de frontera: ¿se consume en el año o dura más? (grupo 2 contra grupo 3);
   ¿es un servicio de una persona o de una empresa?; ¿es reparación (grupo 1) o un repuesto que
   compras tú (grupo 2)?
5. Marco la confianza de cada clasificación: alta, media o «confirmar con financiero».
6. Sumo por renglón y por grupo para el POA.

Renglones frecuentes como referencia (orientativa; confirmar nombre y código en el Manual vigente):

| Grupo | Renglones que más se usan en oficinas públicas |
|---|---|
| 0 | 011 Personal permanente · 022 Personal por contrato · 029 Otras remuneraciones de personal temporal |
| 1 | 111 Energía eléctrica · 112 Agua · 113 Telefonía · 133 Viáticos en el interior · 151 Arrendamiento de edificios y locales · 171 Mantenimiento y reparación de edificios · 185 Servicios de capacitación |
| 2 | 211 Alimentos para personas · 241 Papel de escritorio · 262 Combustibles y lubricantes · 291 Útiles de oficina |
| 3 | 322 Mobiliario y equipo de oficina · 328 Equipo de cómputo |

## Lo que te entrego

```
| # | Insumo | Uso | Grupo | Subgrupo | Renglón (código y nombre) | Cantidad | Costo (Q) | Confianza | Nota |

Resumen por renglón
| Renglón | Nombre | Total (Q) | % del total |

Resumen por grupo de gasto
| Grupo | Nombre | Total (Q) |

Por confirmar con la unidad financiera
- ...
```

## Reglas

- El catálogo de renglones y sus descripciones se actualizan por acuerdo ministerial: consulta
  siempre la edición vigente del Manual en minfin.gob.gt. Los ejemplos de renglones que doy son
  orientativos; revisado: noviembre de 2026.
- No invento renglones. Si un insumo no encaja claramente, lo digo y doy las dos opciones más
  probables con la razón de cada una.
- Los renglones de personal (grupo 0) y los servicios técnicos o profesionales individuales tienen
  reglas laborales y de contratación propias; siempre van con «confirmar con recursos humanos y
  financiero».
- Un bien de grupo 3 genera inventario; recuérdalo para el registro de activos.
- Si la lista trae salarios o nombres de personas, propone primero `data-shield`.
- Para armar la hoja con totales y tablas dinámicas, apóyate en `spreadsheet-helper`.

## Ejemplo

**Pedido:** «Clasifica: resmas de papel, mantenimiento de 6 aires acondicionados, 3 computadoras,
gasolina para el pick-up y un taller para el personal».
**Entrega (resumen):** papel en grupo 2 (productos de papel), mantenimiento en grupo 1
(mantenimiento y reparación de maquinaria y equipo), computadoras en grupo 3 (equipo de cómputo),
gasolina en grupo 2 (combustibles y lubricantes), taller en grupo 1 (servicios de capacitación).
Cada uno con su código de tres dígitos sugerido, confianza y nota de verificar en el Manual
vigente.
