import requests
import warnings
import random

def get_ticker(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(
            f'https://query1.finance.yahoo.com/v6/finance/quote?symbols={ticker}',
            headers=headers, verify=False
        )

    return response.json()['finance']

def get_quote(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(
            f'https://query1.finance.yahoo.com/v6/finance/quote?symbols={ticker}',
            headers=headers, verify=False
        )

    data = response.json()['quoteResponse']['result'][0]

    return {
        '10_day_average_volume': data['averageDailyVolume10Day'],
        '3_month_average_volume': data['averageDailyVolume3Month'],
        'currency': data['currency'],
        'name': data['displayName'],

    }

def get_quote_summary(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(
            f'https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticker}?modules=summaryDetail,assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,incomeStatementHistoryQuarterly,cashflowStatementHistory,balanceSheetHistory,earnings,earningsHistory,insiderHolders,cashflowStatementHistory,cashflowStatementHistoryQuarterly,insiderTransactions,secFilings,indexTrend,earningsTrend,netSharePurchaseActivity,upgradeDowngradeHistory,institutionOwnership,recommendationTrend,balanceSheetHistory,balanceSheetHistoryQuarterly,fundOwnership,majorDirectHolders,majorHoldersBreakdown,,price,,quoteType,,esgScores',
            headers=headers, verify=False
        )

    data = response.json()['quoteSummary']['result'][0]

    return {

    }

def get_insights(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        response = requests.get(
            f'https://query1.finance.yahoo.com/ws/insights/v1/finance/insights?symbol={ticker}',
            headers=headers, verify=False
        )

    data =  response.json()['finance']['result']

    return {
        'insights': {
            'company': {
                'dividends': data['companySnapshot']['company']['dividends'],
                'earnings_reports': data['companySnapshot']['company']['earningsReports'],
                'hiring': data['companySnapshot']['company']['hiring'],
                'inovativeness': data['companySnapshot']['company']['innovativeness'],
                'insider_sentiments': data['companySnapshot']['company']['insiderSentiments'],
                'sustainability': data['companySnapshot']['company']['sustainability'],
            },
            'sector': {
                'dividends': data['companySnapshot']['sector']['dividends'],
                'earnings_reports': data['companySnapshot']['sector']['earningsReports'],
                'hiring': data['companySnapshot']['sector']['hiring'],
                'inovativeness': data['companySnapshot']['sector']['innovativeness'],
                'insider_sentiments': data['companySnapshot']['sector']['insiderSentiments'],
                'sustainability': data['companySnapshot']['sector']['sustainability'],
                'name': data['companySnapshot']['sectorInfo']
            },
            'info': {
                'provider': data['instrumentInfo']['keyTechnicals']['provider'],
                'resistance': data['instrumentInfo']['keyTechnicals']['resistance'],
                'stopLoss': data['instrumentInfo']['keyTechnicals']['stopLoss'],
                'support': data['instrumentInfo']['keyTechnicals']['support'],
            },
            'recommendation': {
                'provider': data['instrumentInfo']['recommendation']['provider'],
                'rating': data['instrumentInfo']['recommendation']['rating'],
                'target_price': data['instrumentInfo']['recommendation']['targetPrice'],
            },
            'technical_events': {
                'provider': data['instrumentInfo']['technicalEvents']['provider'],
                'short_term': data['instrumentInfo']['technicalEvents']['shortTerm'],
                'mid_term': data['instrumentInfo']['technicalEvents']['midTerm'],
                'long_term': data['instrumentInfo']['technicalEvents']['longTerm'],
            },
            'valuation': {
                'description': data['instrumentInfo']['valuation']['description'],
                'discount': data['instrumentInfo']['valuation']['discount'],
                'provider': data['instrumentInfo']['valuation']['provider'],
            },
        }
    }

def get_yfinance_data(ticker):
    data = {}
    data.update(get_insights(ticker))
    data.update(get_quote(ticker))
    data.update(get_quote_summary(ticker))

    return data

print(get_yfinance_data('aapl'))
