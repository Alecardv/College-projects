;4. Hacer una función reciba un vector de enteros y un
;   numero X, busque el número X en el vector y devuelva 
;   la posición donde se encuentra la primera vez ese número
;   en el vector. En caso de no estar debe devolver -1.

(define (Encontrar Vect X Pos)
  (if (>= Pos (vector-length Vect))
      (display -1)
      (begin
        (if (= (vector-ref Vect Pos) X)
            (display Pos) ;Imprime Asumiendo que la primera posicion es 0
            (Encontrar Vect X (+ Pos 1))
            )
        )
      )
  )


(define VectorDePrueba (vector 12 1 3 44 56 2 3 4))

(Encontrar VectorDePrueba 12 0)