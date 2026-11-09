---
name: financial-ratios
description: "Calcula razones de liquidez, endeudamiento, actividad y rentabilidad a partir de los estados financieros y explica en palabras qué dice cada una. Úsala cuando digas «sácame los ratios», «cómo está la empresa» o «explícale al gerente si podemos pedir el préstamo»."
---

# Ratios con interpretación

Calcula las razones financieras clave y las traduce a lenguaje de negocio: qué significa el número,
si es bueno o preocupante para ese giro y qué hacer.

## Cuándo usarla

- «Sácame los ratios del balance de diciembre.»
- «¿La empresa tiene liquidez para pagar lo que debe este año?»
- «Prepara el análisis para presentar al banco o a la junta.»

## Qué necesito de ti

- Balance general y estado de resultados (ideal: dos periodos para comparar). Si solo tienes la
  balanza, primero usa `financial-statements`.
- Giro del negocio (comercio, servicios, manufactura, agro) para leer los números en contexto.
- Para qué es el análisis: gerencia, banco, inversionista o auditoría.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Tomo las cifras de los estados y te muestro de dónde sale cada una.
2. Calculo las razones con su fórmula visible y dos decimales.
3. Comparo contra el periodo anterior y digo si mejoró, empeoró o se mantuvo.
4. Interpreto cada razón en una o dos frases llanas: «por cada quetzal que debes a corto plazo
   tienes Q1.45 para pagarlo».
5. Señalo alertas (por ejemplo, liquidez menor a 1, días de cobro que crecen, margen que cae) y las
   relaciono entre sí: una baja de liquidez puede venir de clientes que pagan más lento.
6. Cierro con 3 conclusiones y 3 acciones sugeridas para la gerencia.

## Lo que te entrego

| Grupo | Razón | Fórmula | Periodo actual | Periodo anterior | Tendencia | Qué significa |
|---|---|---|---:|---:|---|---|
| Liquidez | Razón corriente | Activo corriente / Pasivo corriente | | | | |
| Liquidez | Prueba ácida | (Activo corriente − Inventarios) / Pasivo corriente | | | | |
| Liquidez | Capital de trabajo (Q) | Activo corriente − Pasivo corriente | | | | |
| Endeudamiento | Endeudamiento total | Pasivo total / Activo total | | | | |
| Endeudamiento | Pasivo a patrimonio | Pasivo total / Patrimonio | | | | |
| Endeudamiento | Cobertura de intereses | Utilidad en operación / Gastos financieros | | | | |
| Actividad | Días de cobro | Cuentas por cobrar / Ventas al crédito × 365 | | | | |
| Actividad | Días de inventario | Inventario / Costo de ventas × 365 | | | | |
| Actividad | Días de pago | Proveedores / Compras al crédito × 365 | | | | |
| Rentabilidad | Margen bruto | Utilidad bruta / Ventas | | | | |
| Rentabilidad | Margen neto | Utilidad neta / Ventas | | | | |
| Rentabilidad | ROA | Utilidad neta / Activo total | | | | |
| Rentabilidad | ROE | Utilidad neta / Patrimonio | | | | |

```text
LECTURA PARA LA GERENCIA
Cómo está la empresa en una frase: ________
Alertas: 1. ____  2. ____  3. ____
Acciones sugeridas: 1. ____  2. ____  3. ____
Límites del análisis: cifras sin auditar | un solo periodo | promedios vs. saldos de cierre
```

## Reglas

- Muestro siempre la fórmula y las cifras usadas; nada de números sin origen.
- No hay un valor «correcto» universal: comparo contra el periodo anterior, el giro y, si me das
  datos del sector con fuente, contra el sector. No invento promedios de industria.
- Si los estados no cuadran o no están cerrados, lo digo antes de calcular.
- Uso saldos de cierre salvo que me des saldos promedio; lo indico.
- No es asesoría de inversión: es un análisis contable para que la gerencia decida.
- Para presentarlo, me apoyo en `one-pager` o en `spreadsheet-helper` si quieres la hoja con
  fórmulas.

## Ejemplo

**Pedido:** «Comercializadora, quiero saber si podemos pedir un préstamo de Q500,000.»
**Entrega (resumen):** tabla de 13 razones con dos periodos; razón corriente 1.32 que baja desde 1.60
porque los días de cobro pasaron de 38 a 61; endeudamiento de 0.58; conclusión de que el préstamo es
viable si antes se mejora la cobranza, con tres acciones concretas.
