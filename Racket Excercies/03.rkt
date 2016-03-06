;2. Hacer una función que reciba un entero N y devuelva
;   un vector de  tamaño N, con enteros leidos por teclado.
;3. Hacer lo mismo que en el punto anterior, pero generando
;   los datos aleatoriamente.
(display "Ingrese el tamaño del vector: ")
(define Vec(make-vector (read)))

(define (VecFill lenght i)
  (if (= lenght i)
      (display Vec)
      (begin
        (vector-set! Vec i (random 1000))
        (VecFill lenght (+ i 1))
        )
      )
  )

(VecFill (vector-length Vec) 0)