# Desafío Talana Kombat

## Introducción
Solución desarrollara en Python3 por el postulante Javier Valenzuela para el desafío "Talana Kombat".
Las instrucciones del problema resuelto en este repositorio son las que se encuentran en `resources/desafio_talana.pdf`

## Requerimientos
1. Sistema operativo Unix
2. pipenv 11.9.0
3. python3+

## Instalación
### Clonar el repositorio
```
git clone ssh://github.com/tschirnhausen/desafio_talana
```

### Navegar hasta el directorio principal
```
cd desafio_talana
```

### Activar entorno virtual e instalar dependencias
```
pipenv shell
pipenv install
pipev activate // Para activar el entorno
```

## Uso general
### Para simular una batalla, ejecute el archivo main.py
```
pipenv run python main.py
```

## Salida de ejemplo
```
Tony D K
Tony avanza y da una patada
Arnaldor SA K
Arnaldor usa un Remuyuken
Tony DSD P
Tony usa un Taladoken
Arnaldor SA 
Arnaldor se mueve
Tony S 
Tony se agacha
Arnaldor SA K
Arnaldor usa un Remuyuken
La batalla se termina. Tony ha perdido sus puntos de vida
```

## Preguntas
### Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. 
Si no se hizo push. Se puede hacer un restore del commit
```
git restore --staged
```

Si ya se hizo push, en cambio, se puede revertir el commit con su identificador único
```
git revert [commit hash]
```

En ambos casos, se puede luego hacer el `add` correspondiente y hacer el push del commit corregido.

### Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?
Gitflow

### ¿Cuál ha sido la situación más compleja que has tenido con esto?
Trabajando en equipo, nos dimos cuenta de que a veces se "perdía" código. Pensamos que se trataba de algún error de configuración de git en algún dispositivo del equipo. Al analizar los commits y hacerle un seguimiento a un archivo crítico, se encontró que un miembro del equipo, dada su poca experiencia con git, copiaba archivos manualmente de versiones anteriores y los utilizaba para solucionar conflictos. 

### ¿Qué experiencia has tenido con los microservicios? 
He consumido y participado en diseño y programación de microservicios. Consumiendo diversas API externas e internas, para utilizar servicios de terceros o comunicar distintos sistemas de la plataforma, y en cuanto a implementación, para el procesamiento de pagos y liberaciones de saldo.

### ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué? 
AWS Elastic Beanstalk. Ya que simplifica el proceso de puesta en marcha de los proyectos y también su mantenimiento, al orquestar todo mediante este servicio.
