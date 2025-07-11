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

# Conexión SSH
net_connect = ConnectHandler(**router)

# 1. Interfaces
interfaces_output = net_connect.send_command("show ip interface brief")

# Procesamos interfaces que están "up"
interfaces_lines = interfaces_output.splitlines()
interfaces_status = []
for line in interfaces_lines[1:]:
    cols = line.split()
    if len(cols) >= 6 and cols[4] == "up" and cols[5] == "up":
        interfaces_status.append(cols[0])

# 2. NTP status
ntp_output = net_connect.send_command("show ntp associations")
ntp_enabled = "ref clock" in ntp_output.lower() or "*" in ntp_output

# Generamos reporte
reporte = {
    "router": router["host"],
    "fecha": datetime.now().isoformat(),
    "interfaces_up": interfaces_status,
    "ntp_activo": ntp_enabled,
}

# Guardamos como archivo JSON
with open("reporte_validacion.json", "w") as f:
    json.dump(reporte, f, indent=4)

# Cierre conexión
net_connect.disconnect()

print("✅ Validación completada. Revisa el archivo reporte_validacion.json")
