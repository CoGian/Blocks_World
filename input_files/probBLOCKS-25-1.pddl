(define (problem BLOCKS-25-1)
(:domain BLOCKS)
(:objects Q M J E X O H N P R I C T D W L Y B F A G V S U K )
(:INIT (CLEAR K) (CLEAR U) (CLEAR S) (ONTABLE V) (ONTABLE G) (ONTABLE A)
 (ON K F) (ON F B) (ON B Y) (ON Y L) (ON L W) (ON W D) (ON D T) (ON T C)
 (ON C I) (ON I R) (ON R P) (ON P N) (ON N H) (ON H O) (ON O X) (ON X E)
 (ON E J) (ON J M) (ON M V) (ON U G) (ON S Q) (ON Q A) (HANDEMPTY))
(:goal (AND (ON P Y) (ON Y T) (ON T R) (ON R N) (ON N L) (ON L U) (ON U A)
            (ON A O) (ON O D) (ON D I) (ON I Q) (ON Q C) (ON C M) (ON M H)
            (ON H G) (ON G B) (ON B V) (ON V E) (ON E J) (ON J S) (ON S X)
            (ON X K) (ON K F) (ON F W)))
)