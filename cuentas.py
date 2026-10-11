class CuentaBancaria:
    def __init__(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0  # saldo privado, inicia en 0.0

    def _actualizar_saldo(self, delta):
        """Acceso controlado al saldo privado para las clases hijas."""
        self.__saldo += delta

    def depositar(self, monto):
        # Validación: el monto debe ser positivo (corregido en hotfix/validar-monto)
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0")
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"Cuenta {self.numero_cuenta} | Titular: {self.titular} | Saldo: {self.__saldo:.2f}"
