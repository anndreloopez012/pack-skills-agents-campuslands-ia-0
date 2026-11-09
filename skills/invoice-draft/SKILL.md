---
name: invoice-draft
description: "Prepara los datos para emitir la factura electrónica (FEL) y la nota de entrega, y revisa que NIT, montos, IVA y productos cuadren con la cotización o el pedido antes de emitir. Úsala cuando digas «prepara la factura de este pedido», «revisa antes de facturar» o «haz la nota de entrega»."
---

# Factura y entrega

Deja listos y revisados los datos que vas a ingresar en tu sistema de facturación electrónica y la
nota de entrega que firma el cliente, para no tener que anular facturas por errores.

## Cuándo usarla

- «El cliente aceptó la cotización, prepara los datos de la factura.»
- «Revisa esta factura antes de que la emita.»
- «Haz la nota de entrega para que la firme quien recibe.»

## Qué necesito de ti

- La cotización aceptada o el pedido confirmado.
- Datos fiscales del cliente: NIT o CUI (o consumidor final, «CF», si aplica), nombre como aparece en
  la SAT y dirección.
- Tu régimen de IVA (general o pequeño contribuyente) y si el cliente es agente de retención.
- Forma de pago y si es al contado o al crédito.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Comparo línea por línea el pedido con la cotización: producto, cantidad, precio y descuento.
2. Reviso los datos del receptor: que el NIT tenga formato válido y que el nombre sea el que tú
   confirmaste en la consulta de NIT de la SAT. Yo no consulto el NIT: te recuerdo hacerlo.
3. Verifico el monto: a partir de cierto total la SAT exige identificar al comprador con NIT o CUI y
   no permite «CF»; te pido confirmar el monto vigente en el portal.
4. Calculo base e IVA (12 % en régimen general) y reviso que el total cuadre con la cotización.
5. Si el cliente es agente de retención, te aviso que te puede retener IVA o ISR y que debes pedir la
   constancia.
6. Armo la nota de entrega con las mismas cantidades de la factura.

## Lo que te entrego

```text
DATOS PARA LA FEL (para copiar en tu sistema de facturación)
Tipo de documento: Factura | Factura cambiaria (si es al crédito) | Nota de crédito
Receptor: NIT/CUI ________   Nombre según SAT: ________   Dirección: ________
Moneda: GTQ   Fecha de emisión: dd/mm/aaaa
```

| No. | Bien o servicio | Descripción | Cantidad | Precio unitario con IVA (Q) | Descuento (Q) | Total línea (Q) |
|---:|---|---|---:|---:|---:|---:|
| 1 | Bien | | | | | |

```text
Total: Q____   Base: Q____   IVA 12 %: Q____   Total en letras: ________
Condición: contado | crédito ___ días   Retención esperada del cliente: Sí / No

REVISIÓN ANTES DE EMITIR
[ ] Cantidades y precios = cotización COT-____
[ ] NIT y nombre confirmados en la consulta de la SAT
[ ] Monto permite «CF» o se identificó al comprador (confirmar el monto vigente)
[ ] Total en letras = total en números
[ ] Descuentos autorizados

NOTA DE ENTREGA No. ____   Fecha: ________   Factura relacionada: serie ___ No. ___
Cliente: ________   Dirección de entrega: ________
No. | Descripción | Cantidad entregada | Observaciones (estado del producto)
Recibí conforme: Nombre ________  Firma ________  Fecha y hora ________
```

## Reglas

- No emito facturas: preparo los datos; tú emites en tu sistema y certificador.
- Si algo no cuadra con la cotización, lo marco y no doy la revisión por buena.
- IVA de referencia 12 %; reglas sobre «CF», factura cambiaria y retenciones se verifican en
  portal.sat.gob.gt (revisado: noviembre de 2026).
- Si hay que corregir una factura ya emitida, te recuerdo que se hace con nota de crédito o
  anulación según el procedimiento de la SAT; lo confirma tu contador.
- Nada se envía al cliente sin tu aprobación; si quieres, te dejo el mensaje para WhatsApp.

## Ejemplo

**Pedido:** «Facturar la cotización COT-2026-041, cliente con NIT, al crédito 30 días.»
**Entrega (resumen):** datos para factura cambiaria con 3 líneas, total Q12,880.00 (base Q11,500.00,
IVA Q1,380.00), aviso de que el cliente es agente de retención, lista de revisión con un precio que no
coincidía con la cotización, y nota de entrega lista para firma.
