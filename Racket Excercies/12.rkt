;12. Hacer una función que reciba un vector de enteros e
;    indique si está ordenado ascendentemente.

(define (OrdenAscendente? Vect Pos)
  (if (>= Pos (- (vector-length Vect) 1))
      #t
      (if (> (vector-ref Vect Pos) (vector-ref Vect (+ Pos 1)) )
          #f
          (OrdenAscendente? Vect (+ Pos 1))
          )))

(define VectorDePrueba (vector 1 2 3 20 4 5 6 7 8 10))
(OrdenAscendente? VectorDePrueba 0)