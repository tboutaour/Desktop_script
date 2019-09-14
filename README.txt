Pequeño script para limpiar mensualmente el escritorio y meterlo en una carpeta a parte.

Desktop_script.py contiene el código python para realizar esta funcionalidad.

Para ejecutarlo mensualmente se puede usar crontab.

crontab -e

Para el último dia del mes añadir lo siguiente en el fichero.
5 13 28-31 * * comando.
