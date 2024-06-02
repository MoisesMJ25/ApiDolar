
DROP TABLE IF EXISTS moisesmarquinaj_coderhouse.api_dolar;

CREATE TABLE IF NOT EXISTS Api_dolar(
     casa VARCHAR(200),
     moneda VARCHAR(5),
     compra FLOAT(50),
     venta FLOAT(50),
     fecha DATETIME
)