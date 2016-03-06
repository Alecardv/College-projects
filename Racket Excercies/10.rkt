;10. Hacer una función que reciba un vector de enteros y
;    devuelva la posición del mayor valor de los datos existentes.

(define 

(define (Mayor Vect Pos result)
  (if (>= Pos (vector-length Vect))
      (display result)
      (if (> result (vector-ref Vect Pos) )
          (Mayor Vect (+ Pos 1) result)
          (Mayor Vect (+ Pos 1) (vector-ref Vect Pos))
          )))

(define VectorDePrueba (vector 100 100 12 1 3 44 56 2 3 4 100))
(Mayor VectorDePrueba 0 (vector-ref VectorDePrueba 0))