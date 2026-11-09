---
name: audit-planning
description: "Arranca un encargo de auditoría con el entendimiento del cliente, la materialidad, la matriz de riesgos y el memorando o carta de planificación, siguiendo las NIA. Úsala cuando digas «planifica la auditoría de este cliente», «calcula la materialidad» o «arma la matriz de riesgos»."
---

# Planificación de auditoría

Prepara la planificación de una auditoría de estados financieros: materialidad, riesgos de
incorrección material y respuesta del auditor, siguiendo las Normas Internacionales de Auditoría
(NIA/ISA).

## Cuándo usarla

- «Planifica la auditoría del año del cliente X.»
- «Calcula la materialidad con estos estados financieros.»
- «Arma la matriz de riesgos y los procedimientos para cada área.»
- Antes de correr el agente `audit-workpapers`.

## Qué necesito de ti

- Estados financieros o balanza del periodo y del anterior.
- Giro del cliente, tamaño, sistemas que usa, cambios importantes del año (nuevos préstamos, nuevas
  líneas de negocio, cambio de gerencia) y hallazgos de auditorías anteriores.
- Tipo de encargo (auditoría externa, interna, especial) y fecha de entrega del informe.
- Propongo pasar la información por `data-shield` si trae nombres, NIT o cuentas.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Resumo el entendimiento de la entidad y su entorno: negocio, ingresos principales, regulación
   (SAT, IGSS, y supervisor si aplica), sistemas y control interno general (NIA 315).
2. Hago procedimientos analíticos preliminares: variaciones relevantes entre años y razones clave
   (apoyo en `financial-ratios`); cada variación grande es una pista de riesgo.
3. Propongo la materialidad global, la de ejecución y el umbral de errores claramente
   insignificantes (NIA 320 y NIA 450), con la base elegida y la justificación. Los porcentajes son
   rangos de práctica profesional; la decisión es del juicio del auditor.
4. Identifico riesgos de incorrección material por área y aserción, incluyendo los que la norma trata
   como significativos por defecto: riesgo de fraude en el reconocimiento de ingresos (presunción
   refutable) y elusión de controles por la dirección (NIA 240).
5. Para cada riesgo defino la respuesta: pruebas de controles, procedimientos sustantivos,
   naturaleza, alcance y momento (NIA 330).
6. Redacto el memorando de planificación con equipo, cronograma y comunicaciones al cliente (NIA 300).

## Lo que te entrego

```text
MEMORANDO DE PLANIFICACIÓN   Cliente: ________   Periodo: ________   Preparó/Revisó: ____ / ____
1. Entendimiento de la entidad (5 a 8 puntos)
2. Analítica preliminar: variaciones relevantes y lo que podrían indicar
```

| Materialidad | Base | Monto base (Q) | % aplicado | Monto (Q) | Justificación |
|---|---|---:|---:|---:|---|
| Global | Utilidad antes de ISR / Ingresos / Activos | | rango de práctica | | |
| De ejecución | % de la global | | | | |
| Errores claramente insignificantes | % de la global | | | | |

| Área | Aserción | Riesgo identificado | Inherente (A/M/B) | Control (A/M/B) | ¿Significativo? | ¿Fraude? | Respuesta planificada | Cédula |
|---|---|---|---|---|---|---|---|---|
| Ingresos | Ocurrencia, corte | Ventas registradas en el periodo equivocado | A | M | Sí | Sí | Corte de FEL 10 días antes y después del cierre | |
| Cuentas por cobrar | Existencia, valuación | | | | | | Confirmaciones (NIA 505) y antigüedad | |
| Inventarios | Existencia | | | | | | Observación de toma física (NIA 501) | |

```text
3. Cronograma: planificación ___ | interina ___ | final ___ | informe ___
4. Equipo y horas por área
5. Comunicaciones: carta de encargo, solicitud de información (lista PBC), reunión de inicio
6. Temas abiertos para el socio o encargado
```

## Reglas

- Cito las NIA por número y tema (300, 315, 320, 330, 240, 450, 501, 505, 530); no cito números de
  párrafo. Verifica la versión vigente de las NIA adoptadas en Guatemala y el Código de Ética del
  IESBA (revisado: noviembre de 2026).
- La materialidad y la evaluación de riesgos son juicio profesional del auditor; presento propuestas
  con su razonamiento, no decisiones.
- No invento hallazgos ni saldos; lo que falta queda como «solicitar al cliente».
- La independencia y la aceptación del cliente las confirma el auditor antes de empezar.
- Para controles por proceso me apoyo en `internal-control`; para las cartas, en `audit-letters`.

## Ejemplo

**Pedido:** «Distribuidora con ingresos de Q12 millones y utilidad antes de ISR de Q900,000.»
**Entrega (resumen):** materialidad global propuesta sobre la utilidad antes de ISR con su rango y
justificación, materialidad de ejecución y umbral; 9 riesgos en la matriz, dos significativos
(ingresos y valuación de inventarios); cronograma de 6 semanas y lista de información para el
cliente.
