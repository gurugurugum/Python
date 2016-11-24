(define a 1)
(define b 1)

(defun sum (n m)
	(+ n m)
)

(defun suma (n)
	(+ n a)
)

(defun sumb (n)
	(+ n b)
)

(defun sub (n m)
	(- n m)
)

(defun fibo (n)
	(if (< n 3)
		1
		(+ (fibo (sub n 1)) (fibo (sub n 2)) )
	)
)

(defun ack (n m)
	(if (< m 1)
		(+ n 1)
		(if (< n 1)
			(ack (- m 1) 1)
			(ack (- m 1) (ack m (- n 1)))
		)
	)
)

;(ack 1 1)
(fibo (+ 1 (* a b 3)))

;(for (i 1 10)
;	(= a (+ a 1))
;)
