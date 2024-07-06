# Clase base Servidor
class Servidor:
    def __init__(self, nombre, direccion_ip):
        self._nombre = nombre  # Atributo encapsulado
        self._direccion_ip = direccion_ip  # Atributo encapsulado

    # Método para obtener el nombre (getter)
    def get_nombre(self):
        return self._nombre

    # Método para obtener la dirección IP (getter)
    def get_direccion_ip(self):
        return self._direccion_ip

    # Método para establecer el nombre (setter)
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Método para establecer la dirección IP (setter)
    def set_direccion_ip(self, direccion_ip):
        self._direccion_ip = direccion_ip

    # Método común a todos los servidores
    def iniciar_servicio(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")


# Clase derivada ServidorWindows
class ServidorWindows(Servidor):
    def __init__(self, nombre, direccion_ip, version_windows):
        super().__init__(nombre, direccion_ip)
        self.version_windows = version_windows  # Atributo específico de ServidorWindows

    # Sobrescribir método iniciar_servicio (polimorfismo)
    def iniciar_servicio(self):
        return f"Iniciando servicio en el servidor {self.version_windows}"

    # Método específico de ServidorWindows
    def aplicar_actualizaciones(self):
        return f"Aplicando actualizaciones en el servidor {self.version_windows}.\n"


# Clase derivada ServidorLinux
class ServidorLinux(Servidor):
    def __init__(self, nombre, direccion_ip, distribucion_linux):
        super().__init__(nombre, direccion_ip)
        self.distribucion_linux = distribucion_linux  # Atributo específico de ServidorLinux

    # Sobrescribir método iniciar_servicio (polimorfismo)
    def iniciar_servicio(self):
        return f"Iniciando servicio en el servidor Linux {self.distribucion_linux}"

    # Método específico de ServidorLinux
    def instalar_paquete(self, paquete):
        return f"Instalando paquete {paquete} en el servidor Linux {self.distribucion_linux}."


# Crear instancias y demostrar la funcionalidad

# Instancia de ServidorWindows
mi_servidor_windows = ServidorWindows("Servidor Exchange", "192.168.201.1", "Windows Server 2019")
print(
    f"Nombre: {mi_servidor_windows.get_nombre()}, Dirección IP: {mi_servidor_windows.get_direccion_ip()}, Versión: {mi_servidor_windows.version_windows}")
print(mi_servidor_windows.iniciar_servicio())
print(mi_servidor_windows.aplicar_actualizaciones())

# Instancia de ServidorLinux
mi_servidor_linux = ServidorLinux("Servidor 3DS", "192.168.201.2", "Ubuntu 20.04")
print(
    f"Nombre: {mi_servidor_linux.get_nombre()}, Dirección IP: {mi_servidor_linux.get_direccion_ip()}, Distribución: {mi_servidor_linux.distribucion_linux}")
print(mi_servidor_linux.iniciar_servicio())
print(mi_servidor_linux.instalar_paquete("nginx"))
