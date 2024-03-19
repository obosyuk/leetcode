class Solution:
    def mySqrt(self, x: int) -> int:
        first_el, last_el = 0, x

        while first_el <= last_el:
            mid = (last_el + first_el) // 2

            if mid * mid > x:
                last_el = mid - 1
            elif mid * mid < x:
                first_el = mid + 1
            else:
                return mid

        return last_el