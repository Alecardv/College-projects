z/*------------------------ PERSONA ------------------------*/
-- 4 tables
CREATE TABLE persona(
	id_persona	numeric(15), --PK CEDULA
	nombre		varchar(30),
	apellido	varchar(30),
	telefono	varchar(15),
	email		varchar(50)
	); --FNBC

CREATE TABLE cliente(
	id_cliente integer, --PK
	id_persona numeric(15) --FK CEDULA
	); --FNBC

CREATE TABLE cocinero(
	id_cocinero			integer, --PK
	id_persona			numeric(15), --KF CEDULA
	fecha_vinculacion	date,
	salario				integer
	); --FNBC

CREATE TABLE mesero(
	id_mesero			integer, --PK
	id_persona			numeric(15), --FK CEDULA
	fecha_vinculacion	date,
	salario				integer
	); --FNBC

/*------------------------ HOTEL ------------------------*/
-- 5 tablas
CREATE TABLE hotel(
	id_hotel			integer, --PK
	telefono			varchar(15),
	direccion			varchar(30),
	num_habitaciones	integer,	--numero de habitaciones
	categoria			varchar (10)
	); --¿? categorias

CREATE TABLE tipo(
	id_tipo		integer, --PK
	nombre		varchar(30),
	descripcion	varchar(200),
	costo		integer	--costo basico por 24horas
	); --FNBC

CREATE TABLE habitacion(
	id_habitacion	varchar(5), --PK
	id_hotel		integer, --FK
	id_tipo			integer, --FK
	id_estado		integer  --FK
	); --FNBC

CREATE TABLE reserva(
	id_reserva		integer, --PK
	id_cliente		integer, --FK
	id_habitacion	varchar(5), --FK
	fecha_in		date,
	fecha_out		date,
	fecha_reserva	date,
	no_personas		integer
	); --FNBC

CREATE TABLE cancelacion(
	id_cancelacion	integer, --PK
	id_reserva		integer, --FK
	recargo			integer
	); --FNBC

/*------------------------ FACTURACION ------------------------*/
-- 1 tabla
CREATE TABLE factura(
	id_factura 	integer, --PK
	id_cliente 	integer, --FK
	fecha 		date,
	total 		integer
	); --3FN

CREATE TABLE detalle_factura_restaurante(
	id_factura 			integer, --FK
	id_orden_cliente 	integer --FK
	); --3FN

CREATE TABLE detalle_factura_hotel(
	id_factura	integer, --FK
	id_reserva	integer --FK
	); --3FN

/*------------------------ BODEGA ------------------------*/
-- 9 tablas
CREATE TABLE bodega(
 	id_bodega integer, --PK
 	direccion varchar(30),
 	capacidad integer --CAPACIDAD EN ESTANTES
	); --FBNC

CREATE TABLE estante(
 	id_estante	integer, --PK
 	id_bodega	integer, --FK
 	ubicacion	varchar(10),
 	num_cajones	varchar(30)
	); --FNBC

CREATE TABLE cajon(
	id_cajon	integer, --PK
	id_estante	integer, --FK
	capacidad	integer
	); --FNBC

CREATE TABLE producto(
	id_producto	varchar(15), --PK
	nombre		varchar(30),
	descripcion	varchar(200)
	); --FNBC

CREATE TABLE existencia(
 	id_existencia	integer, --PK
 	id_cajon		integer, --FK
 	id_producto		varchar(15), --FK
 	cantidad		integer
	); --FBNC

CREATE TABLE proveedor(
 	id_proveedor	integer, --PK nit
 	nombre			varchar(40),
 	direccion		varchar(30),
 	telefono		varchar(15)
 	); --FNBC

--Trigger: Actualiza existencia.
CREATE TABLE ingreso(
 	id_ingreso		integer, --PK
 	id_proveedor	integer, --FK
 	fecha			date
	); --FNBC

CREATE TABLE detalle_ingreso(
	id_ingreso	integer, --FK
	id_producto	varchar(15),
	cantidad	integer
	); --FNBC

--Trigger: Actualiza existencia.
CREATE TABLE salida(
 	id_salida	integer, --PK
	id_producto	varchar(15), --FK
 	cantidad	integer,
 	fecha		date
	); --FNBC

CREATE TABLE pedido(
 	id_pedido		integer, --PK
 	id_proveedor	integer, --FK
 	fecha			date
	); --FNBC

CREATE TABLE detalle_pedido(
	id_pedido	integer, --FK
	id_producto	varchar(15), --FK
	cantidad	integer
	); --FNBC
/*------------------------ RESTAURANTE ------------------------*/
-- 6 tablas
CREATE TABLE restaurante(
	id_restaurante	integer, --PK
	id_hotel		integer, --FK
	nombre			varchar(20),
	telefono		varchar(15),
	capacidad		integer, --en personas
	num_mesas		integer
	); --FNBC

CREATE TABLE mesa(
 	id_mesa		varchar(4), --PK
 	id_estado 	integer, --FK
 	zona		varchar(15)
	); --FNBC

CREATE TABLE estado(
	id_estado	integer, --PK
	descripcion	varchar(10)
	); --FNBC

CREATE TABLE menu(
 	id_menu		integer, --PK
 	descripcion	varchar(300)
	); --FNBC

CREATE TABLE producto_terminado(
 	id_producto_terminado	varchar(5), --PK
 	id_menu					integer, 	--FK
 	nombre					varchar(20),
 	precio					integer,
 	categoria				varchar(30)
 	); --FNBC

CREATE TABLE orden_cliente(
 	id_orden_cliente	integer, --PK
 	id_mesa				varchar(4), --FK
 	id_cliente			integer, --FK Cedula
 	estado				varchar(30),
 	detalles			varchar(200),
 	fecha_ 				date
 	); --FNBC

CREATE TABLE detalle_orden_cliente(
	id_orden_cliente		integer, --FK
	id_producto_terminado	varchar(5)
	); --FNBC

CREATE TABLE control_cocina(
 	id_control_cocina	integer, --PK
 	id_orden_cliente	integer, --FK
 	id_cocinero			integer, --FK
 	fecha				date
	); --¿SOBRA ESTA RELACION?
