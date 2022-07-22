import CurrencyProviderTCMB

def main():
    print("Started...")
    
    cp = CurrencyProviderTCMB.CurrencyProviderTCMB()
    print(cp.get_currency_data())
    

if __name__ == "__main__":
    main()