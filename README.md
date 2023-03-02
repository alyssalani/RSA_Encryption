# RSA_Encryption
Encrypt and Decrpyt messages

Instructions for this assignment:
  Write a class called RSA.
   - Write a method called GenerateKeys that takes two very long text strings as input.
      Treat the text strings as base 26 numbers, and convert them to base 10 numbers
      mod by 10^200 to make them the right size. Ensure that they were longer than 10^200 before doing the mod, or print a Warning message.
      Make them odd. Then start adding 2 until they are prime.
      Now you have your two, 200 digit prime numbers, p and q.
      Calculate n = p*q
      Calculate r = (p-1)*(q-1)
      Find e – a 398 digit number that is relatively prime with r.
      Find d – the inverse of e mod r.
      Save n and e to a file called public.txt (write them as text, with 1 return after each number)
      Save n and d to a file called private.txt
      All other variables can be discarded.
   - Write a method called Encrypt that takes as parameters the name of an input text file and the name of an output text file.
      Open the input file (which should already exist in the current directory and be full of plain text). Use binary mode, then convert the contents to text mode as follows:
      Use this alphabet:
      alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      Treat the input file text as a base 70 integer, and convert it to base 10, using block sizes so as to not exceed integer n.
      Encode each block using the rules of RSA.  (Read n and e from public.txt)
      Convert the resulting integers back to the base 70 alphabet, and write to the output file.  Put a $ after each block to indicate where each block ends. Note that the output file should also be opened in binary mode, so to write text to it, the text must first be converted to binary as follows:
      fout.write( stringMessage.encode("utf-8") )
   - Write a method called Decrypt that takes as parameters the name of an input text file and the name of an output text file.
      Open the input file in binary mode (which should already exist and be full of encrypted text).
      Use the same alphabet as above.
      Treat the input file text as a base 70 integer, and convert it to base 10, using block sizes as indicated by the $ signs.
      Decode each block using the rules of RSA.  (Read n and d from private.txt)
      Convert the resulting integers back to the base 70 alphabet, and write to the output file, again converting to binary mode as explained above.
   - Write a main function to test your code
      o    Make a class of type RSA

      o    Generate the key files by calling GenerateKeys with two very long strings of lowercase letters that only you would remember.

      o    Make a plain text file consisting of only letters in the alphabet.  It should be long enough to require multiple encoding blocks.

      o    Call your Encrypt method.

      o    Call your Decrypt method.

      o    Verify that the decoded output file exactly matches the original plain text file.
