;1. Hacer una función que reciba un valor entero N y devuelva
;   un vector de tamaño N, donde cada posición contiene el valor -1.
(display "Ingrese el tamaño del vector: ")
(define Vec(make-vector (read)))

(define (VecFill lenght i)
  (if (= lenght i)
      (display Vec)
      (begin
        (vector-set! Vec i -1)
        (VecFill lenght (+ i 1))
        )
      )
  )

(VecFill (vector-length Vec) 0)