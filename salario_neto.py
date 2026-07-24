print("Salario neto")

salario_bruto = float(input("Ingresa el salario bruto: "))
impuestos = float(input("Ingresa el porcentaje de impuestos: "))
deducciones = float(input("Ingresa las deducciones: "))

impuesto = salario_bruto * impuestos / 100

salario_neto = salario_bruto - impuesto - deducciones

print("El salario neto es:", salario_neto)