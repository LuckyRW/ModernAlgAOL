This application verifies whether a given algebraic structure is a ring and determines its specific properties.  
It checks for ring axioms and identifies the classification of the ring based on its properties.  

Ring Verification:  
a. Additive group is abelian  
b. Multiplication is associative  
c. Distributive property holds  

Classifications of finite rings:  
a. Field  
b. Commutative ring with unity  
c. Commutative ring  
d. Ring with unity  
e. Ring  

HOW TO USE:  
1. Input Size: Enter the dimension (n x n) of your tables  
2. Enter Tables:  
Provide addition (+) and multiplication (×) tables  
Use only the uppercase letters listed in the tables for elements (e.g., A, B, C)  
3. Check Ring: Submit tables for analysis  
4. View Results: See which ring properties your structure satisfies  

SAMPLE TABLES  
The app includes examples of various ring types as well as ring failure checks:  
1. Commutative ring: a 3x3 zero ring  
2. Field ring: Z/3Z  
3. Commutative ring wih unity: Z/4Z  
4. Boolean ring: 2x2 Boolean Ring  
5. Ring: non-commutative ring of order 4, the ring of 2×2 matrices over F2  
6. Non distributive multiplication check  
7. Non abelian addition check  
8. Non associative multiplication check  

EXAMPLE OUTPUT:  
For valid rings, you'll see analysis like:  

"""  
Commutative: Yes |All combinations are commutative  
Unity element: Yes |Identity found: B  
Exists zero divisor? : No  
All non-zero elements are units: Yes |All nonzero elements have inverses.  
Analysis:   
This is a field! the multiplicative group is commutative,   
doesnt have zero divisors, has a unity element, and all non-zero elements are units.   
 It is known that fields are also both integral domains and division rings!   
 A known example of a field is Z/pZ, where p is a prime   
number.  
"""  

However,  for invalid rings you will see which axioms it fails  

"""  
Not associative for: B, C, C -> A != B  
"""  

NOTE:  
Currently case-sensitive and cannot change the name of the elements (also, use ALL CAPS for elements).  
This application will automatically detect the ones and zeros of a given ring. However,  
It isn't possible yet to automatically assign an element as the identity element of such group, or in short to assign the ones and zeros of the ring.  
A scroll bar exists at the side and the bottom of the application in the case of extremely large tables, although admittedly it doesn't stand out much.  
