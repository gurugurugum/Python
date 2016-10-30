(defun sum (n m)
	(+ n m)
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

(fibo 7)
