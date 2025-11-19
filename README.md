# Rama Backups – Club Deportivo

Esta rama contiene todo lo necesario para trabajar con las copias de seguridad y la generación de datos de ejemplo del club deportivo en Django.

---

## Estado del Proyecto

La rama **Backups** incluye:

- Seeders para poblar las tablas del proyecto.
- Comando personalizado para crear datos aleatorios con Faker.
- Backup de datos exportado en formato fixture **UTF-8** (compatible y listo para importar en Django).

---

## Flujo de Trabajo y Requisitos

| Paso                        | Descripción                                                                       |
| --------------------------- | --------------------------------------------------------------------------------- |
| Rellenar tablas con seeders | Uso de scripts y utilidades para poblar los modelos del club con datos iniciales. |
| Comando Faker personalizado | Genera **10 objetos aleatorios** por cada modelo usando Faker.                    |
| Backup con fixture en UTF-8 | Exporta todos los datos a un archivo JSON en formato UTF-8 puro.                  |

---

## Exportación de Fixture UTF-8

Dado que los **fixtures** estándar no funcionaban correctamente en tu entorno UFT-16 LE, se creó un proceso alternativo para generar el backup en **UTF-8** puro. Esto evita problemas de codificación.

---

### Código utilizado para la exportación

Guarda este script como `club/export_club.py`:
