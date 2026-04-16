
 Un restaurante nos contrato para diseñar y desarrollar un programa que permita facturar rapidamente a los comensales

 opciones para desarrollar:
 1. Crear productos
 datos a almacenar:
 codigo, nombre, valor unitario e iva
 2. crear mesas
 datos a almacenar:
 codigo, nombre y puestos.
 3. Crear clientes:
 datos a almacenar:
 identificacion, nombre, telefono, email.

 4. facturacion:
 * se debe solicitar el codigo de la mesa a atender
 * debe solicitar el cliente, se debe añadir a traves de su identificacion
 * colocar fecha automaticamente
 * se inicia la factura con mesa y cliente
 * el usuario añade productos por codigo
 * registrar la cantidad del producto agregado
 * se puede agregar varios productos ingresados por el comensal (cliente)
 * se debe preguntar si desea agregar un producto
 * cuando diga que no se genera la factura
 * se calcula el subtotal
 * se calcula el total
 * la factura se muestra y se pregunta si se quiere guardar y se guarda en formato txt
 * los datos a mostrar en las facturas son: fecha, mesa, los datos del cliente, y todos los datos que aparece en la imagen
 * la factura cierra con el total a pagar


5. Reporte de ventas
* permite que el usuario obtenga el reporte de ventas asi como dice en la imagen
* preguntar la fecha del reporte
* se pregunta si se quiere imprimir el reporte y guardarlo en csv
* compartir el codigo con amigos los miembros del equipo

*****subir al git *****

archivo principal de ejecucion en py
archivos secundarios del proyecto
archivos txt json y csv


****** correcciones


Separar las funciones por archivos
guardas los productos en csv
datos persistentes





