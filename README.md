# 🚀 Aprendiendo POO con Python

Este repositorio contiene una serie de ejercicios prácticos diseñados para dominar los pilares de la **Programación Orientada a Objetos (POO)** utilizando Python. Cada ejercicio está estructurado siguiendo una **arquitectura de capas** para asegurar la separación de responsabilidades entre la lógica de negocio y la interfaz de usuario.

## 📋 Tabla de Contenidos
* [Conceptos Aplicados](#-conceptos-aplicados)
* [Estructura del Proyecto](#-estructura-del-proyecto)
* [Ejercicios Incluidos](#-ejercicios-incluidos)
* [Cómo Ejecutar](#-cómo-ejecutar)

## 🧠 Conceptos Aplicados
A través de estos ejercicios se demuestran los siguientes principios:

* **Abstracción y Encapsulamiento:** Lógica "pura" que procesa datos sin interacción directa con la consola (sin `print` ni `input` en la capa de lógica).
* **Herencia:** Creación de jerarquías de clases utilizando `super()` para inicializar atributos base.
* **Polimorfismo:** Sobrescritura de métodos para adaptar comportamientos específicos por especie o tipo de objeto.
* **Agregación y Relaciones:** Gestión de objetos que contienen otros objetos, como una `Cita` que contiene una instancia de `Medico`.
* **Manejo de Colecciones:** Uso de listas y diccionarios para la persistencia de datos en memoria.

## 📂 Estructura del Proyecto
El repositorio sigue una organización modular profesional:

```text
/EJERCICIO_X
│
├── main.py                 # Punto de entrada del programa
├── logic/                  # Capa de Lógica (Cálculos y Clases)
│   ├── entidades.py        # Definición de clases y modelos
│   └── gestor_data.py      # Controladores y gestión de colecciones
└── view/                   # Capa de Vista (Interacción con usuario)
    └── consola.py          # Menús, entradas (input) y salidas (print)
```

## 📝 Ejercicios Incluidos
## 1. Convertidor Multiespecie
Calculadora de edad biológica para mascotas basada en años humanos.

Lógica: La conversión no es lineal; varía según la especie (perro o gato) y el tamaño del animal (Pequeño, Mediano o Grande).

## 2. Sistema IMC Pro (Gestión de Salud)
Sistema para centros médicos que registra pacientes y calcula su Índice de Masa Corporal (IMC).

Funcionalidad: Clasificación del estado nutricional (Bajo peso, Normal, Sobrepeso, Obesidad) y actualización dinámica de datos.

## 3. Gestión de Agenda Médica
Administración de citas clínicas mediante la interacción de las entidades Paciente, Médico y Cita.

Regla de Negocio: Validación estricta para que un paciente no supere las 3 citas programadas.

## 4. Motor de Blackjack "Las Vegas Edition"
Simulador de cartas que gestiona una baraja de 52 naipes con reglas dinámicas para el valor del As y las figuras.

## 5. Juego de Azar "¿Por qué siempre yo?"
Simulación digital de un juego de mesa que utiliza un tablero con 6 huecos y un sistema de "pozo" para la eliminación de fichas.

## 6. Prácticas de Combate (RPG)
Simulación de batalla entre clases de personajes utilizando Clases Abstractas.

Personajes: Guerrero, Mago y Arquero heredando de una clase base Jugador.

## 🚀 Cómo Ejecutar
Clona el repositorio:

Bash
```text
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
```
Navega a la carpeta del ejercicio deseado:

Bash
```text
cd EJERCICIO_X
```
Ejecuta el archivo principal:

Bash
```text
python main.py
```
Este repositorio fue desarrollado como parte del proceso de formación en Análisis y Desarrollo de Software (ADSO) - SENA.
