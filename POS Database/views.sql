-- View: "parcial-view1"

-- DROP VIEW "parcial-view1";


CREATE OR REPLACE VIEW "parcial-view1" AS 
 SELECT reserva.id_cliente,
    reserva.fecha_in
   FROM reserva;

ALTER TABLE "parcial-view1"
  OWNER TO postgres;
COMMENT ON VIEW "parcial-view1"
  IS 'CLIENTES QUE HAN USADO HABITACION Y RESTAURANTE SIMULTANEAMENTE';
 -----------------------------
-- View: "parcial-view2"

-- DROP VIEW "parcial-view2";

CREATE OR REPLACE VIEW "parcial-view2" AS 
 SELECT orden_cliente.id_cliente,
    orden_cliente.fecha
   FROM orden_cliente;

ALTER TABLE "parcial-view2"
  OWNER TO postgres;
-------------------------------
-- View: "parical-view3"

-- DROP VIEW "parical-view3";

CREATE OR REPLACE VIEW "parical-view3" AS 
 SELECT reserva.id_cliente,
    reserva.fecha_in
   FROM reserva
   JOIN orden_cliente ON orden_cliente.id_cliente = reserva.id_cliente AND orden_cliente.fecha = reserva.fecha_in;

ALTER TABLE "parical-view3"
  OWNER TO postgres;
-------------------------------
-- View: view1

-- DROP VIEW view1;

CREATE OR REPLACE VIEW view1 AS 
 SELECT persona.nombre,
    persona.apellido
   FROM persona
   JOIN cliente ON cliente.id_persona = persona.id_persona;

ALTER TABLE view1
  OWNER TO postgres;
COMMENT ON VIEW view1
  IS 'MUESTRA LOS NOMBRES DE LAS PERSONAS QUE SON CLIENTES';
--------------------------------
-- View: view2

-- DROP VIEW view2;

CREATE OR REPLACE VIEW view2 AS 
 SELECT producto.id_producto,
    producto.nombre
   FROM producto
  WHERE (producto.id_producto::text IN ( SELECT existencia.id_producto
           FROM existencia));

ALTER TABLE view2
  OWNER TO postgres;
COMMENT ON VIEW view2
  IS 'Muestra los productos con existencia';

--------------------------------

-- View: view3

-- DROP VIEW view3;

CREATE OR REPLACE VIEW view3 AS 
 SELECT cliente.id_cliente
   FROM cliente
  WHERE (cliente.id_cliente IN ( SELECT reserva.id_cliente
           FROM reserva
          WHERE reserva.id_habitacion::text = '103'::text));

ALTER TABLE view3
  OWNER TO postgres;
COMMENT ON VIEW view3
  IS 'ID DE CLIENTES QUE SE HOSPEDARON EN LA HABITACION 103 EN CUALQUIER FECHA';


  -------------------------------

  -- View: view4

-- DROP VIEW view4;

CREATE OR REPLACE VIEW view4 AS 
 SELECT persona.id_persona
   FROM persona
  WHERE (persona.id_persona IN ( SELECT cliente.id_persona
           FROM cliente
          WHERE (cliente.id_cliente IN ( SELECT cliente_1.id_cliente
                   FROM cliente cliente_1
                  WHERE (cliente_1.id_cliente IN ( SELECT reserva.id_cliente
                           FROM reserva
                          WHERE reserva.id_habitacion::text = '103'::text))))));

ALTER TABLE view4
  OWNER TO postgres;
COMMENT ON VIEW view4
  IS 'CEDULA DE CLIENTES QUE SE HOSPEDARON EN LA HABITACION 103 EN CULQUIER FECHA';

----------------------------
-- View: view5

-- DROP VIEW view5;

CREATE OR REPLACE VIEW view5 AS 
 SELECT persona.id_persona,
    persona.nombre,
    persona.apellido
   FROM persona
  WHERE (persona.id_persona IN ( SELECT persona_1.id_persona
           FROM persona persona_1
          WHERE (persona_1.id_persona IN ( SELECT cliente.id_persona
                   FROM cliente
                  WHERE (cliente.id_cliente IN ( SELECT cliente_1.id_cliente
                           FROM cliente cliente_1
                          WHERE (cliente_1.id_cliente IN ( SELECT reserva.id_cliente
                                   FROM reserva
                                  WHERE reserva.id_habitacion::text = '103'::text))))))));

ALTER TABLE view5
  OWNER TO postgres;
COMMENT ON VIEW view5
  IS 'HISTORICO DE CLIENTES (ID, NOMBRE, APELLIDO) QUE SE HOSPEDARON EN LA HABITACION 103
';

