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


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, tasa_interes):
        super().__init__(numero_cuenta, titular)
        self.tasa_interes = tasa_interes  # porcentaje anual, ej: 4.5 para 4.5%

    def calcular_interes(self):
        """Interés anual = saldo * tasa / 100."""
        return self.consultar_saldo() * self.tasa_interes / 100

    def __str__(self):
        return (f"{super().__str__()} | Tasa: {self.tasa_interes}% "
                f"| Interés anual: {self.calcular_interes():.2f}")


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, limite_sobregiro):
        super().__init__(numero_cuenta, titular)
        self.limite_sobregiro = limite_sobregiro  # máximo que puede quedar negativo

    def retirar(self, monto):
        """Permite retirar hasta saldo + limite_sobregiro."""
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > self.consultar_saldo() + self.limite_sobregiro:
            raise ValueError("El retiro excede el límite de sobregiro")
        self._actualizar_saldo(-monto)

    def permite_sobregiro(self):
        """True si el saldo actual es negativo."""
        return self.consultar_saldo() < 0

    def __str__(self):
        return f"{super().__str__()} | Límite de sobregiro: {self.limite_sobregiro:.2f}"


# ----------------------- Instancias y operaciones de prueba -----------------------
base = CuentaBancaria("CB-001", "Oscar")
base.depositar(100)
print(base)

ahorros = CuentaAhorros("AH-100", "Lucia Perez", 4.5)
ahorros.depositar(1500)
print(ahorros)
ahorros.depositar(300)
ahorros.retirar(200)
print("Después de operar:", ahorros)
print("Interés anual:", ahorros.calcular_interes())

corriente = CuentaCorriente("CC-200", "Carlos Ruiz", 200)
corriente.depositar(400)
print(corriente)
corriente.retirar(500)
print("¿Está en sobregiro?", corriente.permite_sobregiro())
print(corriente)
try:
    corriente.retirar(500)
except ValueError as e:
    print("Error:", e)
try:
    ahorros.depositar(-50)
except ValueError as e:
    print("Error:", e)
