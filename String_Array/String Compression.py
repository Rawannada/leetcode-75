class Solution:
    def compress(self, chars: List[str]) -> int:
        first = chars [0]
        number = 0
        write = 0
        s = []
        for char in chars :
            if char == first :
                number = number + 1
            else :
                chars[write] = first
                write = write + 1
                if number > 1:
                 for digit in str(number):
                  chars[write] = digit
                  write = write +1
                first = char 
                number = 1
        chars[write] = first
        write = write + 1
        if number > 1:
         for digit in str(number):
            chars[write] = digit
            write = write +1
        return write
        
        