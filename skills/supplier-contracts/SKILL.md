---
name: supplier-contracts
description: "Lleva el control de contratos de mantenimiento y proveedores: vigencia, periodicidad de visitas, técnico asignado, piezas cambiadas y evaluación del servicio. Pídela así: «arma el control de mis contratos», «evalúa al proveedor de ascensores»."
---

# Contratos y proveedores

Ordena en una sola tabla qué proveedor atiende cada sistema, cada cuánto debe venir, quién vino, qué
cambió y cómo cumplió. Para administradores de edificios y gerentes administrativos.

## Cuándo usarla

- «Tengo 12 contratos de mantenimiento en PDF, hazme el cuadro de control».
- «El proveedor de aire no ha venido este mes, cómo lo documento».
- «Evalúa al proveedor de ascensores antes de renovar».

## Qué necesito de ti

- Los contratos o sus datos: proveedor, objeto, sistema, fecha de inicio y fin, monto en Q, forma
  de pago, periodicidad de visitas, tiempo de respuesta a emergencias, qué incluye (mano de obra,
  piezas, consumibles).
- Las boletas o reportes de visita que tengas.
- Si los contratos traen nombres, DPI, NIT o cuentas bancarias, propone primero usar `data-shield`.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Extraigo de cada contrato los campos de la plantilla. Lo que no esté escrito lo marco «No indica».
2. Calculo las visitas que debieron ocurrir en el periodo según la periodicidad (mensual, bimestral,
   trimestral, semestral, anual) y las comparo con las boletas recibidas.
3. Registro cada visita: fecha, técnico, trabajo hecho, piezas cambiadas (con número de serie si
   aplica) y si la pieza estaba incluida o se cobró aparte.
4. Señalo alertas: visitas faltantes, piezas cobradas que el contrato incluía, garantías de piezas
   por vencer, contratos con menos de 60 días de vigencia.
5. Evalúo el servicio con la matriz de abajo y propongo renovar, renegociar o cotizar.

## Lo que te entrego

```
CONTROL DE CONTRATOS - <Edificio> - Corte: __/__/____
| N.º | Sistema | Proveedor | Objeto | Inicio | Fin | Días por vencer | Monto mensual Q | Periodicidad | Respuesta a emergencias | Incluye piezas (Sí/No/Parcial) | Responsable interno |

BITÁCORA DE VISITAS
| Fecha | Proveedor | Sistema | Técnico | Tipo (Preventivo/Correctivo/Emergencia) | Trabajo realizado | Piezas cambiadas | Serie | ¿Incluida? | Costo extra Q | Boleta N.º | Firma de conformidad |

CUMPLIMIENTO DEL PERIODO
| Proveedor | Visitas pactadas | Visitas realizadas | % cumplimiento | Emergencias | Tiempo medio de respuesta (h) |

EVALUACIÓN DEL SERVICIO (1 a 5)
| Proveedor | Puntualidad | Calidad del trabajo | Tiempo de respuesta | Documentación (boletas, informes) | Seguridad del técnico | Precio vs mercado | Promedio | Recomendación |

ALERTAS
- <contrato o visita> - <qué pasa> - <qué hacer y antes de cuándo>
```

## Reglas

- No interpreto cláusulas legales como abogado: si hay penalidades, garantías o rescisión en duda,
  lo marco para revisión del asesor legal.
- Promedio menor a 3 o cumplimiento menor a 80 % = proponer reunión con el proveedor y plan de mejora.
- Toda pieza cambiada debe tener boleta con firma de quien recibió; si no hay, lo anoto como hallazgo.
- Los avisos al proveedor los redacto con `pro-writer`, pero nada se envía sin tu aprobación.
- Las fechas de vencimiento alimentan al agente `contract-deadlines`.
- Montos en quetzales (Q). Sin emojis.

## Ejemplo

**Pedido:** «Aquí están los datos de mis contratos de ascensores, aire y planta eléctrica».
**Entrega (resumen):** cuadro de 3 contratos; el de aire vence en 45 días (alerta); ascensores con
11 de 12 visitas (92 %); planta eléctrica cobró un filtro que el contrato incluía (hallazgo con monto
Q y borrador de reclamo para aprobar).
