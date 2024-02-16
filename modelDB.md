Entidades 📊:
Instrument 🎻:
PK: _id
comment 📝
version 🔄
file_name 📂
instrument 🎸
measurement 📏
date 📅
time ⌚
temperature_C 🌡️
battery_voltage 🔋
averages 🧮
integration ⏳
dark_mode 🌚
foreoptic 🔍
radiometric_calibration 🌐
units 📐
wavelength_range 🌈
latitude 🌐
longitude 🌐
altitude ⛰️
gps_time 🕰️
satellites 🛰️
calibrated_reference_correction_file 🗂️
channels 📺
columns5 📊
data 📄
Capture 📷:
PK: _id
FK: instrument_id (referencia a Instrument)
num_subdivisions 🔄
num_measurements_sublevel1 📏
num_measurements_sublevel2 📏
num_measurements_sublevel3 📏
num_atypical_measurements ❗
atypical_measurement_observation 📝
AgronomicData 🌱:
PK: _id
FK: instrument_id (referencia a Instrument)
variable_name 📚
variable_type 📊
allowed_limits ⚖️
value 💡
observation 📝
Relaciones 🤝:
Instrument (1 - M) Capture 📷
Instrument (1 - M) AgronomicData 🌱
Lógica de Negocio 🚀:
Instrument 🎻:
Crear un Nuevo Instrumento: Registrar un nuevo instrumento con todos sus detalles.
Consultar Instrumentos: Obtener la lista de todos los instrumentos existentes.
Consultar Instrumento por ID: Buscar un instrumento específico por su identificador único (_id).
Actualizar Instrumento: Modificar los detalles de un instrumento existente.
Eliminar Instrumento: Eliminar un instrumento específico.
Capture 📷:
Registrar Captura: Asociar mediciones específicas a un instrumento mediante la creación de capturas.
Consultar Capturas: Obtener la lista de todas las capturas asociadas a un instrumento.
Consultar Captura por ID: Buscar una captura específica por su identificador único (_id).
Actualizar Captura: Modificar detalles de una captura existente.
Eliminar Captura: Eliminar una captura específica.
AgronomicData 🌱:
Registrar Datos Agronómicos: Asociar datos agronómicos a un instrumento mediante la creación de registros en AgronomicData.
Consultar Datos Agronómicos: Obtener la lista de todos los registros de datos agronómicos asociados a un instrumento.
Consultar Datos Agronómicos por ID: Buscar un registro de datos agronómicos específico por su identificador único (_id).
Actualizar Datos Agronómicos: Modificar detalles de un registro de datos agronómicos existente.
Eliminar Datos Agronómicos: Eliminar un registro de datos agronómicos específico.
Consideraciones Adicionales 🤔:
Las operaciones de actualización y eliminación deben manejar adecuadamente la integridad referencial para mantener la consistencia de la base de datos.
La información presentada se centra en las operaciones principales; sin embargo, se pueden agregar detalles según las necesidades específicas del sistema y la aplicación.
