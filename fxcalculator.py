from abc import abstractmethod, ABC 
import currencybt as cb

currency_list = cb.currency_list
all_pair = cb.all_pair


class Conversion(ABC):
    
    def __init__(self,from_curr,to_curr):
        self.from_curr = from_curr
        self.to_curr = to_curr
       

    @abstractmethod
    def calculate_conv_rate(self):
        pass
        


class Unity(Conversion):
    def __init__(self,from_curr,to_curr):
        super().__init__(from_curr,to_curr)

    def calculate_conv_rate(self):
        return 1

class NonCross(Conversion):
    def __init__(self,from_curr,to_curr):
        super().__init__(from_curr,to_curr)

    def calculate_conv_rate(self):
        pair = (self.from_curr,self.to_curr)
        fac = all_pair[pair]
        return fac

    

class CrossConversion:
    def __init__(self,from_curr,to_curr):
        self.from_curr = from_curr
        self.to_curr = to_curr

    def calculate_crossconv_rate(self,curr_pair):
        self.curr1, self.curr2 = curr_pair
        pair = (self.curr1,self.curr2)
        fac = all_pair[pair]
        return fac 
      

class CrossUsd(CrossConversion):
    def __init__(self,from_curr,to_curr):
        super().__init__(from_curr,to_curr)
       

    def calculate_conv_rate(self):
        pair1 = (self.from_curr,'USD')
        fac1 = super().calculate_crossconv_rate(pair1)
        pair2 = ('USD',self.to_curr)
        actual_pair = (self.from_curr,self.to_curr)
        check_pair = tuple(set(pair1).symmetric_difference(set(pair2)))
        if sorted(check_pair) == sorted(actual_pair) and pair2 in all_pair:
                fac2 = super().calculate_crossconv_rate(pair2)
                return fac1*fac2
        else:
                pair2 = ('USD','EUR')
                fac2 = super().calculate_crossconv_rate(pair2)
                pair3 = ('EUR',self.to_curr)
                fac3 = super().calculate_crossconv_rate(pair3)
                return fac1*fac2*fac3

        

class CrossEur(CrossConversion):
    def __init__(self,from_curr,to_curr):
        super().__init__(from_curr,to_curr)

    def calculate_conv_rate(self):
        pair1 = (self.from_curr,'EUR')
        fac1 = super().calculate_crossconv_rate(pair1)
        pair2 = ('EUR',self.to_curr)
        actual_pair = (self.from_curr,self.to_curr)
        check_pair = tuple(set(pair1).symmetric_difference(set(pair2)))
        if sorted(check_pair) == sorted(actual_pair) and pair2 in all_pair:
            fac2 = super().calculate_crossconv_rate(pair2)
            return fac1*fac2
        else:
            pair2 = ('EUR','USD')
            fac2 = super().calculate_crossconv_rate(pair2)
            pair3 = ('EUR',self.to_curr)
            fac3 = super().calculate_crossconv_rate(pair3)
            return fac1*fac2*fac3


     