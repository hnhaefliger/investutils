import requests
import warnings
import random

def try_to_get(dict, *args):
    try:
        for arg in args:
            dict = dict[arg]

        return dict

    except:
        return None

def get_ticker(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
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
        '10_day_average_volume': try_to_get(data, 'averageDailyVolume10Day'),
        '3_month_average_volume': try_to_get(data, 'averageDailyVolume3Month'),
        'currency': try_to_get(data, 'currency'),
        'name': try_to_get(data, 'displayName'),
        'dividend_data': try_to_get(data, 'dividendDate'),
        'earnings_date': try_to_get(data, 'earningsTimestamp'),
        'current_eps': try_to_get(data, 'epsCurrentYear'),
        'forward_eps': try_to_get(data, 'epsForward'),
        '12_month_eps': try_to_get(data, 'epsTrailingTwelveMonths'),
        'esg_populated': try_to_get(data, 'esgPopulated'),
        'exchange': try_to_get(data, 'fullExchangeName'),
        'bid': try_to_get(data, 'bid'),
        'ask': try_to_get(data, 'ask'),
        '50_day_average': try_to_get(data, 'fiftyDayAverage'),
        '52_week_high': try_to_get(data, 'fiftyTwoWeekHigh'),
        '52_week_low': try_to_get(data, 'fiftyTwoWeekLow'),
        'forward_pe': try_to_get(data, 'forwardPE'),
        'market': try_to_get(data, 'market'),
        'market_cap': try_to_get(data, 'marketCap'),
        'market_state': try_to_get(data, 'marketState'),
        'price_eps_current_year': try_to_get(data, 'priceEpsCurrentYear'),
        'shares_outstanding': try_to_get(data, 'sharesOutstanding'),
        'trailing_annual_dividend_rate': try_to_get(data, 'trailingAnnualDividendRate'),
        'trailing_annual_dividend_yield': try_to_get(data, 'trailingAnnualDividendYield'),
        'trailing_pe': try_to_get(data, 'trailingPE'),
        '200_day_average': try_to_get(data, 'twoHundredDayAverage'),
    }

def get_quote_summary(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
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
        warnings.simplefilter('ignore')
        response = requests.get(
            f'https://query1.finance.yahoo.com/ws/insights/v1/finance/insights?symbol={ticker}',
            headers=headers, verify=False
        )

    data =  response.json()['finance']['result']

    return {
        'insights': {
            'company': {
                'dividends': try_to_get(data, 'companySnapshot', 'company', 'dividends'),
                'earnings_reports': try_to_get(data, 'companySnapshot', 'company', 'earningsReports'),
                'hiring': try_to_get(data, 'companySnapshot', 'company', 'hiring'),
                'inovativeness': try_to_get(data, 'companySnapshot', 'company', 'innovativeness'),
                'insider_sentiments': try_to_get(data, 'companySnapshot', 'company', 'insiderSentiments'),
                'sustainability': try_to_get(data, 'companySnapshot', 'company', 'sustainability'),
            },
            'sector': {
                'dividends': try_to_get(data, 'companySnapshot', 'sector', 'dividends'),
                'earnings_reports': try_to_get(data, 'companySnapshot', 'sector', 'earningsReports'),
                'hiring': try_to_get(data, 'companySnapshot', 'sector', 'hiring'),
                'inovativeness': try_to_get(data, 'companySnapshot', 'sector', 'innovativeness'),
                'insider_sentiments': try_to_get(data, 'companySnapshot', 'sector', 'insiderSentiments'),
                'sustainability': try_to_get(data, 'companySnapshot', 'sector', 'sustainability'),
                'name': try_to_get(data, 'companySnapshot', 'sectorInfo')
            },
            'info': {
                'provider': try_to_get(data, 'instrumentInfo', 'keyTechnicals', 'provider'),
                'resistance': try_to_get(data, 'instrumentInfo', 'keyTechnicals', 'resistance'),
                'stopLoss': try_to_get(data, 'instrumentInfo', 'keyTechnicals', 'stopLoss'),
                'support': try_to_get(data, 'instrumentInfo', 'keyTechnicals', 'support'),
            },
            'recommendation': {
                'provider': try_to_get(data, 'instrumentInfo', 'recommendation', 'provider'),
                'rating': try_to_get(data, 'instrumentInfo', 'recommendation', 'rating'),
                'target_price': try_to_get(data, 'instrumentInfo', 'recommendation', 'targetPrice'),
            },
            'technical_events': {
                'provider': try_to_get(data, 'instrumentInfo', 'technicalEvents', 'provider'),
                'short_term': try_to_get(data, 'instrumentInfo', 'technicalEvents', 'shortTerm'),
                'mid_term': try_to_get(data, 'instrumentInfo', 'technicalEvents', 'midTerm'),
                'long_term': try_to_get(data, 'instrumentInfo', 'technicalEvents', 'longTerm'),
            },
            'valuation': {
                'description': try_to_get(data, 'instrumentInfo', 'valuation', 'description'),
                'discount': try_to_get(data, 'instrumentInfo', 'valuation', 'discount'),
                'provider': try_to_get(data, 'instrumentInfo', 'valuation', 'provider'),
            },
        }
    }

def get_yfinance_data(ticker):
    data = {}
    data.update(get_insights(ticker))
    data.update(get_quote(ticker))
    data.update(get_quote_summary(ticker))

    return data
