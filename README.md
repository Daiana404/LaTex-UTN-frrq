# LaTex-UTN-frrq
Apuntes de materias y resúmenes de fórmulas específicas de la carrera Ingeniería Electromecánica

# Guía para trabajar en el repositorio

Este repositorio es de colaboración, por lo que cada miembro debe seguir una serie de pasos para hacer cambios correctamente.

## Flujo de trabajo

### 1. **Clonar el repositorio**


### 2. **Crear una nueva rama**

Para trabajar en nuevos archivos o hacer modificaciones, creá una nueva rama utilizando el formato: `nombre-DDMMAAAA-version`, y ubicate en la rama creada con `git checkout`.

Por ejemplo: 
```
git branch daiana-20022025-1
```
```
git checkout daiana-20022025-1
```
### 3. Realizar cambios

Hacé los cambios necesarios en los archivos correspondientes.

### 4. Verificar el estado de los cambios
Puedes ver qué archivos han sido modificados usando:

```
git status 
```
### 5. Agregar los cambios
Agregá todos los cambios con `git add .`, o en a archivos específicos con `git add [filename]`

```
git add .
```
### 6. Confirmar los cambios
Hacé un commit con un mensaje descriptivo que explique los cambios:
```
git commit -m "Descripción de los cambios realizados"
```

### 7. Actualizar tu rama con los últimos cambios

Antes de subir tus cambios, asegurate de que tu rama esté actualizada con los últimos cambios de la rama main:

```
git pull origin main
```
### 8. Subir los cambios al repositorio remoto

Una vez que tengas todos tus cambios listos, subí tu rama al repositorio remoto:

```
git push origin nombre-DDMMAAAA-version
```

### 9. Crear un Pull Request (PR)
Una vez que se trabajó y se hizo el push de un archivo, tenés que hacer el pull en GitHub.

1. Andá a GitHub y abrí el repositorio.
2. Vas a ver un botón que dice "Compare & pull request". Hacé clic ahí.
3. En el Pull Request, agregá una descripción de los cambios realizados.
4. Seleccioná la rama main como la rama base, y tu rama como la rama que querés fusionar.
5. Pedí la revisión de tus cambios antes de fusionar.

### 10. Borrar ramas
Una vez que tu Pull Request haya sido fusionado, podés eliminar la rama tanto local como remotamente.

Eliminar la rama localmente:
```
git branch -d nombre-DDMMAAAA-version
```
Eliminar la rama remotamente:
```
git push origin --delete nombre-DDMMAAAA-version
```

¡Listo! Así es como podés colaborar en este repositorio. Si tenés alguna duda, no dudes en preguntar.

<!-- 
# Agregar archivos
Algunas consideraciones a tener en cuenta
> En revisión de contenido...
### Materias
Crear una carpeta por cada materia que se requiera. Colocar el nombre completo de la materia, en minúsculas y separado por guiones medios. Por ejemplo: `máquinas-eléctricas`


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

Así como se crea una carpeta de Teoría, se deberá crear una carpeta llamada `Formulas`. En dicha carpeta, se creará el archivo respectivo al resumen de fórmulas. Ejemplo: `maq-ele-formulas` -->


