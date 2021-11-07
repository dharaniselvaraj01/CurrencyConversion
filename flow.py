import pandas as pd 
import fxcalculator as fxc
import userinp as ip

def run():
    table = pd.read_csv('conv.txt',delimiter=',')
    table.set_index('/',inplace=True)
    non_crosslist = ["D","Inv"]

    while True:
        try:
            from_curr, to_curr, amt = ip.get_input()
            valid_currency = ip.check_currency(from_curr,to_curr)
            if valid_currency:
                method = table[to_curr][from_curr]
                if method == "1:1":
                    unity = fxc.Unity(from_curr,to_curr)
                    unity_rate = unity.calculate_conv_rate()
                    converted_amt = fxc.ConvertAmount(amt,unity_rate).convert_amt()
                elif method in non_crosslist:
                    noncross = fxc.NonCross(from_curr,to_curr)
                    noncross_rate = noncross.calculate_conv_rate() 
                    converted_amt = fxc.ConvertAmount(amt,noncross_rate).convert_amt()
                elif method == "USD":
                    crossusd = fxc.CrossUsd(from_curr,to_curr)
                    crossusd_rate = crossusd.calculate_conv_rate()
                    converted_amt = fxc.ConvertAmount(amt,crossusd_rate).convert_amt()
                else:
                    crosseur = fxc.CrossEur(from_curr,to_curr)
                    crosseur_rate = crosseur.calculate_conv_rate()
                    converted_amt = fxc.ConvertAmount(amt,crosseur_rate).convert_amt()
                if to_curr == "JPY":
                    print(f"={to_curr} {converted_amt:.0f}")
                else:
                    print(f"={to_curr} {converted_amt:.2f}")
                
            else:
                print(f"Unable to find rate for {from_curr}/{to_curr}")

        except IndexError:
            print("Enter currency and amount in the format Curr amount eg: CAD 100:00")
            continue
    
        except TypeError:
            print("Enter currency first , followed by amount eg: CAD 100:00")
            continue
    
        except ValueError:
            print("Enter currency first(3letters) , followed by amount(positive number) eg: CAD 100:00")
            continue