from cliente import Cliente

cliente = Cliente("Renan", 22)

cliente.insereEndereco("Avenida Cel Germano", 207, "Centro", "Socorro")
cliente.insereEndereco("Avenida XV de Agosto", 32, "Centro", "Socorro")

cliente.listaEndereco()
