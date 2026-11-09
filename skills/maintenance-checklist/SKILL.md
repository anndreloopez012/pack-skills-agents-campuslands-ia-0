---
name: maintenance-checklist
description: "Arma el checklist de mantenimiento de un edificio por nivel y por sistema (sanitarios, eléctrico, iluminación, climatización, BMS, bombeo, ascensores, contra incendios, fachada), con periodicidad y responsable. Pídela así: «haz el checklist mensual del edificio», «qué reviso en el cuarto de bombas»."
---

# Checklist de mantenimiento

Convierte un edificio en una lista de revisión por nivel y por sistema, lista para imprimir o llevar
en el celular. Para administradores de edificios y gerentes de infraestructura.

## Cuándo usarla

- «Haz el checklist de mantenimiento preventivo de mi edificio de 6 niveles».
- «Qué debo revisar cada semana en sanitarios y cada mes en el cuarto eléctrico».
- «Pásame esta lista de equipos a un formato de ronda por nivel».

## Qué necesito de ti

- Niveles del edificio (sótanos, primer nivel, niveles tipo, azotea) y uso (oficinas, vivienda, comercio).
- Lista de equipos que conozcas: tableros, planta eléctrica, bombas, cisterna, ascensores, equipos de
  aire, BMS, bombas contra incendio, extintores.
- Frecuencia que necesitas: diaria, semanal, mensual, trimestral o anual.
- Si falta algo, haz como máximo 3 preguntas cortas y sigue con supuestos marcados como «Supuesto:».

## Cómo trabajo

1. Hago el inventario por nivel: qué sistema hay en cada nivel (por ejemplo, sótano 1: cisterna,
   bombas, planta eléctrica; azotea: condensadoras, tanque elevado, cuarto de máquinas de ascensor).
2. Para cada sistema uso la lista base de abajo y la ajusto a tus equipos.
3. Separo lo que revisa el personal propio (inspección visual, lecturas) de lo que hace el proveedor
   especializado (pruebas, ajustes, cambio de piezas).
4. Asigno periodicidad, criterio de aceptación («qué es estar bien») y acción si falla.
5. Te entrego el checklist por nivel y una hoja de hallazgos para anotar lo que no pasó.

Lista base por sistema:

- **Sanitarios:** fugas en inodoros, lavamanos y fluxómetros; presión; drenajes lentos; olores;
  dispensadores de jabón y papel; rejillas de piso.
- **Eléctrico:** tableros cerrados y rotulados; temperatura anormal o olor a quemado; breakers
  disparados; planta eléctrica (nivel de combustible, batería, prueba en vacío); transferencia
  automática; tierras físicas (medición anual por técnico).
- **Iluminación:** luminarias apagadas o parpadeando por nivel; luces de emergencia y rótulos de
  salida con prueba de batería; sensores de presencia y horarios.
- **HVAC (climatización):** filtros, drenajes de condensado, temperatura de salida, ruidos y
  vibración, limpieza de serpentines (proveedor), extractores de baños y parqueos.
- **BMS (sistema de gestión del edificio):** alarmas activas, sensores sin lectura, horarios
  programados, respaldo de configuración.
- **Bombeo e hidrosanitario:** nivel de cisterna y tanque elevado, presión del hidroneumático,
  alternancia de bombas, fugas en válvulas, flotes, tratamiento o cloración del agua, trampas de grasa.
- **Ascensores:** nivelación en cada parada, puertas y sensores, iluminación y botón de emergencia de
  cabina, intercomunicador, cuarto de máquinas limpio; mantenimiento mensual del proveedor autorizado.
- **Contra incendios:** extintores (presión, sello, fecha de recarga, acceso libre), gabinetes y
  mangueras, detectores de humo, panel de alarma sin fallas, bomba contra incendio (arranque de
  prueba), rutas de evacuación despejadas, puertas cortafuego cerradas.
- **Fachada e impermeabilización:** fisuras, sellos de ventanería, manchas de humedad en losas y
  muros, bajadas pluviales y canales limpios antes del invierno, estado de la membrana en azotea.

## Lo que te entrego

```
CHECKLIST DE MANTENIMIENTO - <Edificio> - <Frecuencia> - Ronda del: __/__/____
Revisó: ______________  Hora inicio: ____  Hora fin: ____

NIVEL: Sótano 1
| Sistema | Equipo / punto | Qué revisar | Criterio OK | OK / Falla | Observación | Acción |
|---|---|---|---|---|---|---|
| Bombeo | Cisterna | Nivel | Arriba de 60 % | | | Avisar a proveedor |

HOJA DE HALLAZGOS
| N.º | Nivel | Sistema | Hallazgo | Prioridad (Alta/Media/Baja) | Responsable | Fecha límite | Estado |

PROGRAMA ANUAL (resumen)
| Sistema | Diario | Semanal | Mensual | Trimestral | Anual | Proveedor |
```

## Reglas

- Lo eléctrico energizado, ascensores, planta y bombas contra incendio los interviene solo personal
  calificado o el proveedor; el checklist propio es inspección visual y lectura.
- Prioridad Alta para todo lo que afecte la vida (incendio, evacuación, electricidad expuesta,
  ascensor con falla de puerta o freno): se atiende el mismo día.
- La periodicidad que propongo es referencial; manda el manual del fabricante y el contrato del
  proveedor.
- Antes del invierno (mayo) agrego revisión de azotea, canales y bajadas pluviales.
- Para llevar las rondas en hoja de cálculo, apóyate en `spreadsheet-helper`; para los contratos de
  cada sistema, en `supplier-contracts`.
- Sin emojis. La IA prepara; la persona decide qué se contrata o repara.

## Ejemplo

**Pedido:** «Edificio de oficinas de 5 niveles y 2 sótanos, dame el checklist semanal».
**Entrega (resumen):** checklist por nivel (sótanos con cisterna, bombas, planta y parqueo; niveles
1 a 5 con sanitarios, iluminación, extintores y aire; azotea con condensadoras, tanque y cuarto de
ascensores), hoja de hallazgos y programa anual con 9 sistemas y su proveedor.
