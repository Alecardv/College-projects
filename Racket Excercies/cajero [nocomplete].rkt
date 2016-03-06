;Este programa aun esta incompleto, revisar los comentarios para saber que falta

(define usr1 (vector "usr"   "1234"  )) ;Usuario normal
(define usr2 (vector "admin" "123456")) ;Usuario administrador
(define ctas (make-vector 100)) ;Vector que guarda las cuentas
(vector-set! ctas 0 (vector 35 "Alejandro C."  "3207651940" 500000 1)) ;el uno al final significa activo, 0 inactivo
(vector-set! ctas 1 (vector 43 "Diego Osorio"  "3217023750" 600000 1))

(define (chPassAdmin) ;cambia la contraseña del administrdor
  (begin
    (display "Ingrese una nueva contraseña para el adiministrador: ")
    (vector-set! usr2 1 (read))
    (display "susess")
    )
  )

(define (crearCta) ;crea una cuenta nueva
  (display "Ingrese los datos de la nueva cuenta en este orden: ")
  (newline)
  (display "Numero de cuenta.")(newline)
  (display "Nombre.")(newline)
  (display "Telefono.")(newline)
  (vector-set! ctas (vector-length ctas)
               (vector (read) (read) (read) 1) )
  )
  

(define (cancelarCta ncta pos) ;cancela una cuenta
  (if (> pos (- (vector-length ctas) 1))
      (display "Account not found")
      (if (= (vector-ref (vector-ref ctas pos) 0) ncta)
          (vector-fill! (vector-ref ctas pos)) ;If->True
          (cancelarCta ncta (+ pos 1))         ;If->False
          )
      )
  )

(define (modificarDatos ncta pos)
  (if (> pos (- (vector-length ctas) 1))
      (display "Account not found")
      (if (= (vector-ref (vector-ref ctas pos) 0) ncta)
          (begin
            (display "Ingrese nuevo nombre: ")
            (vector-set! (vector-ref ctas pos) 1 (read))
            (display "Ingrese nuevo telefono: ")
            (vector-set! (vector-ref ctas pos) 2 (read))
            (display "Ingrese nuevo saldo: ")
            (vector-set! (vector-ref ctas pos) 3 (read))
            )
          (modificarDatos ncta (+ pos 1))
          )
      )
  )

(define (mostrarNombres pos)
  (if (> pos (- (vector-length ctas) 1))
      (newline)
      (begin
        (vector-ref (vector-ref ctas pos) 1)
        (newline)
        (mostrarNombres (+ pos 1))
        )
      )
  )

(define (mostrarCuentas pos)
  (if (> pos (- (vector-length ctas) 1))
      (newline)
      (begin
        (vector-ref (vector-ref ctas pos) 0)
        (newline)
        (mostrarCuentas (+ pos 1))
        )
      )
  )

(define (ncta) ;Lee un numero de cuenta
  (display "Ingrese el numero de la cuenta a modificar: ")
  (read)
  )
(define (optionsadmin opt) ;Menu que llama las funciones de admin
  (cond
    [(equal? opt 1) (cancelarCta (ncta) 0)]
    [(equal? opt 2) (modificarDatos (ncta) 0)]
    [(equal? opt 3) (chPassAdmin)]
    [(equal? opt 4) (mostrarNombres 0)]
    [(equal? opt 5) ( )] ;Aqui falta (Listar alfabeticamente)
    [(equal? opt 6) (mostrarCuentas 0)]
    [(equal? opt 7) (crearCta)]
    [(equal? opt 8) ( )] ;Aqui falta (activar desactivar cuenta)
    [(equal? opt 9) (exit)]
    (else (begin
            (display "Opcion incorrecta, intente de nuevo")
            (newline)
            (optionsadmin (read)) )
          )
    )  )

(define (optionsusr opt) ;Menu que llama las funciones de usuario
  (cond
    [(equal? opt 1) ( )](newline) ;aqui falta (retirar)
    [(equal? opt 2) ( )](newline) ;aqui falta (consultar)
    [(equal? opt 3) ( )](newline) ;aqui falta (consignar)
    [(equal? opt 4) (exit)]
    (else (begin
            (display "Opcion incorrecta, intente de nuevo")
            (newline)
            (optionsusr (read)) )
          )
    )  )

(define (menuadmin) ;Menu que muestra las funciones de admin
  (display "1. Cancelar cuenta")(newline)
  (display "2. Modificar datos")(newline)
  (display "3. Cambiar contraseña de admnistrador")(newline)
  (display "4. Lista de clientes general")(newline)
  (display "5. Lista de clientes alfabetico")(newline) ;falta
  (display "6. Lista de cuentas")(newline)
  (display "7. Crear cuenta")(newline)
  (display "8. Activar/Desactivar cuenta")(newline) ;falta
  (display "9. Salir")(newline)
  (display "Seleccione una opcion: ")
  (optionsadmin (read))
  )

(define (menuusr) ;Menu que muestra las funciones de usuario
  (display "1. Retirar.") ;falta
  (display "2. Consultar.") ;falta
  (display "3. Consignar.") ;falta
  (display "4. Salir.")
  (optionsusr (read))
  )

(define (Login usr pass) ;Verificacion del inicio de session
  (if (equal? usr (vector-ref usr1 0))
      (if (equal? pass (vector-ref usr1 1))
          (menuusr)
          )
      (if (equal? usr (vector-ref usr2 0))
          (if (equal? pass (vector-ref usr2 1))
              (menuadmin)
              )
          )
      ) )

(define rUsr ;Lee el nombre de usuario
  {begin
   (display "Usuario: ")
   (read)
  } )

(define rPass ;Lee la contraseña
  {begin
   (display "Contraseña: ")
   (read)
  } )

(define (main) ;Funcion inicial
  (Login rUsr rPass)
  )

(main) ;Llamado deseencadenante