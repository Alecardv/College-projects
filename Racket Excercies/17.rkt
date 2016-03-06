;17. Hacer una función que reciba una matriz y muestre
;    los datos por pantalla con N filas de M enteros.

(define MatrizPrueba (make-vector 8 (make-vector 5 "F")))

(define MatrizPrueba1 (vector (vector 5 6 7) (vector 8 9 0) ))

(define (DisplayMatrix MATRIX i j)
  (if (= j (vector-length (vector-ref MATRIX 0)))
      (newline)
      (if (= i (vector-length MATRIX))
          (begin
            (newline)
            (DisplayMatrix MATRIX 0 (+ j 1))
           )
          (begin
            (display (vector-ref (vector-ref MATRIX i) j))(display ", ")
            (DisplayMatrix MATRIX (+ i 1) j)
           )
          )
      )
  )

(DisplayMatrix MatrizPrueba1 0 0)