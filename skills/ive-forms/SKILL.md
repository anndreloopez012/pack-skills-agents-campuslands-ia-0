---
name: ive-forms
description: "Prepara y revisa la información que piden los formularios y reportes de la IVE (Intendencia de Verificación Especial): conocimiento del cliente, beneficiario final, PEP, origen de fondos y transacciones en efectivo. Úsala cuando digas «revisa este formulario IVE», «qué le falta a este expediente» o «prepara la información del cliente para la IVE»."
---

# Formularios IVE

Ordena y revisa la información de conocimiento del cliente que exigen las normas de prevención de
lavado de dinero en Guatemala, para que el expediente esté completo antes de firmarlo o enviarlo.

## Cuándo usarla

- «Revisa si este formulario de inicio de relación está completo.»
- «Qué documentos le pido a un cliente nuevo para su expediente.»
- «Este cliente pagó en efectivo un monto alto, ¿qué debo registrar?»
- «Prepara el perfil del cliente con lo que me dio.»

## Qué necesito de ti

- Si eres persona obligada ante la IVE o trabajas para una (banco, aseguradora, cooperativa,
  casa de cambio u otra actividad que la ley incluya), y qué tipo.
- El formulario o la lista de campos que te pide tu entidad (cada sujeto obligado tiene los suyos).
- La información del cliente que ya tienes. Recomiendo `data-shield`: puedo revisar completitud con
  etiquetas en lugar de DPI, NIT o cuentas reales.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Confirmo el tipo de cliente (persona individual o jurídica) y el tipo de relación o transacción.
2. Reviso campo por campo contra el formulario de tu entidad: identificación, actividad económica,
   ingresos, propósito de la relación, origen de fondos y perfil transaccional esperado.
3. Para personas jurídicas, verifico que esté identificado el beneficiario final (las personas
   individuales que la controlan o son dueñas en última instancia) y el representante legal.
4. Reviso si el cliente o sus allegados son personas expuestas políticamente (PEP) según lo que tú
   me indiques, y qué debida diligencia ampliada pide tu entidad en ese caso.
5. Marco las transacciones que superan el umbral de reporte de efectivo que te aplique (la referencia
   habitual es el equivalente a US$10,000, sea en una o en varias operaciones; confírmalo).
6. Señalo inconsistencias: ingresos declarados que no cuadran con el volumen, actividad poco clara,
   documentos vencidos, direcciones incompletas.
7. Entrego la lista de faltantes y el resumen del perfil, sin decidir si algo es sospechoso.

## Lo que te entrego

```text
REVISIÓN DE EXPEDIENTE   Cliente: [CLIENTE_01]   Tipo: Individual | Jurídica   Fecha: ________
Formulario de referencia: [el de tu entidad, con su código]
```

| Sección | Campo | Estado (Completo / Falta / Inconsistente) | Documento que lo respalda | Acción |
|---|---|---|---|---|
| Identificación | Documento de identidad vigente | | DPI / pasaporte | |
| Actividad | Actividad económica y fuente de ingresos | | Constancia, patente, estados financieros | |
| Origen de fondos | Explicación y soporte | | | |
| Beneficiario final | Personas que controlan o son dueñas | | Registro de accionistas | |
| PEP | ¿Es PEP o allegado? | | Declaración del cliente | |
| Perfil | Monto y frecuencia esperada de operaciones | | | |

```text
TRANSACCIONES EN EFECTIVO SOBRE EL UMBRAL: fecha | monto | moneda | registrada en formulario: Sí/No
SEÑALES A EVALUAR (las evalúa el oficial de cumplimiento, no la IA): 1. ____ 2. ____
FALTANTES PARA COMPLETAR: 1. ____ 2. ____
```

## Reglas

- Marco legal de referencia: Ley contra el Lavado de Dinero u Otros Activos (Decreto 67-2001), Ley
  para Prevenir y Reprimir el Financiamiento del Terrorismo (Decreto 58-2005) y su normativa. Verifica
  formularios, umbrales y plazos vigentes en ive.org.gt y con tu oficial de cumplimiento (revisado:
  noviembre de 2026).
- No invento códigos de formulario: uso el que tu entidad te dé.
- La decisión de reportar una transacción sospechosa es del oficial de cumplimiento. La IA no la
  toma ni la redacta como conclusión.
- Confidencialidad: nunca se le avisa al cliente que se analiza o se reporta una operación; no
  preparo mensajes al cliente sobre eso.
- No subo datos reales de clientes si no hace falta: trabajo con etiquetas.

## Ejemplo

**Pedido:** «Sociedad anónima nueva, me dio escritura, DPI del representante y dice que sus fondos
vienen de ventas.»
**Entrega (resumen):** expediente con 6 secciones; faltan beneficiario final, soporte del origen de
fondos y declaración PEP; perfil transaccional sin llenar; dos acciones para pedirle al cliente.
