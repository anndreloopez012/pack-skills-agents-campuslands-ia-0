---
name: internal-control
description: "Evalúa el control interno con el marco COSO en procesos de compras, ventas, cobros, pagos, inventarios y caja; arma arqueos y propone recomendaciones. Úsala cuando digas «evalúa los controles de compras», «haz un arqueo de caja chica» o «qué riesgos tiene este proceso de cobros»."
---

# Control interno COSO

Revisa cómo se hace un proceso, encuentra dónde puede haber error o fraude y propone controles
sencillos y proporcionales al tamaño de la empresa.

## Cuándo usarla

- «Evalúa el proceso de compras: así lo hacemos hoy.»
- «Arma el formato y la cédula del arqueo de caja chica.»
- «¿Qué riesgos tiene que la misma persona cobre y registre?»
- Durante una auditoría interna o externa, junto con `audit-planning`.

## Qué necesito de ti

- La descripción del proceso: quién hace qué, con qué documento y en qué sistema. Si no la tienes
  escrita, primero usa `process-mapper`.
- Organigrama o lista de puestos que intervienen (sin nombres; basta el puesto).
- Para arqueos: fondo autorizado, conteo de billetes y monedas, vales y facturas pendientes.
- Hallazgos o incidentes anteriores, si los hay.
- Si falta algo, hago como máximo 3 preguntas cortas y sigo con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Divido el proceso en pasos: autorización, ejecución, registro, custodia y revisión.
2. Busco riesgos en cada paso: segregación de funciones incompatibles, falta de autorización,
   documentos sin numeración, accesos al sistema compartidos, ausencia de conciliaciones.
3. Ubico cada control en los 5 componentes de COSO (2013): entorno de control, evaluación de
   riesgos, actividades de control, información y comunicación, y supervisión.
4. Califico el diseño (¿el control existe y cubre el riesgo?) y, si me das evidencia, la
   operación (¿se cumple en la práctica?).
5. Propongo controles concretos y baratos primero (firmas, conciliaciones, topes, doble revisión)
   antes de sistemas costosos.
6. Si es arqueo, cuadro: efectivo contado + documentos pendientes = fondo autorizado, y explico el
   faltante o sobrante.

## Lo que te entrego

```text
EVALUACIÓN DE CONTROL INTERNO   Proceso: ________   Fecha: ________   Evaluó: ________
```

| No. | Paso del proceso | Riesgo (qué puede salir mal) | Control actual | Componente COSO | Diseño (Adecuado / Débil / No existe) | Operación (Efectiva / No efectiva / No probada) | Recomendación | Prioridad |
|---|---|---|---|---|---|---|---|---|
| 1 | Aprobación de la orden de compra | Compras sin necesidad real o a proveedor relacionado | Ninguno | Actividades de control | No existe | No probada | Tope de aprobación por monto y tres cotizaciones arriba de Q____ | Alta |

Matriz de segregación de funciones:

| Puesto | Autoriza | Ejecuta | Registra | Custodia | Conflicto |
|---|---|---|---|---|---|

```text
ARQUEO DE CAJA   Fondo: ________   Responsable (puesto): ________   Fecha y hora: ________
Billetes y monedas (denominación × cantidad): Q____
Facturas y vales pendientes de reintegro:     Q____
Total arqueado:                                Q____
Fondo autorizado:                              Q____
Diferencia (faltante / sobrante):              Q____  Explicación: ____
Firmas: responsable del fondo ____  quien arquea ____
```

## Reglas

- COSO como marco; no cito números de principio que no corresponda. Los 5 componentes y los 17
  principios se verifican en la versión vigente de COSO (revisado: noviembre de 2026).
- Recomendaciones proporcionales: en una empresa de 5 personas propongo controles compensatorios
  (revisión del dueño) en lugar de segregación imposible.
- No acuso a personas: hablo de puestos y de riesgos.
- Si veo indicios de fraude, lo marco con cuidado como «situación que amerita investigación» y
  sugiero escalar a la gerencia o al auditor; no saco conclusiones.
- El arqueo se hace por sorpresa y frente al responsable; la IA solo prepara el formato y el cuadre.
- Los hallazgos los paso a `audit-letters` si van en la carta a la gerencia.

## Ejemplo

**Pedido:** «La misma persona recibe los cobros en efectivo, hace el depósito y registra en el
sistema.»
**Entrega (resumen):** tres riesgos (apropiación, registro tardío, depósitos incompletos), matriz de
segregación con el conflicto marcado, y cuatro controles: depósito diario completo, conciliación
semanal por otra persona, recibos prenumerados y revisión mensual del gerente.
