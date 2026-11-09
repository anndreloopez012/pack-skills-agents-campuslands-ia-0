---
name: tax-returns-gt
description: "Calcula y revisa las declaraciones de IVA, ISR e ISO de Guatemala con su base, el detalle del cálculo y la lista de documentos que hay que tener de respaldo. Úsala cuando digas «calcula el IVA de octubre», «revisa el ISR trimestral» o «cuánto me toca pagar de ISO»."
---

# IVA, ISR e ISO

Prepara el cálculo de los impuestos del periodo con la base legal guatemalteca, muestra cada paso y
dice qué hay que documentar, para que el contador revise y presente en Declaraguate.

## Cuándo usarla

- «Calcula el IVA de octubre con estas ventas y compras.»
- «Revisa mi pago trimestral de ISR en el régimen sobre utilidades.»
- «¿Cuánto ISR pago en el régimen opcional simplificado este mes?»
- «Calcula el ISO del trimestre y cuánto puedo acreditar.»

## Qué necesito de ti

- NIT y régimen de la empresa: IVA general o pequeño contribuyente; ISR sobre utilidades u opcional
  simplificado; si es agente de retención.
- Libro de ventas y libro de compras del periodo (o el resumen de FEL emitidas y recibidas).
- Retenciones sufridas y efectuadas (constancias) y el remanente de crédito fiscal del mes anterior.
- Para ISR sobre utilidades e ISO: estado de resultados del periodo y balance o ingresos brutos que
  pida la base.
- Te propongo pasar los libros por `data-shield` si traen NIT y nombres de terceros.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Confirmo impuesto, periodo y régimen; si el régimen no está claro, me detengo y pregunto.
2. IVA general: débito fiscal (ventas gravadas × 12 %) menos crédito fiscal (compras con FEL válida ×
   12 %) menos retenciones de IVA sufridas menos remanente anterior = IVA a pagar o remanente.
3. ISR opcional simplificado: 5 % sobre los primeros Q30,000 de ingresos del mes y 7 % sobre el
   excedente, menos lo que ya te retuvieron.
4. ISR sobre utilidades: 25 % sobre la renta imponible (ingresos menos costos y gastos deducibles,
   más gastos no deducibles); para el pago trimestral, calculo con la base que corresponda y resto
   el ISO acreditado si aplica.
5. ISO: 1 % sobre la base que define la ley (en general, la mayor entre la cuarta parte del activo
   neto y la cuarta parte de los ingresos brutos); te muestro ambas bases y la que se usa.
6. Reviso consistencia: ventas del libro contra FEL emitidas, compras contra FEL recibidas, montos
   redondos sospechosos, facturas a nombre de otro NIT y gastos sin respaldo.
7. Armo la lista de documentos de respaldo y las dudas que debe resolver el contador.

## Lo que te entrego

```text
CÁLCULO DE [IVA | ISR | ISO]   Contribuyente: ________  NIT: ****  Periodo: ________
Régimen: ________   Supuestos: ________
```

| Línea | Concepto | Base (Q) | Tasa | Impuesto (Q) | Origen del dato |
|---|---|---:|---:|---:|---|
| 1 | Ventas gravadas (débito fiscal) | | 12 % | | Libro de ventas |
| 2 | Compras y servicios con FEL (crédito fiscal) | | 12 % | | Libro de compras |
| 3 | Retenciones de IVA sufridas | | | | Constancias |
| 4 | Remanente de crédito del periodo anterior | | | | Declaración anterior |
| 5 | **IVA a pagar o (remanente)** = 1 − 2 − 3 − 4 | | | | |

| Revisión | Resultado | Acción |
|---|---|---|
| Ventas del libro = FEL emitidas | Cuadra / Diferencia de Q____ | |
| Compras con FEL a nombre de la empresa | ____ documentos con observación | |
| Gastos no deducibles identificados | Q____ | |

```text
DOCUMENTOS DE RESPALDO: FEL emitidas y recibidas, constancias de retención, libros autorizados,
estado de cuenta, declaración anterior.
FECHA LÍMITE DE REFERENCIA: ________ (confírmala en portal.sat.gob.gt; si cae en día inhábil,
corre al siguiente día hábil).
PARA EL CONTADOR: dudas que debe resolver antes de presentar: 1. ____ 2. ____
```

## Reglas

- Cifras de referencia, revisado: noviembre de 2026; verifica que sigan vigentes en
  portal.sat.gob.gt antes de presentar: IVA 12 %; ISR sobre utilidades 25 %; régimen opcional
  simplificado 5 % hasta Q30,000 mensuales y 7 % sobre el excedente; ISO 1 %.
- Plazos de referencia (confírmalos en el calendario tributario de la SAT): IVA general mensual
  dentro del mes siguiente; ISR simplificado mensual dentro de los primeros 10 días hábiles del mes
  siguiente; pagos trimestrales de ISR e ISO al terminar cada trimestre; ISR anual hasta el 31 de
  marzo.
- No cito números de formulario ni artículos que no me confirmes: digo «formulario de IVA general
  mensual en Declaraguate» y te pido verificarlo en el portal.
- No invento ventas, compras ni retenciones; lo que falta queda como pendiente.
- Nunca pido ni uso la contraseña de Agencia Virtual; la persona presenta y paga.
- Si algo es una interpretación dudosa (por ejemplo, si un gasto es deducible), lo marco como
  «criterio a confirmar» y sugiero `source-researcher` o consultar a la SAT.

## Ejemplo

**Pedido:** «Régimen general. Ventas gravadas Q85,000 sin IVA, compras con FEL Q52,000 sin IVA,
remanente anterior Q1,100.»
**Entrega (resumen):** débito Q10,200.00, crédito Q6,240.00, remanente Q1,100.00, IVA a pagar
Q2,860.00; dos compras marcadas porque la FEL no trae el NIT de la empresa; lista de respaldo y fecha
límite a confirmar en el portal.
