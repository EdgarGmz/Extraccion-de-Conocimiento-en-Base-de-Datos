# Instalación de dependencias

Pasos para configurar el entorno y ejecutar los ejercicios del repositorio.

## 0. Instalación de Python 3

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Se recomienda la versión **3.10 o superior**.

### **Windows**
1.  Descarga el instalador oficial: [Python for Windows](https://www.python.org/downloads/windows/).
2.  Al ejecutar el instalador, **es fundamental** marcar la casilla **"Add Python to PATH"**.
3.  Sigue las instrucciones del instalador (Recomendado: "Install Now").

### **Linux (Ubuntu/Debian)**
Python suele venir preinstalado. Si no lo tienes, ejecuta:
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```
Para otras distribuciones, utiliza el gestor de paquetes correspondiente (pacman, dnf, etc.).

### **macOS**
1.  Descarga el instalador oficial: [Python for macOS](https://www.python.org/downloads/macos/).
2.  O utiliza [Homebrew](https://brew.sh/): `brew install python`

---

## 1. Configuración del Entorno Virtual (Global)

Para evitar duplicidad, utilizamos un único entorno virtual en la raíz del proyecto que contiene todas las dependencias necesarias para el primer y segundo parcial.

```bash
# Crear el entorno virtual en la raíz
python3 -m venv .venv

# Activar el entorno
source .venv/bin/activate
```

## 2. Instalación de Dependencias

Instala todas las librerías necesarias (pandas, numpy, scikit-learn, matplotlib, seaborn, etc.) desde el archivo de requerimientos unificado:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Ejecución de Ejercicios

Una vez activado el entorno, puedes ejecutar cualquier ejercicio desde la raíz:

```bash
# Ejemplo del Segundo Parcial
python3 segundo-parcial/ejercicio-03.py

# Ejemplo del Primer Parcial
python3 primer-parcial/ej1.py
```

## Notas Adicionales
- **Visualización**: Algunos scripts generan archivos `.png` en su respectiva carpeta.
- **Limpieza**: Si deseas salir del entorno virtual, simplemente ejecuta `deactivate`.
- **Estructura**: El archivo `requirements.txt` en la raíz es el principal. Los archivos en las subcarpetas se mantienen como referencia de lo solicitado originalmente.
