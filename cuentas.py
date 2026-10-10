# HOTFIX: depositar() valida que el monto sea positivo (monto > 0), si no lanza ValueError
class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = saldo

    def depositar(self, monto: float):
        if monto > 0:
            self._saldo += monto
        else:
            raise ValueError("El monto a depositar debe ser mayor a 0")

    def retirar(self, monto: float):
        if monto > 0 and self._saldo >= monto:
            self._saldo -= monto
        else:
            raise ValueError("Monto inválido o saldo insuficiente")

    def consultar_saldo(self) -> float:
        return self._saldo

    def __str__(self) -> str:
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: ${self._saldo:.2f}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0.0, tasa_interes: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo)
        self.tasa_interes = tasa_interes

    def calcular_interes(self) -> float:
        return (self._saldo * self.tasa_interes) / 100

    def __str__(self) -> str:
        return super().__str__() + f" | Tasa: {self.tasa_interes}% | Interés Anual: ${self.calcular_interes():.2f}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, saldo: float = 0.0, limite_sobregiro: float = 0.0):
        super().__init__(numero_cuenta, titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto: float):
        # Permite retirar hasta saldo + limite_sobregiro
        if monto > 0 and (self._saldo + self.limite_sobregiro) >= monto:
            self._saldo -= monto
        else:
            raise ValueError("Excede el límite de sobregiro o monto inválido")

    def permite_sobregiro(self) -> bool:
        return self._saldo < 0

    def __str__(self) -> str:
        return super().__str__() + f" | Sobregiro Máx: ${self.limite_sobregiro:.2f}"


# Instancias y pruebas requeridas al final del archivo
if __name__ == "__main__":
    ahorros = CuentaAhorros("AH-100", "Lucia Perez", 1500.0, 4.5)
    corriente = CuentaCorriente("CC-200", "Carlos Ruiz", 400.0, 200.0)

    print(ahorros)
    ahorros.depositar(300)
    print("Después del depósito en ahorros:", ahorros)

    print("\n" + str(corriente))
    corriente.retirar(500)  # Entra en sobregiro permitido
    print("¿Está en sobregiro?", corriente.permite_sobregiro())
    print(corriente)




# Instancia de la clase base (prueba)
cuenta_base = CuentaBancaria("BASE-001", "Oscar")
cuenta_base.depositar(100)
print(cuenta_base)
