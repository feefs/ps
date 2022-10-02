# 2429. Minimize XOR
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        Bit manipulation
        """
        num_bits1, num_bits2 = bin(num1)[2:].count("1"), bin(num2)[2:].count("1")
        if num_bits1 == num_bits2:
            return num1

        # set num1's n least significant 1 bits to 0 if num2's set bit count is lower
        # set num1's n least significant 0 bits to 1 if num2's set bit count is higher
        n = abs(num_bits1 - num_bits2)
        index = 0
        while n > 0:
            mask = 1 << index
            if num_bits2 < num_bits1:
                if num1 & mask:
                    num1 &= ~mask
                    n -= 1
            elif num_bits2 > num_bits1:
                if not num1 & mask:
                    num1 |= mask
                    n -= 1
            index += 1
        return num1

    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        String manipulation
        """
        s1, s2 = list(bin(num1)[2:]), list(bin(num2)[2:])

        # pad lengths
        if len(s1) < len(s2):
            s1 = ["0" for _ in range(len(s2) - len(s1))] + s1
        elif len(s1) > len(s2):
            s2 = ["0" for _ in range(len(s1) - len(s2))] + s2

        # compute hamming weights
        set_bits1 = s1.count("1")
        set_bits2 = s2.count("1")

        if set_bits1 == set_bits2:
            return num1

        n = abs(set_bits1 - set_bits2)

        # if hamming weight of num1 is higher, set n least significant 1 bits to 0
        # if hamming weight of num2 is higher, set n least significant 0 bits to 1
        i = len(s1) - 1
        while n > 0:
            if set_bits1 > set_bits2 and s1[i] == "1":
                s1[i] = "0"
                n -= 1
            elif set_bits1 < set_bits2 and s1[i] == "0":
                s1[i] = "1"
                n -= 1
            i -= 1

        return int("".join(s1), 2)
