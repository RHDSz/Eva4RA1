🚀 **Automatización de Redes con Ansible y Python**  
Flujo integral para configurar, validar y respaldar routers Cisco usando tecnologías de automatización.  

---

## 📌 **Conceptos Claves**  

### 🔗 **Tecnologías Utilizadas**  
- **Ansible**: Automatización de configuración mediante playbooks YAML  
- **Netmiko**: Biblioteca Python para interacción SSH con dispositivos de red  
- **Bash**: Orquestación del flujo completo mediante scripting  

### ⚙ **Módulos Principales**  
1. **Configuración Automatizada** (Ansible):  
   - Establecimiento de hostname y dominio  
   - Configuración de NTP y VLANs  
   - Gestión de interfaces físicas y lógicas  

2. **Validación de Estado** (Python + Netmiko):  
   - Verificación de interfaces operativas  
   - Chequeo de sincronización NTP  
   - Generación de reportes JSON  

3. **Gestión de Backups**:  
   - Captura de running-config  
   - Almacenamiento con timestamp en formato JSON  

---

## 📋 **Estructura del Proyecto**  
```
.
├── backup_config.py          # Respaldo de configuración  
├── validar_router.py         # Validación de estado de red  
├── router_7200v4.yml         # Playbook de configuración  
├── inventory.ini             # Definición de equipos y credenciales  
├── automatizar.sh            # Script de ejecución principal  
└── reporte_validacion.json   # Ejemplo de output de validación  
```

---

## 🛠 **Requisitos Técnicos**  
| Componente | Versión |  
|------------|---------|  
| Ansible    | 2.9+    |  
| Python     | 3.8+    |  
| Netmiko    | 4.1.2+  |  

Instalación de dependencias:  
```bash
pip install netmiko paramiko ansible-core
```

---

## 🚀 **Implementación**  

### 1. Configuración Inicial  
```bash
git clone [repo_url]
cd [project_dir]
```

### 2. Personalización  
Editar:  
- `inventory.ini` (Credenciales/IP del router)  
- `router_7200v4.yml` (Ajustes de VLANs/NTP)  

### 3. Ejecución Completa  
```bash
chmod +x automatizar.sh
./automatizar.sh
```

---

## 📄 **Outputs Generados**  
| Archivo | Contenido | Formato |  
|---------|-----------|---------|  
| `backup_config_*.json` | Configuración completa | JSON |  
| `reporte_validacion.json` | Estado de interfaces y NTP | JSON |  

---

## 🔍 **Flujo Técnico Detallado**  

### ▶ **Fase Ansible**  
- Configuración atómica mediante tasks:  
  ```yaml
  - name: Configurar NTP
    cli_command:
      command: |
        configure terminal
        ntp server {{ item }}
        end
    loop: "{{ ntp_servers }}"
  ```

### ▶ **Fase Netmiko**  
- Conexión SSH programática:  
  ```python
  net_connect = ConnectHandler(
      device_type="cisco_ios",
      host="192.168.56.107",
      username="fcer",
      password="qwerty12345"
  )
  ```

### ▶ **Fase Bash**  
- Orquestación secuencial:  
  ```bash
  # Fase 1: Ansible
  ansible-playbook -i inventory.ini router_7200v4.yml
  
  # Fase 2: Validación
  python3 validar_router.py
  ```

---

## ⚠ **Consideraciones**  
1. Verificar conectividad SSH previa a la ejecución  
2. Ajustar timeouts para equipos legacy (ver `inventory.ini`)  
3. Los archivos JSON generados sobrescriben versiones previas  

---

📜 **Licencia**: MIT  
🔧 **Mantenido por**: [Tu Nombre]  

--- 

**¡Configuración profesional lista para producción!** 💻🔌# README - Automatización de Configuración de Router Cisco  

🚀 **Automatización de Redes con Ansible y Python**  
Flujo integral para configurar, validar y respaldar routers Cisco usando tecnologías de automatización.  

---

## 📌 **Conceptos Claves**  

### 🔗 **Tecnologías Utilizadas**  
- **Ansible**: Automatización de configuración mediante playbooks YAML  
- **Netmiko**: Biblioteca Python para interacción SSH con dispositivos de red  
- **Bash**: Orquestación del flujo completo mediante scripting  

### ⚙ **Módulos Principales**  
1. **Configuración Automatizada** (Ansible):  
   - Establecimiento de hostname y dominio  
   - Configuración de NTP y VLANs  
   - Gestión de interfaces físicas y lógicas  

2. **Validación de Estado** (Python + Netmiko):  
   - Verificación de interfaces operativas  
   - Chequeo de sincronización NTP  
   - Generación de reportes JSON  

3. **Gestión de Backups**:  
   - Captura de running-config  
   - Almacenamiento con timestamp en formato JSON  

---

## 📋 **Estructura del Proyecto**  
```
.
├── backup_config.py          # Respaldo de configuración  
├── validar_router.py         # Validación de estado de red  
├── router_7200v4.yml         # Playbook de configuración  
├── inventory.ini             # Definición de equipos y credenciales  
├── automatizar.sh            # Script de ejecución principal  
└── reporte_validacion.json   # Ejemplo de output de validación  
```

---

## 🛠 **Requisitos Técnicos**  
| Componente | Versión |  
|------------|---------|  
| Ansible    | 2.9+    |  
| Python     | 3.8+    |  
| Netmiko    | 4.1.2+  |  

Instalación de dependencias:  
```bash
pip install netmiko paramiko ansible-core
```

---

## 🚀 **Implementación**  

### 1. Configuración Inicial  
```bash
git clone [repo_url]
cd [project_dir]
```

### 2. Personalización  
Editar:  
- `inventory.ini` (Credenciales/IP del router)  
- `router_7200v4.yml` (Ajustes de VLANs/NTP)  

### 3. Ejecución Completa  
```bash
chmod +x automatizar.sh
./automatizar.sh
```

---

## 📄 **Outputs Generados**  
| Archivo | Contenido | Formato |  
|---------|-----------|---------|  
| `backup_config_*.json` | Configuración completa | JSON |  
| `reporte_validacion.json` | Estado de interfaces y NTP | JSON |  

---

## 🔍 **Flujo Técnico Detallado**  

### ▶ **Fase Ansible**  
- Configuración atómica mediante tasks:  
  ```yaml
  - name: Configurar NTP
    cli_command:
      command: |
        configure terminal
        ntp server {{ item }}
        end
    loop: "{{ ntp_servers }}"
  ```

### ▶ **Fase Netmiko**  
- Conexión SSH programática:  
  ```python
  net_connect = ConnectHandler(
      device_type="cisco_ios",
      host="192.168.56.107",
      username="fcer",
      password="qwerty12345"
  )
  ```

### ▶ **Fase Bash**  
- Orquestación secuencial:  
  ```bash
  # Fase 1: Ansible
  ansible-playbook -i inventory.ini router_7200v4.yml
  
  # Fase 2: Validación
  python3 validar_router.py
  ```

---

## ⚠ **Consideraciones**  
1. Verificar conectividad SSH previa a la ejecución  
2. Ajustar timeouts para equipos legacy (ver `inventory.ini`)  
3. Los archivos JSON generados sobrescriben versiones previas  

---

📜 **Licencia**: MIT  
🔧 **Mantenido por**: [Fabian Cabezas - Esteban Rohdis]  

--- 

**¡Configuración profesional lista para producción!** 💻🔌
