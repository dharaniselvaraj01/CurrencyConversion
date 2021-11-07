from currencybt import currency_list

def get_input():
    print("From:",end=" ")
    inp = input()
    from_curr = inp.split(" ")[0].upper()
    amt = float(inp.split(" ")[1])
    print("To:", end=" ")
    to_curr = input().upper()
    return from_curr,to_curr,amt



def check_currency(curr1,curr2):
    return (curr1 in currency_list) and (curr2 in currency_list)

    