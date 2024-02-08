CREATE TRIGGER registro_despues_de_insertar
AFTER INSERT ON ventas
BEGIN
	INSERT INTO registro_ventas (descripcion) VALUES ('Nueva venta agregada');
END;