class Hello:
   def solve(self, s, k):
      def shift(c):
         i = ord(c) - ord('a')
         i += k
         i %= 26
         return chr(ord('a') + i)

      return "".join(map(shift, s))

ob = Hello()

word = str(input("Enter the Message: "))

print(("Encrypted Message: " + ob.solve(word, 3)))