---
name: visit-report
description: "Convierte tus notas, fotos descritas o la transcripción de un audio de una visita técnica en un informe con hallazgos, trabajo realizado, repuestos necesarios, cotización sugerida y siguiente paso. Úsala cuando digas «haz el reporte de la visita de hoy», «pasa este audio a informe» o «qué repuestos le cotizo al cliente»."
---

# Reporte de visita técnica

Ordena lo que viste y lo que hiciste en una visita de servicio en un informe claro para el cliente y
para tu empresa, con lo que falta y lo que se debe cotizar.

## Cuándo usarla

- «Te paso mis notas de la visita al aire acondicionado del cliente, haz el reporte.»
- «Transcribí mi audio, conviértelo en informe.»
- «Saca la lista de repuestos para cotizar.»

## Qué necesito de ti

- Tus notas o la transcripción del audio (si tu IA no transcribe audio, usa la función de dictado del
  teléfono y pega el texto).
- Datos de la visita: cliente o código, dirección general, fecha, hora de llegada y salida, equipo
  (marca, modelo, número de serie si lo tienes).
- Fotos: descríbelas o adjúntalas si tu IA puede verlas.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Separo lo que el cliente reportó, lo que tú encontraste y lo que hiciste.
2. Escribo cada hallazgo con su causa probable y su gravedad (crítica: el equipo no funciona o es
   peligroso; media: funciona con falla; baja: mantenimiento preventivo).
3. Listo los repuestos y materiales con cantidad y especificación; si no me diste código o precio,
   lo marco como pendiente.
4. Defino el siguiente paso con responsable y fecha (cotizar, pedir repuesto, segunda visita).
5. Redacto un resumen de 3 líneas para el cliente, sin términos técnicos innecesarios.
6. Si hay riesgo de seguridad (eléctrico, gas, altura), lo pongo arriba y en negrita.

## Lo que te entrego

```text
REPORTE DE VISITA TÉCNICA No. ____
Cliente: [CLIENTE]   Lugar: ________   Fecha: dd/mm/aaaa   Llegada: __:__   Salida: __:__
Técnico: ________   Tipo de visita: Instalación | Correctivo | Preventivo | Diagnóstico
Equipo: ________   Marca/modelo: ________   Serie: ________
Reporte del cliente: ________
```

| No. | Hallazgo | Causa probable | Gravedad | Evidencia (foto/medición) |
|---:|---|---|---|---|
| 1 | | | Crítica / Media / Baja | |

```text
TRABAJO REALIZADO: 1. ____ 2. ____
ESTADO AL SALIR: Funcionando | Funcionando con observaciones | Fuera de servicio
```

| Repuesto o material | Especificación / código | Cantidad | ¿Lo tenemos? | Precio unitario (Q) |
|---|---|---:|---|---:|
| | | | Sí / No | [pendiente] |

```text
SIGUIENTE PASO: ________   Responsable: ________   Fecha: ________
RESUMEN PARA EL CLIENTE (listo para copiar): Buen día, [nombre]. Hoy revisamos su [equipo].
Encontramos [hallazgo principal]. Dejamos [estado]. Para dejarlo al 100 % se necesita [repuesto o
trabajo]; le envío la cotización a más tardar el [fecha].
Firma de conformidad del cliente: ________
```

## Reglas

- No invento mediciones, códigos de repuesto ni precios: lo que no está en tus notas queda
  pendiente.
- Separo hechos («el capacitor marcó 0 µF») de suposiciones («probablemente por sobrecarga»).
- Los riesgos de seguridad van primero y con la recomendación de no usar el equipo si aplica.
- No incluyo datos personales del cliente que no hagan falta; usa `data-shield` si las notas los
  traen.
- El resumen al cliente lo envías tú; nada se envía sin tu aprobación. Para cotizar los repuestos,
  sigue con `quote-builder`.

## Ejemplo

**Pedido:** «Audio: llegué 9:10, aire de 24 mil BTU no enfría, compresor no arranca, capacitor
inflado, lo cambié por uno que traía, quedó enfriando pero el filtro está muy sucio, hay que hacer
mantenimiento completo.»
**Entrega (resumen):** reporte de correctivo con 2 hallazgos (capacitor dañado, crítico, resuelto;
filtro saturado, media), trabajo realizado, repuesto usado y mantenimiento por cotizar, siguiente
paso con fecha y resumen de 3 líneas para el cliente.
