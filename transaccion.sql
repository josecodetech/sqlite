BEGIN TRANSACTION;
INSERT INTO ventas (cantidad) VALUES (100);
UPDATE ventas SET cantidad = cantidad * 20 WHERE id = 4;
-- Decidir si confirmar o revertir
--COMMIT;
--ROLLBACK;
END TRANSACTION;