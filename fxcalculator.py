from abc import abstractmethod, ABC 
import currencybt as cb
import pandas as pd

currency_list = cb.currency_list
all_pair = cb.all_pair


class Conversion(ABC):
    
    def __init__(self,from_curr,to_curr,amt):
        self.from_curr = from_curr
        self.to_curr = to_curr
        self.amt = amt       

    @abstractmethod
    def calculate_conv_rate(self):
        pass
        
    def calculate_converted_amt(self):
        return round(self.amt*self.calculate_conv_rate(),2) 

class Unity(Conversion):

    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)
        

    def calculate_conv_rate(self):
        return 1

    


class NonCross(Conversion):

    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)

    def calculate_conv_rate(self):
        pair = (self.from_curr,self.to_curr)
        fac = all_pair[pair]
        return fac

    
class CrossConversion(Conversion):

    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)

    def calculate_conv_rate(self,curr_pair):
        self.curr1, self.curr2 = curr_pair
        pair = (self.curr1,self.curr2)
        fac = all_pair[pair]
        return fac 
      

class CrossUsd(CrossConversion):

    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)
       

    def calculate_converted_amt(self):
        pair1 = (self.from_curr,'USD')
        fac1 = super().calculate_conv_rate(pair1)
        pair2 = ('USD',self.to_curr)
        actual_pair = (self.from_curr,self.to_curr)
        check_pair = tuple(set(pair1).symmetric_difference(set(pair2)))
        if sorted(check_pair) == sorted(actual_pair) and pair2 in all_pair:
                fac2 = super().calculate_conv_rate(pair2)
                return round(self.amt* fac1*fac2,2)
        else:
                pair2 = ('USD','EUR')
                fac2 = super().calculate_conv_rate(pair2)
                pair3 = ('EUR',self.to_curr)
                fac3 = super().calculate_conv_rate(pair3)
                return round(self.amt*fac1*fac2*fac3,2)

        
class CrossEur(CrossConversion):

    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)

    def calculate_converted_amt(self):
        pair1 = (self.from_curr,'EUR')
        fac1 = super().calculate_conv_rate(pair1)
        pair2 = ('EUR',self.to_curr)
        actual_pair = (self.from_curr,self.to_curr)
        check_pair = tuple(set(pair1).symmetric_difference(set(pair2)))
        if sorted(check_pair) == sorted(actual_pair) and pair2 in all_pair:
            fac2 = super().calculate_conv_rate(pair2)
            return round(self.amt*fac1*fac2,2)
        else:
            pair2 = ('EUR','USD')
            fac2 = super().calculate_conv_rate(pair2)
            pair3 = ('EUR',self.to_curr)
            fac3 = super().calculate_conv_rate(pair3)
            return round(self.amt*fac1*fac2*fac3,2)
                    


class UnityInstance(Unity):

    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)
        

    def create_instance(self):
        unity = Unity(self.from_curr,self.to_curr,self.amt)
        converted_amt = unity.calculate_converted_amt()
        return converted_amt


class NonCrossInstance(NonCross):
    
    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)

    def create_instance(self):
        noncross = NonCross(self.from_curr,self.to_curr,self.amt)
        converted_amt = noncross.calculate_converted_amt()
        return converted_amt

class CrossUsdInstance(CrossUsd):
    
    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)

    def create_instance(self):
        crossusd = CrossUsd(self.from_curr,self.to_curr,self.amt)
        converted_amt = crossusd.calculate_converted_amt()
        return converted_amt

class CrossEurInstance(CrossEur):
    
    def __init__(self,from_curr,to_curr,amt):
        super().__init__(from_curr,to_curr,amt)

    def create_instance(self):
        crosseur = CrossEur(self.from_curr,self.to_curr,self.amt)
        converted_amt = crosseur.calculate_converted_amt()
        return converted_amt

class MethodExecute(UnityInstance,NonCrossInstance,CrossUsdInstance,CrossEurInstance):
    
    def __init__(self,from_curr,to_curr,amt):
        self.from_curr = from_curr
        self.to_curr = to_curr
        self.amt = amt

    def method_picker(self):
        
        table = pd.read_csv('conv.txt',delimiter=',')
        table.set_index('/',inplace=True)
        non_crosslist = ["D","Inv"]
        method = table[self.to_curr][self.from_curr]
        
        if method == "1:1":
            return UnityInstance(self.from_curr,self.to_curr,self.amt).calculate_converted_amt()
        elif method in non_crosslist:
            return NonCrossInstance(self.from_curr,self.to_curr,self.amt).calculate_converted_amt()
        elif method == "USD" : 
            return CrossUsdInstance(self.from_curr,self.to_curr,self.amt).calculate_converted_amt()
        else:
            return CrossEurInstance(self.from_curr,self.to_curr,self.amt).calculate_converted_amt()


class DisplayOutput:

    def __init__(self,converted_amt,to_curr):
        self.converted_amt = converted_amt
        self.to_curr = to_curr

    def check_jpy(self):
        return self.to_curr == "JPY"

    def __str__(self):
        check_jpy = self.check_jpy()
        if not check_jpy:
            return f"={self.to_curr} {self.converted_amt:.2f}"
        else:
            return f"={self.to_curr} {self.converted_amt:.0f}"
