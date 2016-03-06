;14. Hacer una función que lea por teclado N nombres de personas, los guarde en un vector y los muestre después por pantalla.

(define (Copy Origen Destino Pos)
  (if (>= Pos (vector-length Origen))
      Destino
      (begin
        (vector-set! Destino Pos (vector-ref Origen Pos))
        (Copy Origen Destino (+ Pos 1))
        )
      )
  )

(define (Leer Vect Pos Value)
  (if (equal? Value 1)
      Vect
      (begin
        (vector-set! Vect Pos Value)
        (Leer (Copy Vect (make-vector (+ (vector-length Vect) 1)) 0) (+ Pos 1) (read))
        )
      )
  )

(display "Para terminar de ingresar datos, ingrese 1")
(display (Leer (make-vector 1) 0 (read)))

