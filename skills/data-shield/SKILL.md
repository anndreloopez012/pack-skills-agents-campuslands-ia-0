---
name: data-shield
description: "Antes de trabajar un documento con IA, reemplaza nombres, DPI, NIT, cuentas, teléfonos, correos, direcciones y salarios por etiquetas como [PERSONA-1] o [NIT-1], te entrega la tabla de correspondencias para guardarla aparte y te avisa qué no debe pegarse nunca en una IA. Úsala con «quita los datos personales», «anonimiza este listado», «puedo pegar esto en la IA»."
---

# Protege tus datos

Prepara tus documentos para trabajarlos con IA sin exponer a personas, clientes ni a tu empresa.
Para cualquiera que maneja planillas, expedientes, listados de clientes o estados de cuenta.

## Cuándo usarla

- «Quita los datos personales de este listado antes de analizarlo.»
- «¿Puedo pegar este contrato en la IA?»
- «Voy a pedir un resumen de expedientes de alumnos.»
- Cuando otra skill del pack detecta datos sensibles y te la propone.

## Qué necesito de ti

- El texto o la tabla. Si es muy sensible, mejor pega solo una muestra o la estructura (nombres
  de columnas) y yo te digo cómo anonimizar el resto en tu computadora.
- Qué análisis quieres hacer después, para saber qué dato conviene conservar (por ejemplo, el
  departamento sí, la dirección exacta no).
- Si falta algo importante, hago como máximo 3 preguntas cortas y sigo con supuestos marcados
  como «Supuesto:».

## Cómo trabajo

1. Primero reviso si hay algo que **no debe pegarse en ninguna IA personal**: contraseñas, PIN,
   códigos de verificación, tokens o claves de sistemas, números completos de tarjeta con su
   código, y documentos de clientes bajo acuerdo de confidencialidad. Si lo hay, te pido que lo
   borres y no lo proceso.
2. Busco y reemplazo con etiquetas numeradas, siempre la misma etiqueta para el mismo dato:
   - Nombres de personas → [PERSONA-1], [PERSONA-2]
   - Empresas o clientes → [EMPRESA-1]
   - DPI / CUI → [DPI-1]   NIT → [NIT-1]   Pasaporte → [PASAPORTE-1]
   - Cuentas bancarias o de préstamo → [CUENTA-1]   Tarjetas → [TARJETA-1]
   - Teléfonos → [TEL-1]   Correos → [CORREO-1]   Direcciones → [DIRECCION-1]
   - Salarios, saldos o montos individuales → [MONTO-1] o rangos («entre Q 5,000 y Q 7,000») si
     el análisis necesita la magnitud
   - Números de expediente, carné, afiliación al IGSS → [EXPEDIENTE-1], [IGSS-1]
3. Conservo lo que no identifica a nadie y sirve al análisis: cargo, departamento, mes, categoría.
4. Reviso combinaciones que delatan aunque no haya nombre («la única gerenta de la agencia de
   Salamá») y las generalizo.
5. Te entrego el texto protegido y, por separado, la tabla de correspondencias.

## Lo que te entrego

```
TEXTO PROTEGIDO (este sí puedes usarlo con la IA):
...

TABLA DE CORRESPONDENCIAS — guárdala aparte, en tu computadora, NO la pegues en la IA
| Etiqueta | Dato original |
|---|---|
| [PERSONA-1] | |
| [NIT-1] | |

RESUMEN: [n] datos reemplazados — tipos: ...
NO PROCESADO (bórralo del original): [contraseñas, tarjetas, etc., o «nada»]
RIESGOS QUE QUEDAN: [combinaciones que aún podrían identificar a alguien]
```

Cuando la IA te devuelva el resultado, reemplaza las etiquetas con tu tabla (en Word o Excel:
Buscar y reemplazar).

## Reglas

- La tabla de correspondencias es tuya: no la vuelvo a pedir ni la uso en otros pedidos.
- Nunca pido contraseñas, tokens ni datos de tarjetas, ni para «protegerlos».
- Si el documento es de tu trabajo, usa la IA aprobada por tu empresa o institución y respeta
  sus políticas; esta skill reduce el riesgo, no lo elimina.
- En banca, salud, educación y gobierno hay datos protegidos por normas y contratos: ante la
  duda, pregunta a tu área de cumplimiento antes de usar IA.
- Si me pegas el documento completo en una IA personal, el dato ya salió: lo ideal es
  anonimizar antes o trabajar solo con la estructura.

## Ejemplo

**Pedido:** «Quita los datos personales de este listado de 40 empleados (nombre, DPI, NIT,
salario, teléfono, puesto, agencia) antes de analizar la planilla por agencia.»
**Entrega (resumen):** Tabla con [PERSONA-1] a [PERSONA-40], DPI, NIT y teléfono reemplazados,
salario convertido a rangos de Q 1,000, puesto y agencia conservados. Aviso de riesgo: en la
agencia de Retalhuleu hay un solo jefe, así que su rango salarial lo identifica; se propone
agrupar Retalhuleu con Mazatenango. Tabla de correspondencias aparte para guardar.
