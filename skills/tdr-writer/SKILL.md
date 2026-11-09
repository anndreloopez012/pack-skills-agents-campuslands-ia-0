---
name: tdr-writer
description: "Redacta términos de referencia (TDR) y especificaciones técnicas claras para contratar bienes, servicios u obras por Guatecompras, conforme a la Ley de Contrataciones del Estado. Úsala cuando digas «redacta los TDR de esta consultoría», «arma las especificaciones técnicas» o «revisa si mis TDR dirigen la compra»."
---

# Términos de referencia

Prepara los TDR o las especificaciones técnicas de una contratación pública para que los
oferentes entiendan qué se pide, cómo se evalúa y cómo se paga, sin dirigir la compra a un
proveedor.

## Cuándo usarla

- «Redacta los TDR para contratar una consultoría de diagnóstico institucional».
- «Arma las especificaciones técnicas de 20 computadoras».
- «Revisa estos TDR antes de publicarlos en Guatecompras».

## Qué necesito de ti

- Qué se necesita y para qué (el problema que resuelve).
- Monto estimado en quetzales (Q) y plazo de ejecución.
- Productos o entregables esperados, y quién los recibe y aprueba.
- Perfil requerido (para servicios) o características mínimas (para bienes).
- La modalidad prevista (baja cuantía, compra directa, cotización, licitación u otra) si ya la
  definió la unidad de compras.
- Si falta algo importante, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como
  «Supuesto:».

## Cómo trabajo

1. Confirmo el objeto de la contratación en una frase y su vínculo con el POA y el renglón
   presupuestario (con `budget-classifier`).
2. Redacto antecedentes y justificación breves: por qué la institución lo necesita ahora.
3. Defino objetivo general y específicos, alcance (lo que incluye y lo que no) y actividades.
4. Detallo productos o entregables con contenido mínimo, formato, fecha y porcentaje de pago
   asociado.
5. Para bienes: especificaciones funcionales y de desempeño mínimas, garantía, entrega e
   instalación. Uso «o similar o superior» y evito marcas, modelos o medidas que solo cumple un
   proveedor.
6. Perfil del oferente o del consultor: formación, experiencia general y específica, y cómo se
   acredita.
7. Criterios de evaluación y calificación con puntajes que sumen 100, verificables con documentos.
8. Condiciones: plazo, lugar, forma de pago, supervisión, confidencialidad, propiedad de los
   productos y garantías o seguros que correspondan.
9. Reviso que el texto no dirija la compra y que cada requisito se pueda verificar.

## Lo que te entrego

```
TÉRMINOS DE REFERENCIA
1. Antecedentes
2. Justificación
3. Objetivo general y objetivos específicos
4. Alcance y actividades
5. Productos esperados
| Producto | Contenido mínimo | Fecha de entrega | % de pago |
6. Especificaciones técnicas (bienes) o perfil requerido (servicios)
| Característica | Requisito mínimo | Cómo se verifica |
7. Criterios de evaluación
| Criterio | Puntaje | Documento que lo acredita |
8. Plazo, lugar y forma de pago
9. Supervisión y aprobación de productos
10. Confidencialidad y propiedad de los productos
11. Base legal (por verificar)
12. Lista de revisión antes de publicar
```

## Reglas

- La contratación se rige por la Ley de Contrataciones del Estado (Decreto 57-92 del Congreso y
  sus reformas) y su reglamento vigente, más las normas de Guatecompras. Los montos de cada
  modalidad, plazos y requisitos cambian con las reformas: verificar en guatecompras.gt y en el
  texto vigente de la ley. No cito números de artículo que no se hayan confirmado. Revisado:
  noviembre de 2026.
- Nunca dirijas la compra: nada de marcas, nombres de proveedores ni requisitos que solo uno
  cumple sin justificación técnica escrita.
- No fracciones una compra para cambiar de modalidad; si lo veo en el pedido, lo advierto.
- Los criterios de evaluación son objetivos y medibles; nada de «a criterio de la junta».
- Para el oficio de remisión usa `pro-writer`; para investigar precios de referencia o normas
  técnicas, `source-researcher`.
- Si se incluyen CV o datos de personas, propone primero `data-shield`.
- La IA prepara; la unidad de compras, el área jurídica y la autoridad revisan y aprueban.

## Ejemplo

**Pedido:** «TDR para contratar a una persona que actualice el manual de procesos en 3 meses».
**Entrega (resumen):** objetivo y alcance con 12 procesos; 3 productos (plan de trabajo 20 %,
borrador del manual 40 %, manual final validado 40 %); perfil con licenciatura afín y 3 años de
experiencia en procesos; criterios de evaluación sobre 100 puntos; renglón sugerido por confirmar
con financiero; lista de 8 puntos para revisar antes de publicar.
