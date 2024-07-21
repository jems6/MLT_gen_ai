import requests

class SecEgdar:
    def __init__(self, url) -> None:
        self.comps = {}
        self.ticks = {}
        headers = {'user-agent' : 'MLT CP josuemelendez619@gmail.com'}
        r = requests.get(url, headers=headers)
        data = r.json()
        #print(data)
        for comp in data:
            # comp is the nth company, to get its dictionary to data[company]
            company = data[comp]
            #print(f'CURRENT COMPANT: {comp}, {data[comp]}')
            #print(f'Loading {company}')
            self.comps[company['title']] = company['cik_str']
            self.ticks[company['ticker']] = company['cik_str']
            if(self.comps.get(company['title']) == None):
                print(f'Error loading {company}')
        print(f'Loaded {len(self.comps)} companies, with {len(self.ticks)} tickers')

    def name_to_cik(self, name):
        cik = self.comps.get(name)
        if cik is None:
            raise ValueError('Company not found')
        for ticker, target in self.ticks.items():
            if(target == cik):
                return (name, ticker, cik)    
        raise ValueError('Ticker not found')

    def ticket_to_cik(self, ticker):
        cik = self.ticks.get(ticker)
        if cik is None:
            raise ValueError('Ticker not found')
        for name, target in self.comps.items():
            if(target == cik):
                return (name, ticker, cik)
        raise ValueError('Company not found')
s = SecEgdar('https://www.sec.gov/files/company_tickers.json')
print(s.name_to_cik('Apple Inc.'))