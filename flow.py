import fxcalculator as fxc
import userinp as ip

def run():
        
    while True:
        try:
            from_curr, to_curr, amt = ip.get_input()
            valid_currency = ip.check_currency(from_curr,to_curr)
            if valid_currency:
                method_picker = fxc.MethodExecute(from_curr,to_curr,amt)
                converted_amt = method_picker.method_picker()
                print(fxc.DisplayOutput(converted_amt,to_curr))
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

        