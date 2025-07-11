#!/bin/bash

echo "🔧 Fase 1: Configuración del router con Ansible"
ansible-playbook -i inventory.ini router_7200v4.yml
echo "✅ Fase 1 completada"
echo "-----------------------------------------------"

echo "🧪 Fase 2: Validación de red con Netmiko"
source venv-netmiko/bin/activate
python3 validar_router.py
echo "✅ Fase 2 completada"
echo "-----------------------------------------------"

echo "💾 Fase 3: Backup de configuración"
python3 backup_config.py
echo "✅ Fase 3 completada"
deactivate
echo "-----------------------------------------------"

echo "🚀 Automatización finalizada con éxito"
