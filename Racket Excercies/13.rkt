;13. Hacer una función que reciba un vector de enteros y lo
;    ordene ascendentemente.

(define (seek-replace Vect value pos)
  (if (>= pos (vector-length Vect))
      (display "Err")
      (if (= (vector-ref Vect pos) value)
          (vector-set! Vect pos -1)
          (seek-replace Vect value (+ pos 1))
          )))

(define (Menor Vect Pos result)
  (if (= result -1)
      (if (not (= (vector-ref Vect Pos) -1))
          (Menor Vect 0 (vector-ref Vect Pos))
          (Menor Vect (+ Pos 1) result)
          )
      (if (>= Pos (vector-length Vect))
          (begin
            (seek-replace Vect result 0)
            result
            )
          (if (= (vector-ref Vect Pos) -1)
              (Menor Vect (+ Pos 1) result)
              (if (< result (vector-ref Vect Pos) )
                  (Menor Vect (+ Pos 1) result)
                  (Menor Vect (+ Pos 1) (vector-ref Vect Pos)) )
              )
          )
      ))

(define (OrdenarA Vect Pos Aux)
  (if (>= Pos (vector-length Vect))
      (display Aux)
      (begin
        (vector-set! Aux Pos (Menor Vect 0 (vector-ref Vect 0)))
        (OrdenarA Vect (+ Pos 1) Aux)
        )
      )
  )

(define VectorDePrueba (vector 12 1 3 44 56 100 2 3 4 1 5))
(OrdenarA VectorDePrueba 0 (make-vector (vector-length VectorDePrueba)))