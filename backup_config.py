from netmiko import ConnectHandler
import json
from datetime import datetime

# Datos del router
router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.1",
    "username": "FCER",
    "password": "qwerty12345",
}

# Conexión
net_connect = ConnectHandler(**router)

# Obtener running-config
running_config = net_connect.send_command("show running-config")

# Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Armar el backup como diccionario
backup_data = {
    "router": router["host"],
    "fecha_hora": timestamp,
    "running_config": running_config
}

# Guardar a archivo JSON
backup_filename = f"backup_config_{timestamp}.json"
with open(backup_filename, "w") as f:
    json.dump(backup_data, f, indent=4)

# Cerrar conexión
net_connect.disconnect()

print(f"✅ Backup guardado en {backup_filename}")
