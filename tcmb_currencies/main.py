import CurrencyProviderTCMB

def main():
    print("Started...")
    
    cp = CurrencyProviderTCMB.CurrencyProviderTCMB()
    print(cp.get_specifict_currency_code_and_buy_sell_rates('USD'))
    

if __name__ == "__main__":
    main()