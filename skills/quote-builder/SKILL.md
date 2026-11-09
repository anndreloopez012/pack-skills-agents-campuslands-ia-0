---
name: quote-builder
description: "Convierte un mensaje de WhatsApp o un correo del cliente en una cotización completa con productos, precios, IVA, plazo de entrega, forma de pago y vigencia, más el mensaje listo para copiar. Úsala cuando digas «cotízale esto a este cliente», «arma la cotización de este WhatsApp» o «pásame esto a cotización formal»."
---

# Cotizaciones rápidas

Del mensaje desordenado del cliente a una cotización clara, con números que cuadran, y el texto
listo para pegar en WhatsApp o en un correo.

## Cuándo usarla

- «Me escribió esto por WhatsApp, cotízale.»
- «Arma la cotización formal de este pedido para mandarla en PDF.»
- «El cliente pide descuento por volumen, recalcula.»

## Qué necesito de ti

- El mensaje del cliente tal como llegó (pégalo; no necesito su número de teléfono).
- Tu lista de precios o los precios de cada producto o servicio, y si incluyen IVA o no.
- Tus condiciones: forma de pago (contado, crédito a 30 días, anticipo), plazo de entrega, vigencia
  de la cotización, garantía, costo de envío.
- Datos de tu empresa para el encabezado (nombre comercial, NIT si lo quieres incluir).
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Leo el mensaje y extraigo lo que pide: producto, cantidad, medida o modelo, lugar y fecha de
   entrega.
2. Marco lo ambiguo («una caja» ¿de cuántas unidades?) y te propongo la pregunta para el cliente en
   lugar de adivinar.
3. Armo las líneas con cantidad × precio unitario = subtotal; aplico descuentos solo si tú los
   autorizas.
4. Calculo el IVA: si tus precios no incluyen IVA, sumo 12 %; si lo incluyen, muestro la base
   (total / 1.12) y el IVA. Si eres pequeño contribuyente, no desgloso IVA y lo indico.
5. Reviso que la suma cuadre y que el total en letras coincida con el total en números.
6. Redacto el mensaje corto para WhatsApp y, si lo pides, la versión de correo.

## Lo que te entrego

```text
COTIZACIÓN No. COT-aaaa-___        Fecha: dd/mm/aaaa        Vigencia: hasta dd/mm/aaaa
De: [Tu empresa]   Para: [Cliente / empresa]   Atención: [contacto]
```

| No. | Descripción | Cantidad | Unidad | Precio unitario (Q) | Descuento | Subtotal (Q) |
|---:|---|---:|---|---:|---:|---:|
| 1 | | | | | | |
| | | | | | **Subtotal** | |
| | | | | | **IVA 12 %** | |
| | | | | | **Total** | |

```text
Total en letras: ________ quetzales con __/100
Forma de pago: ________   Plazo de entrega: ________   Lugar de entrega: ________
Garantía: ________   Incluye: ________   No incluye: ________
Notas: precios sujetos a existencias; cotización válida hasta la fecha indicada.

MENSAJE PARA WHATSAPP (listo para copiar):
Buen día, [nombre]. Le comparto la cotización de [producto]: [cantidad] por un total de Q____
con IVA incluido, entrega en [plazo]. Forma de pago: [condición]. Vigente hasta el [fecha].
¿Le confirmo el pedido?

PREGUNTAS PARA EL CLIENTE (si hay dudas): 1. ____
```

## Reglas

- Nunca invento precios, existencias ni plazos: si no me das el precio, la línea queda «[precio
  pendiente]».
- Descuentos solo con tu autorización y dentro del margen que me indiques.
- IVA de referencia 12 %; verifica en portal.sat.gob.gt (revisado: noviembre de 2026).
- WhatsApp normal no se puede automatizar: te dejo el texto y tú lo copias y lo envías.
- Nada se envía sin tu aprobación.
- Sin promesas que no puedes cumplir («entrega hoy mismo») ni presión falsa («últimas unidades») si
  no es cierto.
- Para la factura cuando el cliente acepte, sigue con `invoice-draft`.

## Ejemplo

**Pedido:** «Cliente: necesito 20 resmas carta y 5 cajas de lapiceros azules para el lunes en zona
10. Resma Q38 y caja Q45, precios con IVA.»
**Entrega (resumen):** cotización con 2 líneas, total Q985.00 con base Q879.46 e IVA Q105.54, total
en letras, condiciones y mensaje de WhatsApp listo; una pregunta al cliente sobre la dirección
exacta y el horario de entrega.
