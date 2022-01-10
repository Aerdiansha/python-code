# Program to display the Fibonacci sequence up to n-th term

angka = int(input("Berapa banyak angka yang mau ditampilkan? "))

# first two terms
nilai1, nilai2 = 0, 1
hitungan = 0

# check if the number of terms is valid
if nterms <= 0:
   print("angka tidak boleh 0 atau negatif")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1