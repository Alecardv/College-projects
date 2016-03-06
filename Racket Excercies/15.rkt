;15. Un vector es un arreglo unidimensional que permite manejar una lista
;    de datos del mismo tipo. Una matriz es un arreglo bidimensional que se
;    puede representar como un vector de vectores. Hacer una función que reciba
;    dos enteros N (filas) y M (columnas), lea por pantalla N x M enteros y los
;    guarde en la matriz. La función debe devolver la matriz (un vector de vectores
;    de tamaño N, donde cada vector tiene M enteros).


(define (Make-Matrix FILAS COLUMNAS)
  (make-vector FILAS (make-vector COLUMNAS))
  )

(define (readfils) (begin (display "Numero de filas: ") (read)))
(define (readcols) (begin (display "Numero de columnas: ") (read)))

(define (Matriz)
  (Make-Matrix (readfils) (readcols)))


(define (Fill-Matrix MATRIX i j)
  (if (>= i (vector-length MATRIX))
      MATRIX
      (if (>= j (vector-length (vector-ref MATRIX 0)))
          (Fill-Matrix MATRIX (+ i 1) 0)
          (begin
            (display "[")(display i)(display "]")(display "[")(display j)(display "]: ")
            (vector-set! (vector-ref MATRIX i) j (read))
            (newline)
            (Fill-Matrix MATRIX i (+ j 1))
            )
          )
      )
  )

(Fill-Matrix (Matriz) 0 0)