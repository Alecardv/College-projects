;16. Hacer el mismo ejercicio pero generando los números aleatoriamente.

(define (Make-Matrix FILAS COLUMNAS)
  (make-vector FILAS (make-vector COLUMNAS))
  )

(define (readfils) (begin (display "Numero de filas: ") (read)))
(define (readcols) (begin (display "Numero de columnas: ") (read)))

(define (Matriz)
  (Make-Matrix (readfils) (readcols)))

(define (randr)
  (random 1000))

(define (Fill-Matrix MATRIX i j rand)
  (if (>= i (vector-length MATRIX))
      MATRIX
      (if (>= j (vector-length (vector-ref MATRIX 0)))
          (Fill-Matrix MATRIX (+ i 1) 0 (randr))
          (begin
            (display "[")(display i)(display "]")(display "[")(display j)(display "]: ")
            (display rand)
            (vector-set! (vector-ref MATRIX i) j rand)
            (newline)
            (Fill-Matrix MATRIX i (+ j 1) (randr))
            )
          )
      )
  )

(Fill-Matrix (Matriz) 0 0 (randr))