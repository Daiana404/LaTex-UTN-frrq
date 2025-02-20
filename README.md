# LaTex-UTN-frrq
Apuntes de materias y resúmenes de fórmulas específicas de la carrera Ingeniería Electromecánica.
### Pasos a seguir

Si es la primera vez, se debe clonar el repositorio con `git clone https://github.com/Daiana404/LaTex-UTN-frrq.git`


Si ya tenés la carpeta, solo tenes que actualizar con `git pull`


Si no se muestran las actualizaciones tenés que ir a otra rama aleatoria `git checkout random-branch` y volver `git checkout main`


### Siempre
Crear una nueva rama `git branch nombre-DDMMAAAA-version` y después `git push origin nombre-DDMMAAAA-version`

### Revisar en GitHub
Una vez que se trabajó y se hizo el push de un archivo, se tiene que realizar el pull en GitHub. Ir a *Pull requests* y después *compare and merge* si está todo ok.

### Eliminar ramas viejas
No elimines hasta que sepamos qué estamos haciendo

# Archivos
Algunas consideraciones a tener en cuenta.

> Estoy trabajando en algunas modificaciones, pero de momento sigan las instrucciones que están a continuación.

### Materias
Crear una carpeta por cada materia que se requiera. Colocar el nombre completo de la materia, en minúsculas y separado por guiones medios: `máquinas-eléctricas`

#### Teoría

Dentro de la carpeta de la materia, se deberá crear una carpeta de `Teoría`. En dicha carpeta, se deberá crear el archivo *main* del resumen de la materia con el siguiente nombre como ejemplo: `maq-ele-resumen`.
> Si están de acuerdo, nombremos a los archivos con las primeras tres letras de cada palabra. Con dos palabras bastaría. Lo hice con todos menos con mecánica de los fluidos... aunque se podría poner algo como `mec-flu`

Además, se deben crear carpetas que correspondan a las unidades. En cada unidad, crear uno o más archivos respectivos a cada tema. Por ejemplo:
`máquinas-eléctricas/Teoría/U1/transformadores.tex`

Así debería verse el archivo *main*, pueden copiar y pegar: 

```
\documentclass[11pt,a4paper]{article}
\usepackage{{../../paquete}}
\usepackage{{../../estilos}}
\graphicspath{{../Figuras}}
%BEGIN_FOLD
\newcommand{\nombreMateria}{Nombre De La Materia}
%Si escriben las palabras principales con la primera letra en mayúscula, mucho mejor...
\newcommand{\materia}{\textit{\nombreMateria}}
%END_FOLD
\fancyhead[L]{\textsc{\nombreMateria}}

\begin{document}
	\input{../../portada}
	\pagestyle{fancy}
  %A continuación, se agregan los \include{} necesarios
	\include{./U1/...}
\end{document}
```

#### Resumen de Formulas

Así como se crea una carpeta de Teoría, se deberá crear una carpeta llamada `Formulas`. En dicha carpeta, se creará el archivo respectivo al resumen de fórmulas. Ejemplo: `maq-ele-formulas`


# Sintáxis de GitHub
Les recomiendo que lean la [Guía de Sintáxis de GitHub](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) para que quede todo más bonito, referenciado y ordenado.
