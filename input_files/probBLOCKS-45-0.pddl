(define (problem BLOCKS-45-0)
(:domain BLOCKS)
(:objects G1 P1 R K1 H M1 J1 A E1 J X I A1 C1 G C Y E
          W Z H1 M Q U K D N T S B S1 L N1 V B1 F1 F L1 I1 Q1 O R1 P O1 D1)
(:INIT (CLEAR G1) (CLEAR P1) (ONTABLE R) (ONTABLE K1) (ON G1 H)
                    (ON H M1) (ON M1 J1) (ON J1 A) (ON A E1) (ON E1 J)
                    (ON J X) (ON X I) (ON I A1) (ON A1 R) (ON P1 C1) (ON C1 G)
                    (ON G C) (ON C Y) (ON Y E) (ON E W) (ON W Z) (ON Z H1)
                    (ON H1 M) (ON M Q) (ON Q U) (ON U K) (ON K D) (ON D N)
                    (ON N T) (ON T S) (ON S B) (ON B S1) (ON S1 L) (ON L N1)
                    (ON N1 V) (ON V B1) (ON B1 F1) (ON F1 F) (ON F L1)
                    (ON L1 I1) (ON I1 Q1) (ON Q1 O) (ON O R1) (ON R1 P)
                    (ON P O1) (ON O1 D1) (ON D1 K1) (HANDEMPTY))
(:goal (AND (ON W P) (ON P Q) (ON Q R1) (ON R1 H1) (ON H1 S) (ON S Q1)
           (ON Q1 A1) (ON A1 J1) (ON J1 V) (ON V G) (ON G K1) (ON K1 D)
           (ON D M) (ON M E) (ON E A) (ON A D1) (ON D1 F) (ON F G1) (ON G1 P1)
           (ON P1 C) (ON C F1) (ON F1 Y) (ON Y L) (ON L M1) (ON M1 E1)
           (ON E1 B) (ON B L1) (ON L1 O) (ON O Z) (ON Z H) (ON H X) (ON X K)
           (ON K R) (ON R T) (ON T I) (ON I C1) (ON C1 S1) (ON S1 O1)
           (ON O1 U) (ON U J) (ON J B1) (ON B1 N1) (ON N1 N) (ON N I1)))
)