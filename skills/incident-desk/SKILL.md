---
name: incident-desk
description: "Registra, prioriza y responde las solicitudes de ocupantes y personal de un edificio (fugas, luces, aire, limpieza, acceso), con tiempos de atención y respuesta lista para enviar. Pídela así: «ordena estas solicitudes de los inquilinos», «responde a este reclamo de la fuga»."
---

# Atención de solicitudes

Convierte mensajes sueltos de WhatsApp, correo o recepción en una mesa de solicitudes ordenada, con
prioridad, responsable y respuesta. Para administradores de edificios y equipos de mantenimiento.

## Cuándo usarla

- «Me llegaron 20 mensajes de inquilinos hoy, ordénalos».
- «Responde con cortesía a este reclamo por el aire del nivel 4».
- «Cuántas solicitudes cerramos este mes y en cuánto tiempo».

## Qué necesito de ti

- Los mensajes o solicitudes tal como llegaron (texto, captura transcrita o lista).
- Equipo disponible: técnicos propios, proveedores por sistema y horario.
- Si los mensajes traen nombres, teléfonos o números de apartamento que vayas a compartir, propone
  usar `data-shield` antes.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Separo cada solicitud aunque vengan varias en un mensaje y le pongo un número.
2. La clasifico por sistema: sanitarios, eléctrico, iluminación, aire, ascensor, agua, seguridad y
   acceso, limpieza, áreas comunes, otro.
3. Asigno prioridad con esta regla:
   - **P1 Crítica (atender ya, meta 1 hora):** riesgo a personas o al edificio: humo, chispas,
     persona atrapada en ascensor, fuga grande, sin agua en todo el edificio.
   - **P2 Alta (mismo día):** afecta el trabajo de un área: sin aire en un nivel, inodoro fuera de
     servicio, falla de acceso.
   - **P3 Media (hasta 3 días hábiles):** molestia sin urgencia: luminaria quemada, puerta que roza.
   - **P4 Baja (programar):** mejoras o solicitudes estéticas.
4. Propongo responsable (técnico propio o proveedor) y redacto la respuesta al solicitante: acuse,
   qué se hará y cuándo.
5. Al cierre del periodo calculo indicadores: solicitudes recibidas, cerradas, tiempo medio de
   atención por prioridad y sistemas que más fallan.

## Lo que te entrego

```
MESA DE SOLICITUDES - <Edificio> - Fecha: __/__/____
| N.º | Fecha y hora | Solicitante (etiqueta) | Nivel / local | Sistema | Descripción | Prioridad | Responsable | Fecha compromiso | Estado (Nueva/En curso/Esperando pieza/Cerrada) | Cierre (fecha y hora) |

RESPUESTAS LISTAS PARA APROBAR
N.º __ - Para: <solicitante>
"Buenos días, recibimos su reporte de <problema> en <lugar>. <Responsable> lo atenderá <cuándo>. Le avisaremos al terminar."

INDICADORES DEL PERIODO
| Prioridad | Recibidas | Cerradas | Tiempo medio de atención (h) | Meta (h) | Dentro de meta % |
Sistemas con más solicitudes: 1) ___ 2) ___ 3) ___  -> revisar en `maintenance-checklist`
```

## Reglas

- Lo P1 va primero en la lista y con aviso de llamar, no solo escribir.
- No prometo fechas que el equipo no puede cumplir: si falta una pieza, lo digo.
- Respuestas cordiales y cortas, en español de Guatemala; para tono delicado uso `pro-writer`.
- Nada se envía a los ocupantes sin tu aprobación.
- Si un mismo problema se repite tres veces en un mes, lo marco como falla recurrente para
  mantenimiento preventivo.
- Sin emojis.

## Ejemplo

**Pedido:** «Lista de 9 mensajes de hoy de inquilinos».
**Entrega (resumen):** 11 solicitudes (dos mensajes traían dos cada uno): 1 P1 (olor a quemado en
tablero del nivel 3, llamar al electricista ya), 3 P2, 5 P3 y 2 P4, con responsables, fechas y 11
respuestas listas para aprobar.
