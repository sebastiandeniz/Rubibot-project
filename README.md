# Rubibot
# 🤖 Robot Solucionador de Cubo de Rubik

Este proyecto consiste en el diseño, construcción y programación de un robot autónomo capaz de resolver un cubo de Rubik 3x3 mediante visión por computador y control mecánico preciso.

## 📌 Objetivos del Proyecto

- Capturar y analizar el estado del cubo usando una cámara fija.
- Detectar colores con OpenCV y reconstruir el estado completo del cubo.
- Resolver el cubo utilizando el algoritmo de Kociemba.
- Controlar motores para ejecutar los movimientos del cubo.
- Documentar el proyecto como recurso educativo.

## 🛠️ Tecnologías y Herramientas

- **Lenguaje:** Python
- **Visión por Computador:** OpenCV
- **Control y lógica:** ESP32
- **Diseño mecánico:** Piezas impresas en 3D (Onshape)
- **Control de motores:**  Motores paso a paso NEMA17

## 📸 Funcionamiento

1. **Captura de imagen**: Se usan dos tomas con una cámara fija para observar todas las caras del cubo.
2. **Reconocimiento de colores**: Segmentación y clasificación de los colores de cada sticker.
3. **Reconstrucción del estado**: Se reconstruyen las 6 caras del cubo.
4. **Resolución**: Se genera una secuencia de movimientos con el algoritmo de Kociemba.
5. **Ejecución física**: Los motores realizan los giros necesarios para resolver el cubo.

## 🧠 Algoritmo utilizado

El proyecto utiliza el algoritmo de Kociemba, ampliamente reconocido por su eficiencia para resolver el cubo en pocos movimientos:

🔗 [https://kociemba.org/cube.htm](https://kociemba.org/cube.htm)
