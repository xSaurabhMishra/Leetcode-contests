class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculate_area(mid: float) -> float:
            a, b = 0, 0
            for x, y, l in squares:
                yy = y + l
                area = l * l
                if mid >= yy:
                    b += area
                elif mid <= y:
                    a += area
                else:
                    aa = (yy - mid) * l
                    bb = (mid - y) * l
                    a += aa
                    b += bb
            
            return a, b

        s = set()
        for x, y, l in squares:
            s.add(y)
            s.add(y + l)
        
        
        low, high = min(s), max(s)
        while high - low > 1e-5:
            mid = (low + high) / 2
            a, b = calculate_area(mid)
            if a > b:
                low = mid  
            else:
                high = mid  
        return (low + high) / 2