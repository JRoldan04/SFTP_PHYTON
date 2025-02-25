# ELIMINAR ARCHIVOS 0 BYTE EN EXPORTSIMP

import paramiko

# Configuración SFTP
sftp_host = "mtu01-sftp-prod.ohrc.oracleindustry.com"
sftp_user = "SFTP_COL"
sftp_password = "#SFdXzvkrbAkv8"  # ⚠️ Usa variables de entorno en producción
sftp_dir = "/SFTP_COL/EXPORTSIMP/DEMOCRATIZACION"

# Conexión SFTP
transport = paramiko.Transport((sftp_host, 22))
transport.connect(username=sftp_user, password=sftp_password)
sftp = paramiko.SFTPClient.from_transport(transport)

def listar_archivos_0_bytes(ruta_base):
    """ Recorre todas las subcarpetas y muestra archivos de 0 bytes """
    try:
        for item in sftp.listdir_attr(ruta_base):
            ruta_completa = f"{ruta_base}/{item.filename}"
            if item.st_mode & 0o40000:  # Es un directorio
                listar_archivos_0_bytes(ruta_completa)
            elif item.st_size == 0:  # Es un archivo de 0 bytes
                print(f"Archivo vacío: {ruta_completa}")
                sftp.remove(ruta_completa)
                print(f"Archivo eliminado 0 bytes: {ruta_completa}")
    except Exception as e:
        print(f"Error en {ruta_base}: {e}")

# Ejecutar función
listar_archivos_0_bytes(sftp_dir)

# ELIMINAR ARCHVIOS O BYTE EN EXPORTINV

import paramiko

# Configuración SFTP
sftp_host = "mtu01-sftp-prod.ohrc.oracleindustry.com"
sftp_user = "SFTP_COL"
sftp_password = "#SFdXzvkrbAkv8"  # ⚠️ Usa variables de entorno en producción
sftp_dir = "/SFTP_COL/EXPORTINV/DEMOCRATIZACION"

# Conexión SFTP
transport = paramiko.Transport((sftp_host, 22))
transport.connect(username=sftp_user, password=sftp_password)
sftp = paramiko.SFTPClient.from_transport(transport)

def listar_archivos_0_bytes(ruta_base):
    """ Recorre todas las subcarpetas y muestra archivos de 0 bytes """
    try:
        for item in sftp.listdir_attr(ruta_base):
            ruta_completa = f"{ruta_base}/{item.filename}"
            if item.st_mode & 0o40000:  # Es un directorio
                listar_archivos_0_bytes(ruta_completa)
            elif item.st_size == 0:  # Es un archivo de 0 bytes
                print(f"Archivo vacío: {ruta_completa}")
                sftp.remove(ruta_completa)
                print(f"Archivo eliminado 0 bytes: {ruta_completa}")
    except Exception as e:
        print(f"Error en {ruta_base}: {e}")

# Ejecutar función
listar_archivos_0_bytes(sftp_dir)
