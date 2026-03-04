🐜 De-Chill — Control de Gastos Hormiga

Aplicación web para registrar, visualizar y controlar los pequeños gastos del día a día que, sin darte cuenta, se acumulan y afectan tus finanzas personales.




👥 Roles de Usuario
RolDescripción🔓 InvitadoPuede explorar la app sin registrarse, acceso limitado👤 Usuario no registradoPuede ver la landing y registrarse✅ Usuario registradoAcceso completo a su panel de gastos🛡️ AdministradorGestión total de usuarios y datos de la plataforma

📋 Historias de Usuario

🔓 Invitado

HU-01 — Ver demo de la app

Como invitado, quiero poder ver una demostración de la app sin registrarme, para evaluar si me es útil antes de crear una cuenta.

Criterios de aceptación:

 El invitado puede acceder a una vista demo con datos de ejemplo
 Se muestra un banner invitando a registrarse
 No puede guardar ni modificar datos reales


HU-02 — Explorar categorías de gastos

Como invitado, quiero ver las categorías de gastos disponibles (café, transporte, snacks, etc.), para entender cómo funciona la clasificación de gastos hormiga.

Criterios de aceptación:

 Se listan las categorías predefinidas con íconos
 Se puede visualizar descripción de cada categoría
 No requiere inicio de sesión


👤 Usuario No Registrado

HU-03 — Registrarse en la app

Como usuario no registrado, quiero crear una cuenta con mi correo y contraseña, para comenzar a registrar mis gastos personales.

Criterios de aceptación:

 Formulario con nombre, correo y contraseña
 Validación de campos obligatorios
 Mensaje de confirmación al registrarse exitosamente
 Redirección al dashboard tras el registro


HU-04 — Iniciar sesión

Como usuario no registrado, quiero iniciar sesión con mi cuenta, para acceder a mi historial y panel de gastos.

Criterios de aceptación:

 Formulario de login con correo y contraseña
 Mensaje de error si las credenciales son incorrectas
 Opción "recordarme"
 Redirección al dashboard tras login exitoso


✅ Usuario Registrado

HU-05 — Registrar un gasto hormiga

Como usuario registrado, quiero registrar un gasto pequeño indicando monto, categoría y descripción, para llevar un control de mis gastos del día a día.

Criterios de aceptación:

 Formulario con monto, categoría, descripción y fecha
 El gasto se guarda y aparece en el historial inmediatamente
 Se puede registrar con la fecha actual por defecto
 Validación de monto positivo mayor a cero


HU-06 — Ver resumen de gastos del mes

Como usuario registrado, quiero ver un resumen visual de mis gastos del mes actual, para entender en qué estoy gastando más dinero.

Criterios de aceptación:

 Se muestra el total gastado en el mes
 Gráfico por categoría (torta o barras)
 Comparativa con el mes anterior si existe historial
 Resumen actualizado en tiempo real al agregar gastos


HU-07 — Filtrar gastos por categoría y fecha

Como usuario registrado, quiero filtrar mis gastos por categoría y rango de fechas, para analizar mis hábitos de consumo en períodos específicos.

Criterios de aceptación:

 Filtro por categoría (una o varias)
 Filtro por rango de fechas (desde / hasta)
 Resultados actualizados al aplicar filtros
 Opción de limpiar filtros


HU-08 — Editar o eliminar un gasto

Como usuario registrado, quiero poder editar o eliminar un gasto registrado, para corregir errores o eliminar entradas duplicadas.

Criterios de aceptación:

 Botón de editar abre el formulario con datos precargados
 Botón de eliminar pide confirmación antes de borrar
 El historial se actualiza tras la acción
 Solo el dueño del gasto puede modificarlo


HU-09 — Establecer un presupuesto mensual

Como usuario registrado, quiero definir un presupuesto mensual máximo para gastos hormiga, para recibir alertas cuando esté por superarlo.

Criterios de aceptación:

 Campo para ingresar presupuesto mensual
 Barra de progreso que muestra el porcentaje consumido
 Alerta visual cuando se supera el 80% del presupuesto
 Alerta cuando se supera el 100%


HU-10 — Ver historial completo de gastos

Como usuario registrado, quiero ver un listado completo de todos mis gastos registrados, para revisar mi historial financiero personal.

Criterios de aceptación:

 Lista paginada de gastos ordenada por fecha descendente
 Cada entrada muestra monto, categoría, descripción y fecha
 Buscador por descripción
 Opción de exportar a CSV


HU-11 — Cerrar sesión

Como usuario registrado, quiero poder cerrar mi sesión de forma segura, para proteger mi información en dispositivos compartidos.

Criterios de aceptación:

 Botón de cerrar sesión visible en el menú
 Se elimina el token de sesión
 Redirección a la página de inicio


🛡️ Administrador

HU-12 — Ver listado de usuarios registrados

Como administrador, quiero ver todos los usuarios registrados en la plataforma, para monitorear el uso de la aplicación.

Criterios de aceptación:

 Tabla con nombre, correo, fecha de registro y estado
 Buscador por nombre o correo
 Paginación del listado


HU-13 — Activar o desactivar usuarios

Como administrador, quiero poder activar o desactivar cuentas de usuarios, para gestionar el acceso a la plataforma.

Criterios de aceptación:

 Toggle de estado activo/inactivo por usuario
 El usuario desactivado no puede iniciar sesión
 Confirmación antes de cambiar el estado


HU-14 — Ver métricas globales de la plataforma

Como administrador, quiero ver estadísticas generales de uso (usuarios activos, gastos registrados, categorías más usadas), para evaluar el comportamiento de la plataforma.

Criterios de aceptación:

 Panel con KPIs: total usuarios, total gastos registrados, categoría más usada
 Gráfico de nuevos registros por mes
 Datos actualizados automáticamente


HU-15 — Gestionar categorías de gastos

Como administrador, quiero crear, editar y eliminar categorías de gastos hormiga, para mantener actualizada la clasificación disponible para los usuarios.

Criterios de aceptación:

 CRUD completo de categorías (nombre, ícono, descripción)
 No se puede eliminar una categoría con gastos asociados
 Los cambios se reflejan inmediatamente para todos los usuarios


