;Developed by Shane Flynn

#lang Scheme

;Find the index of a value in a list if it exists
(define index-of
  (λ (val lst)
    (cond
      ((null? lst) -1)
      ((not (list? lst)) "Error: Not a list")
      ((eq? (car lst) val) 0)
      (else
       (cond
         ((eq? (+ 1 (index-of val (cdr lst))) 0) -1)
         (else (+ 1 (index-of val (cdr lst)))))))))

;List the values at the even indicies in a list
(define list-evens
  (λ (lst)
    (cond
      ((not (list? lst)) "Error: Not a list")
      ((null? lst) '())
      ((null? (cdr lst)) (cons (car lst) '()))
      (else (cons (car lst) (list-evens (cdr (cdr lst))))))))