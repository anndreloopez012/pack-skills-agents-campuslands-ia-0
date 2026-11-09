---
name: inbox-triage
description: "Ordena los correos y mensajes que pegas en cinco grupos (Urgente hoy, Hoy, Esta semana, Solo leer, Delegar), con el motivo, la acción y un borrador de respuesta. Úsala con «ordena mi bandeja», «cuáles contesto primero», «tengo 30 correos sin leer»."
---

# Ordena mi bandeja

Convierte una bandeja llena en una lista corta de qué contestar primero, qué puede esperar y qué
pasar a otra persona. Para quien recibe muchos correos y mensajes y no sabe por dónde empezar.

## Cuándo usarla

- «Ordena estos 15 correos y dime cuáles contesto primero.»
- «Volví de vacaciones y tengo 60 correos.»
- «Te pego los mensajes del grupo de clientes: ¿qué necesita respuesta hoy?»

## Qué necesito de ti

- Los correos o mensajes copiados y pegados (asunto, remitente, fecha y texto). Funciona con
  correo, Teams, Slack o mensajes de WhatsApp que copies a mano. WhatsApp normal no se conecta
  ni se automatiza: tú copias, yo ordeno.
- Tu cargo y qué te importa más (por ejemplo: «soy contadora, lo de la SAT va primero»).
- A quién puedes delegar (nombres o puestos).
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados
  como «Supuesto:».

## Cómo trabajo

1. Si los mensajes traen DPI, NIT, cuentas, salarios o datos de clientes, te propongo pasarlos
   antes por `data-shield`.
2. Leo cada mensaje y anoto quién lo manda, qué pide y para cuándo.
3. Lo clasifico con estas reglas:
   - **Urgente hoy:** vence hoy, hay dinero, multa, cliente molesto o un jefe esperando.
   - **Hoy:** pide respuesta y conviene darla antes de cerrar el día.
   - **Esta semana:** importante pero con plazo de varios días.
   - **Solo leer:** avisos, copias, boletines; no piden nada.
   - **Delegar:** otra persona lo resuelve mejor; digo a quién y por qué.
4. Detecto posibles engaños (premios, cambios de cuenta bancaria, enlaces raros, urgencia
   falsa) y los marco como «Posible fraude: no responder ni abrir enlaces».
5. Para cada mensaje que pide respuesta escribo un borrador corto con el tono adecuado
   (apoyándome en `pro-writer` cuando es formal).
6. Cierro con las 3 respuestas que conviene mandar primero.

## Lo que te entrego

```
BANDEJA ORDENADA — [fecha] — [n] mensajes revisados

LAS 3 PRIMERAS: 1) ... 2) ... 3) ...

| # | Grupo | De | Asunto | Motivo | Acción | Plazo |
|---|---|---|---|---|---|---|
| 1 | Urgente hoy | | | | Responder / Llamar / Pagar / Revisar | hoy 12:00 |
| 2 | Delegar | | | | Reenviar a [persona] con nota | |
| 3 | Solo leer | | | | Archivar | — |

BORRADORES
[#1] Para: ...   Asunto: Re: ...
Texto: ...

[#2] Nota para delegar a [persona]: ...

POSIBLE FRAUDE: [# y motivo] (o «ninguno detectado»)
SUPUESTOS: ...
```

## Reglas

- Ordeno y propongo; tú decides y tú envías. Nunca mando, borro ni reenvío nada.
- El motivo de cada clasificación va en una frase concreta, no «parece importante».
- Los borradores son cortos (máximo 6 líneas), en español de Guatemala y sin frases de robot;
  si quieres, los paso por `human-voice`.
- No invento fechas ni montos que no estén en el mensaje; si falta, lo digo.
- Nunca pido contraseñas, códigos de verificación ni datos de tarjetas, aunque un mensaje los
  solicite.
- Si un mensaje es de un cliente bajo confidencialidad, recuerda usar la IA aprobada por tu
  empresa.

## Ejemplo

**Pedido:** «Ordena estos 8 correos. Soy jefa de ventas en una distribuidora de Mixco; puedo
delegar a Kevin (bodega) y a Ana (facturación).»
**Entrega (resumen):** Urgente hoy: el reclamo de Ferretería El Progreso por un pedido incompleto
de Q 4,800 y la cotización que vence a las 15:00. Delegar: a Ana la corrección de una factura FEL;
a Kevin la consulta de existencias. Solo leer: dos boletines y una copia del gerente. Posible
fraude: un correo que pide «actualizar la cuenta para el pago» desde un dominio distinto al del
proveedor. Con borradores para los tres que piden respuesta.
