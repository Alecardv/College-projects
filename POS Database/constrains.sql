-- CONSTRAINT PERSONAS:
ALTER TABLE persona ADD PRIMARY KEY (id_persona);
ALTER TABLE persona ADD CHECK (id_persona > 0);
ALTER TABLE persona ALTER COLUMN nombre SET NOT NULL;
ALTER TABLE persona ALTER COLUMN apellido SET NOT NULL;

ALTER TABLE cliente ADD PRIMARY KEY (id_cliente);
ALTER TABLE cliente ADD FOREIGN KEY (id_persona) REFERENCES persona(id_persona);
ALTER TABLE cliente ADD	CHECK (id_cliente > 0);

ALTER TABLE cocinero ADD PRIMARY KEY (id_cocinero);
ALTER TABLE cocinero ADD FOREIGN KEY (id_persona) REFERENCES persona(id_persona);
ALTER TABLE cocinero ADD CHECK (id_cocinero > 0);

ALTER TABLE mesero ADD PRIMARY KEY (id_mesero);
ALTER TABLE mesero ADD FOREIGN KEY (id_persona) REFERENCES persona(id_persona);
ALTER TABLE mesero ADD CHECK (id_mesero > 0);
-- FIN PERSONAS.


-- CONSTRAINT HOTEL:
ALTER TABLE estado ADD PRIMARY KEY (id_estado);
ALTER TABLE estado ALTER COLUMN descripcion SET NOT NULL;

ALTER TABLE hotel ADD PRIMARY KEY (id_hotel);
ALTER TABLE hotel ADD CHECK (id_hotel > 0);
ALTER TABLE hotel ALTER COLUMN num_habitaciones SET NOT NULL;

ALTER TABLE tipo ADD PRIMARY KEY (id_tipo);
ALTER TABLE tipo ADD CHECK (id_tipo > 0);
ALTER TABLE tipo ALTER COLUMN nombre SET NOT NULL;
ALTER TABLE tipo ALTER COLUMN costo SET NOT NULL;

ALTER TABLE habitacion ADD PRIMARY KEY (id_habitacion);
ALTER TABLE habitacion ADD FOREIGN KEY (id_hotel) REFERENCES hotel(id_hotel);
ALTER TABLE habitacion ADD FOREIGN KEY (id_tipo) REFERENCES tipo(id_tipo);
ALTER TABLE habitacion ADD FOREIGN KEY (id_estado) REFERENCES estado(id_estado);
ALTER TABLE habitacion ADD CHECK (id_habitacion != ' ');

ALTER TABLE reserva ADD PRIMARY KEY (id_reserva);
ALTER TABLE reserva ADD CHECK (id_reserva > 0);
ALTER TABLE reserva ADD CHECK (no_personas > 0 and no_personas < 10);
ALTER TABLE reserva ADD FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);
ALTER TABLE reserva ADD FOREIGN KEY (id_habitacion) REFERENCES habitacion(id_habitacion);
ALTER TABLE reserva ALTER COLUMN fecha_in SET NOT NULL;
ALTER TABLE reserva ALTER COLUMN fecha_out SET NOT NULL;
ALTER TABLE reserva ALTER COLUMN fecha_reserva SET NOT NULL;

ALTER TABLE cancelacion ADD PRIMARY KEY (id_cancelacion);
ALTER TABLE cancelacion ADD CHECK (id_cancelacion > 0);
ALTER TABLE cancelacion ADD FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva);
-- FIN HOTEL.


-- CONSTRAINT FACTURACION:
ALTER TABLE factura ADD PRIMARY KEY (id_factura);
ALTER TABLE factura ADD FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);
ALTER TABLE factura ADD CHECK (id_factura > 0);
ALTER TABLE factura ALTER COLUMN fecha SET NOT NULL;
ALTER TABLE factura ALTER COLUMN total SET NOT NULL;

ALTER TABLE detalle_factura_hotel ADD FOREIGN KEY (id_factura) REFERENCES factura(id_factura);
ALTER TABLE detalle_factura_hotel ADD FOREIGN KEY (id_reserva) REFERENCES reserva(id_reserva);
-- FIN FACTURACION.


-- CONSTRAINT BODEGA:
ALTER TABLE bodega ADD PRIMARY KEY (id_bodega);
ALTER TABLE bodega ADD CHECK (id_bodega > 0);
ALTER TABLE bodega ALTER COLUMN capacidad SET NOT NULL;

ALTER TABLE estante ADD PRIMARY KEY (id_estante);
ALTER TABLE estante ADD FOREIGN KEY (id_bodega) REFERENCES bodega(id_bodega);
ALTER TABLE estante ADD CHECK (id_estante > 0);
ALTER TABLE estante ALTER COLUMN ubicacion SET NOT NULL;
ALTER TABLE estante ALTER COLUMN num_cajones SET NOT NULL;

ALTER TABLE cajon ADD PRIMARY KEY (id_cajon);
ALTER TABLE cajon ADD FOREIGN KEY (id_estante) REFERENCES estante(id_estante);
ALTER TABLE cajon ADD CHECK (id_cajon > 0);
ALTER TABLE cajon ALTER COLUMN capacidad SET NOT NULL;

ALTER TABLE producto ADD PRIMARY KEY (id_producto);
ALTER TABLE producto ADD CHECK (id_producto != '');

ALTER TABLE existencia ADD PRIMARY KEY (id_existencia);
ALTER TABLE existencia ADD FOREIGN KEY (id_cajon) REFERENCES cajon(id_cajon);
ALTER TABLE existencia ADD FOREIGN KEY (id_producto) REFERENCES producto(id_producto);
ALTER TABLE existencia ADD CHECK (id_existencia > 0);
ALTER TABLE existencia ALTER COLUMN cantidad SET NOT NULL;

ALTER TABLE proveedor ADD PRIMARY KEY (id_proveedor);
ALTER TABLE proveedor ADD CHECK (id_proveedor > 0);
ALTER TABLE proveedor ALTER COLUMN nombre SET NOT NULL;

ALTER TABLE ingreso ADD PRIMARY KEY (id_ingreso);
ALTER TABLE ingreso ADD FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor);
ALTER TABLE ingreso ADD CHECK (id_ingreso > 0);
ALTER TABLE ingreso ALTER COLUMN fecha SET NOT NULL;

ALTER TABLE detalle_ingreso ADD FOREIGN KEY(id_ingreso) REFERENCES ingreso(id_ingreso);
ALTER TABLE detalle_ingreso ADD FOREIGN KEY(id_producto) REFERENCES producto(id_producto);
ALTER TABLE detalle_ingreso ALTER COLUMN cantidad SET NOT NULL;

ALTER TABLE salida ADD PRIMARY KEY (id_salida);
ALTER TABLE salida ADD CHECK (id_salida > 0);
ALTER TABLE salida ALTER COLUMN fecha SET NOT NULL;
ALTER TABLE salida ALTER COLUMN cantidad SET NOT NULL;

ALTER TABLE pedido ADD PRIMARY KEY (id_pedido);
ALTER TABLE pedido ADD FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor);
ALTER TABLE pedido ADD CHECK (id_pedido > 0);
ALTER TABLE pedido ALTER COLUMN fecha SET NOT NULL;

ALTER TABLE detalle_pedido ADD FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido);
ALTER TABLE detalle_pedido ADD FOREIGN KEY(id_producto) REFERENCES producto(id_producto);
ALTER TABLE detalle_pedido ALTER COLUMN cantidad SET NOT NULL;
-- FIN BODEGA.


-- CONSTRAINT RESTAURANTE:
ALTER TABLE restaurante ADD PRIMARY KEY (id_restaurante);
ALTER TABLE restaurante ADD CHECK (id_restaurante > 0);
ALTER TABLE restaurante ADD FOREIGN KEY (id_hotel) REFERENCES hotel(id_hotel);

ALTER TABLE mesa ADD PRIMARY KEY (id_mesa);
ALTER TABLE mesa ADD CHECK (id_mesa != '');
ALTER TABLE mesa ADD FOREIGN KEY (id_estado) REFERENCES estado(id_estado);

ALTER TABLE menu ADD PRIMARY KEY (id_menu);
ALTER TABLE menu ADD CHECK (id_menu > 0);

ALTER TABLE producto_terminado ADD PRIMARY KEY (id_producto_terminado);
ALTER TABLE producto_terminado ADD CHECK (id_producto_terminado != '');
ALTER TABLE producto_terminado ADD FOREIGN KEY (id_menu) REFERENCES menu(id_menu);
ALTER TABLE producto_terminado ALTER COLUMN precio SET NOT NULL;
ALTER TABLE producto_terminado ALTER COLUMN nombre SET NOT NULL;

ALTER TABLE orden_cliente ADD PRIMARY KEY (id_orden_cliente);
ALTER TABLE orden_cliente ADD CHECK (id_orden_cliente > 0);
ALTER TABLE orden_cliente ADD FOREIGN KEY (id_mesa) REFERENCES mesa(id_mesa);
ALTER TABLE orden_cliente ADD FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente);

ALTER TABLE detalle_orden_cliente ADD FOREIGN KEY (id_orden_cliente) REFERENCES orden_cliente(id_orden_cliente);
ALTER TABLE detalle_orden_cliente ADD FOREIGN KEY (id_producto_terminado) REFERENCES producto_terminado(id_producto_terminado);

ALTER TABLE control_cocina ADD PRIMARY KEY (id_control_cocina);
ALTER TABLE control_cocina ADD CHECK (id_control_cocina > 0);
ALTER TABLE control_cocina ADD FOREIGN KEY (id_orden_cliente) REFERENCES orden_cliente(id_orden_cliente);
ALTER TABLE control_cocina ADD FOREIGN KEY (id_cocinero) REFERENCES cocinero(id_cocinero);

ALTER TABLE detalle_factura_restaurante ADD FOREIGN KEY (id_factura) REFERENCES factura(id_factura);
ALTER TABLE detalle_factura_restaurante ADD FOREIGN KEY (id_orden_cliente) REFERENCES orden_cliente(id_orden_cliente);
-- FIN RESTAURANTE.
