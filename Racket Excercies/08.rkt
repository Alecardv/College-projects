;8. Hacer una función que reciba un vector, y
;   devuelva una copia en otro vector.

(define (CopyVector Origen Destino Pos)
  (if (>= Pos (vector-length Origen))
      (display Destino)
      (begin
        (vector-set! Destino Pos (vector-ref Origen Pos))
        (CopyVector Origen Destino (+ Pos 1))
        )
      )
  )

(define VectorDePrueba (vector 12 1 3 44 56 2 3 4))
(CopyVector VectorDePrueba (make-vector (vector-length VectorDePrueba)) 0)