# Desafío Talana Kombat

## Introducción
Solución desarrollada en Python3 por el postulante Javier Valenzuela para el desafío "Talana Kombat".
Las instrucciones del problema resuelto en este repositorio son las que se encuentran en `resources/desafio_talana.pdf`

## Requisitos
1. python3+
2. pipenv 11.9.0 (Opcional)

## Instalación
### Clonar el repositorio
```
git clone ssh://github.com/tschirnhausen/desafio_talana
```

### Navegar hasta el directorio principal
```
cd desafio_talana
```

### Crear entorno virtual, activar e instalar dependencias
El proyecto puede ejecutarse directamente con `python3`, sin embargo, puede ejecutarse en un entorno virtual con pipenv:
```
pipenv shell
pipev activate
pipenv install
```

## Uso general
### Para simular una batalla, ejecute el archivo main.py
```
pipenv run python main.py
```
Para simular otra batalla, se puede reemplazar el valor de la variable `battle_sequence` en el archivo `main.py`

## Salida de ejemplo
```
{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":{"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
Tony avanza y da una patada
Arnaldor usa un Remuyuken
Tony usa un Taladoken
Arnaldor se mueve
Tony se agacha
Arnaldor usa un Remuyuken
¡La batalla termina! El ganador es Arnaldor y aún le quedan 2 puntos de vida

{"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]},"player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P","k"]}}
Tony se mueve y da una patada
Arnaldor se mueve y da un puñetazo
Tony usa un Taladoken
Arnaldor se mueve y da una patada
Tony se mueve y da una patada
Arnaldor se mueve y da una patada
Tony usa un Taladoken
¡La batalla termina! El ganador es Tony y aún le quedan 3 puntos de vida

{"player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]},"player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}}
Tony usa un Taladoken
Arnaldor da un puñetazo
Tony se agacha
Arnaldor se mueve
Tony no hace nada!
Arnaldor se mueve y da un puñetazo
Tony no hace nada!
Arnaldor se mueve y da una patada
Tony no hace nada!
Arnaldor da una patada
Tony no hace nada!
Arnaldor usa un Remuyuken
¡La batalla termina! El ganador es Arnaldor y aún le quedan 3 puntos de vida
```

## Preguntas
### Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. 
Si no se hizo push. Se puede hacer un restore del commit
```
git reset HEAD~
```

Si ya se hizo push, en cambio, se debe buscar el hash del último commit válido y dejar los cambios en estado `unstaged`.
```
git log origin/<branch>
git push -f origin <hash_commit>:<branch>
```

En ambos casos, se puede luego hacer el `add` correspondiente y hacer el push del commit corregido.

```
git add <filename>
git commit -m "<scope>: <commit>"
git push origin <branch>
```

### Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?
Gitflow

### ¿Cuál ha sido la situación más compleja que has tenido con esto?
Trabajando en equipo, nos dimos cuenta de que a veces se "perdía" código. Pensamos que se trataba de algún error de configuración de git en algún dispositivo del equipo. Al analizar los commits y hacerle un seguimiento a un archivo crítico, se encontró que un miembro del equipo, dada su poca experiencia con git, copiaba archivos manualmente de versiones anteriores y los utilizaba para solucionar conflictos. 

### ¿Qué experiencia has tenido con los microservicios? 
He consumido y participado en diseño y programación de microservicios. Consumiendo diversas API externas e internas, para utilizar servicios de terceros o comunicar distintos sistemas de la plataforma, y en cuanto a implementación, para el procesamiento de pagos y liberaciones de saldo.

### ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué? 
AWS Elastic Beanstalk. Ya que simplifica el proceso de puesta en marcha de los proyectos y también su mantenimiento, al orquestar todo mediante este servicio.
