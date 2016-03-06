;7. Hacer una función que reciba un vector de enteros
;   y un número X, la función debe borrar el número si lo
;   encuentra y debe hacer SHIFT-LEFT (mover a la izquierda)
;   todos los elementos siguientes y dejando el valor -1 en la última posición.

(define (ShiftLeft Vect Pos fill)
  (if (>= Pos (vector-length Vect))
      (display "Err")
      (if (= (- (vector-length Vect) 1) Pos)
          (begin
            (vector-set! Vect Pos fill)
            (display Vect)
            )
          (begin
            (vector-set! Vect Pos (vector-ref Vect (+ Pos 1) ))
            (ShiftLeft Vect (+ Pos 1) fill)
            ) ) ) )

(define (Borrar-shleft Vect X Pos)
  (if (>= Pos (vector-length Vect))
      (display -1)
      (begin
        (if (= (vector-ref Vect Pos) X)
            (ShiftLeft Vect Pos -1)
            (Borrar-shleft Vect X (+ Pos 1))
            )
        )
      )
  )
 
(define VectorDePrueba (vector 12 1 3 44 56 2 3 4))
(Borrar-shleft VectorDePrueba 3 0)
