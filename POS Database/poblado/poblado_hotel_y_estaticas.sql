-- Poblado de hotel y otras tablas estaticas*.

INSERT INTO hotel VALUES (0001, 3207651940, 'Cra 10 bis # 11a29', 200, '5 stars');

INSERT INTO restaurante VALUES (1, 0001, 'Sazon extremo', '3008473345', 300, 100);

INSERT INTO proveedor VALUES (001, 'ColComidas', 'Cra 2 # 11-29', '3159871640');
INSERT INTO proveedor VALUES (002, 'SuperInter', 'Cra 3 # 34-56', '3259814526');
INSERT INTO proveedor VALUES (003, 'AlmacExito', 'Cra 4 # 23-67', '3141259823');
INSERT INTO proveedor VALUES (004, 'CheCheCome', 'Cra 5 # 99-01', '3104569827');

INSERT INTO menu VALUES (01, 'Este es el mejor menu');

INSERT INTO tipo VALUES(01, 'Individual',
	'Para una sola persona',
	40000);
INSERT INTO tipo VALUES (02, 'Doble uso indivual',
	'Habitacion doble para uso de una sola persona',
	50000);
INSERT INTO tipo VALUES (03, 'Doble',
	'Acomodacion doble, dos camas o una matrimonial',
	70000);
INSERT INTO tipo VALUES (04, 'Triple',
	'Acomodacion triple, 3 camas o 2 mas una supletoria',
	90000);
INSERT INTO tipo VALUES (05, 'Junior Suites',
	'Habitacion doble, baño y salon',
	120000);
INSERT INTO tipo VALUES (06, 'Suite presidencial',
	'La mejor de todas las Suites, para personas distinguidas ofrece todos los servicios siendo estas las mas lujosas',
	180000);
INSERT INTO tipo VALUES (07, 'Suite nupcial',
	'Pensada para recien casados que queiren disfrutar de una luna de miel con privacidad y todas las comodidades necesarias',
	150000);

INSERT INTO estado VALUES (00, 'DISPONIBLE');
INSERT INTO estado VALUES (01, 'RESERVADO');
