#lang Scheme

; Developed by Shane Flynn
;
; Part 1
;
; Find all prime numbers that is less than or equal to an input number
; Argument:
;     Integer
; Return:
;     List of prime numbers
(define list-primes-below
  (λ (n)
    (cond
      ((or (zero? n) (eq? n 1) (eq? n 2)) '())
      (else
       (build-prime-list '() #t (- n 1) (- n 1))))))

; Build a list of prime numbers
; Helper function for list-primes-below
; Arguments:
;     Empty list,
;     #t for isPrime,
;     Integer to build up to,
;     Recursive iterative integer set to int to build up to initially
; Return:
;     List of prime numbers
(define build-prime-list
  (λ (primeList isPrime n i)
    (cond
      ((eq? i 2) '(2))
      ((eq? i 3) '(3 2))
      (else
       (let ([isPrime (check-if-prime i 2)])
       (cond
         ((eq? isPrime #t) (cons i (build-prime-list primeList #t n (- i 1))))
         (else (build-prime-list primeList #t n (- i 1)))))))))
      
; Check if a given number is prime
; Helper function for build-prime-list
; Arguments:
;     Integer to check,
;     2 initially
; Return:
;     #t if prime
;     #f if not prime
(define check-if-prime
  (λ (i x)
    (cond
      ((zero? (modulo i x)) #f)
      ((eq? x (floor (/ i 2))) #t)
      (else (check-if-prime i (+ x 1))))))

; Part 2

(define bst?
  (λ (binT)
    (cond
      ((null? binT) #t)
      ((and (null? (car (cdr binT))) (null? (car (cddr binT)))) #t) ; If left and right sub-tree don't exist
      (else
       (let ((parentValue (car binT)))
         (let ((lRetVal
                (cond
                  ((null? (car (cdr binT))) #t) ; If left sub-tree doesn't exist
                  (else
                   (let ((lChildValue (caar (cdr binT)))
                         (lChildNode (car (cdr binT))))
                     (cond
                       ((<= lChildValue parentValue) (bst? lChildNode))
                       (else #f))))))
               (rRetVal
                (cond
                  ((null? (car (cddr binT))) #t) ; If right sub-tree doesn't exist
                  (else
                   (let ((rChildValue (caar (cddr binT)))
                         (rChildNode (car (cddr binT))))
                     (cond
                       ((> rChildValue parentValue) (bst? rChildNode))
                       (else #f)))))))
           (cond
             ((and lRetVal rRetVal) #t)
             (else #f))))))))