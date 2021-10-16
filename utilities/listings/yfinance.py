import requests
import warnings
import random
import json


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

    return response.json()


def get_quote_summary_detail(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        response = requests.get(
            f'https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticker}?modules=summaryDetail',
            headers=headers, verify=False
        )

    data = response.json()['quoteSummary']['result']

    if data:
        data = data[0]['summaryDetail']

        return {
            'price_hint': try_to_get(data, 'priceHint', 'raw'),
            'previous_close': try_to_get(data, 'previousClose', 'raw'),
            'open': try_to_get(data, 'open', 'raw'),
            'day_low': try_to_get(data, 'dayLow', 'raw'),
            'day_high': try_to_get(data, 'dayHigh', 'raw'),
            'day_low': try_to_get(data, 'dayLow', 'raw'),
            'dividend_rate': try_to_get(data, 'dividendRate', 'raw'),
            'dividend_yield': try_to_get(data, 'dividendYield', 'raw'),
            'five_year_average_dividend_yield': try_to_get(data, 'fiveYearAvgDividendYield', 'raw'),
            'ex_dividend_date': try_to_get(data, 'exDividendDate', 'raw'),
            'payout_ratio': try_to_get(data, 'payoutRatio', 'raw'),
            'beta': try_to_get(data, 'beta', 'raw'),
            'trailing_pe': try_to_get(data, 'trailingPE', 'raw'),
            'forward_pe': try_to_get(data, 'forwardPE', 'raw'),
            'volume': try_to_get(data, 'volume', 'raw'),
            'average_volume': try_to_get(data, 'averageVolume', 'raw'),
            'average_volume_10_days': try_to_get(data, 'averageVolume10days', 'raw'),
            'bid': try_to_get(data, 'bid', 'raw'),
            'ask': try_to_get(data, 'ask', 'raw'),
            'bid_size': try_to_get(data, 'bidSize', 'raw'),
            'ask_size': try_to_get(data, 'askSize', 'raw'),
            'market_cap': try_to_get(data, 'marketCap', 'raw'),
            'fifty_two_week_low': try_to_get(data, 'fiftyTwoWeekLow', 'raw'),
            'fifty_two_week_high': try_to_get(data, 'fiftyTwoWeekHigh', 'raw'),
            'price_to_sales_12_months': try_to_get(data, 'priceToSalesTrailing12Months', 'raw'),
            'fifty_day_average': try_to_get(data, 'fiftyDayAverage', 'raw'),
            'two_hundred_day_average': try_to_get(data, 'twoHundredDayAverage', 'raw'),
            'trailing_annual_dividend_rate': try_to_get(data, 'trailingAnnualDividendRate', 'raw'),
            'trailing_annual_dividend_yield': try_to_get(data, 'trailingAnnualDividendYield', 'raw'),
            'currency': try_to_get(data, 'currency', 'raw'),
        }

    else:
        return None


def get_quote_asset_profile(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        response = requests.get(
            f'https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticker}?modules=assetProfile',
            headers=headers, verify=False
        )

    data = response.json()['quoteSummary']['result']

    if data:
        data = data[0]['assetProfile']

        return {
            'address': try_to_get(data, 'address1'),
            'city': try_to_get(data, 'city'),
            'state': try_to_get(data, 'state'),
            'country': try_to_get(data, 'country'),
            'phone': try_to_get(data, 'phone'),
            'website': try_to_get(data, 'website'),
            'industry': try_to_get(data, 'industry'),
            'sector': try_to_get(data, 'sector'),
            'description': try_to_get(data, 'longBusinessSummary'),
            'employees': try_to_get(data, 'fullTimeEmployees'),
            'officers': [{
                'name': try_to_get(officer, 'name'),
                'age': try_to_get(officer, 'age'),
                'title': try_to_get(officer, 'title'),
                'year_born': try_to_get(officer, 'yearBorn'),
                'pay': try_to_get(officer, 'totalPay', 'raw'),
                'exercised_value': try_to_get(officer, 'exercisedValue', 'raw'),
                'unexercised_value': try_to_get(officer, 'unexercisedValue', 'raw'),
            } for officer in data['companyOfficers']],
            'audit_risk': try_to_get(data, 'auditRisk'),
            'board_risk': try_to_get(data, 'boardRisk'),
            'compensation_risk': try_to_get(data, 'compensationRisk'),
            'shareholder_risk': try_to_get(data, 'shareHolderRightsRisk'),
            'overall_risk': try_to_get(data, 'overallRisk'),
            'governance_date': try_to_get(data, 'governanceEpochDate'),
            'compensation_as_of_epoch_date': try_to_get(data, 'compensationAsOfEpochDate'),
        }

    else:
        return None


def get_quote_financial_data(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        response = requests.get(
            f'https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticker}?modules=financialData',
            headers=headers, verify=False
        )

    data = response.json()['quoteSummary']['result']

    print(json.dumps(data, indent='\t'))

    if data:
        data = data[0]['financialData']

        return {
            'current_price': try_to_get(data, 'currentPrice', 'raw'),
            'target_high_price': try_to_get(data, 'targetHighPrice', 'raw'),
            'target_low_price': try_to_get(data, 'targetLowPrice', 'raw'),
            'target_mean_price': try_to_get(data, 'targetMeanPrice', 'raw'),
            'target_median_price': try_to_get(data, 'targetMedianPrice', 'raw'),
            'recommendation_mean': try_to_get(data, 'recommendationMean', 'raw'),
            'recommendation_key': try_to_get(data, 'recommendationKey'),
            'number_of_analysts': try_to_get(data, 'numberOfAnalystOpinions', 'raw'),
            'total_cash': try_to_get(data, 'totalCash', 'raw'),
            'total_cash_per_share': try_to_get(data, 'totalCashPerShare', 'raw'),
            'ebitda': try_to_get(data, 'ebitda', 'raw'),
            'total_debt': try_to_get(data, 'totalDebt', 'raw'),
            'quick_ratio': try_to_get(data, 'quickRatio', 'raw'),
            'current_ratio': try_to_get(data, 'currentRatio', 'raw'),
            'total_revenue': try_to_get(data, 'totalRevenue', 'raw'),
            'debt_to_equity': try_to_get(data, 'debtToEquity', 'raw'),
            'revenue_per_share': try_to_get(data, 'revenuePerShare', 'raw'),
            'return_on_assets': try_to_get(data, 'returnOnAssets', 'raw'),
            'return_on_equity': try_to_get(data, 'returnOnEquity', 'raw'),
            'gross_profits': try_to_get(data, 'grossProfits', 'raw'),
            'free_cashflow': try_to_get(data, 'freeCashflow', 'raw'),
            'operating_cashflow': try_to_get(data, 'operatingCashflow', 'raw'),
            'earnings_growth': try_to_get(data, 'earningsGrowth', 'raw'),
            'revenue_growth': try_to_get(data, 'revenueGrowth', 'raw'),
            'gross_margins': try_to_get(data, 'grossMargins', 'raw'),
            'ebitda_margins': try_to_get(data, 'ebitdaMargins', 'raw'),
            'operating_margins': try_to_get(data, 'operatingMargins', 'raw'),
            'profit_margins': try_to_get(data, 'profitMargins', 'raw'),
            'currency': try_to_get(data, 'financialCurrency', 'raw'),
        }

    else:
        return None


def get_quote_key_statistics(ticker):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        response = requests.get(
            f'https://query1.finance.yahoo.com/v11/finance/quoteSummary/{ticker}?modules=defaultKeyStatistics',
            headers=headers, verify=False
        )

    data = response.json()['quoteSummary']['result']

    print(json.dumps(data, indent='\t'))

    if data:
        data = data[0]['defaultKeyStatistics']

        return {
            'price_hint': try_to_get(data, 'priceHint', 'raw'),
            'enterpise_value': try_to_get(data, 'enterpriseValue', 'raw'),
            'forward_pe': try_to_get(data, 'forwardPE', 'raw'),
            'profit_margins': try_to_get(data, 'profitMargins', 'raw'),
            'float_shares': try_to_get(data, 'floatShares', 'raw'),
            'shares_outstanding': try_to_get(data, 'sharesOutstanding', 'raw'),
            'shares_short': try_to_get(data, 'sharesShort', 'raw'),
            'shares_short_prior_month': try_to_get(data, 'sharesShortPriorMonth', 'raw'),
            'shares_short_prior_month_date': try_to_get(data, 'sharesShortPriorMonthDate', 'raw'),
            'date_short_interest': try_to_get(data, 'dateShortInterest', 'raw'),
            'shares_percent_out': try_to_get(data, 'sharesPercentOut', 'raw'),
            'held_percent_insiders': try_to_get(data, 'heldPercentInsiders', 'raw'),
            'held_percent_institutions': try_to_get(data, 'heldPercentInstitutions', 'raw'),
            'short_ratio': try_to_get(data, 'shortRatio', 'raw'),
            'short_percent_of_float': try_to_get(data, 'shortPercentOfFloat', 'raw'),
            'beta': try_to_get(data, 'beta', 'raw'),
            'category': try_to_get(data, 'category'),
            'book_value': try_to_get(data, 'bookValue', 'raw'),
            'price_to_book': try_to_get(data, 'priceToBook', 'raw'),
            'ytd_return': try_to_get(data, 'ytdReturn', 'raw'),
            'beta_3_year': try_to_get(data, 'beta3Year', 'raw'),
            'total_assets': try_to_get(data, 'totalAssets', 'raw'),
            'yield': try_to_get(data, 'yield', 'raw'),
            'fund_family': try_to_get(data, 'fund_family'),
            'fund_inception_date': try_to_get(data, 'fundInceptionDate', 'raw'),
            'legal_type': try_to_get(data, 'legalType'),
            'three_year_average_return': try_to_get(data, 'threeYearAverageReturn', 'raw'),
            'five_year_average_return': try_to_get(data, 'fiveYearAverageReturn', 'raw'),
            'last_fiscal_year_end': try_to_get(data, 'lastFiscalYearEnd', 'raw'),
            'next_fiscal_year_end': try_to_get(data, 'nextFiscalYearEnd', 'raw'),
            'most_recent_quarter': try_to_get(data, 'mostRecentQuarter', 'raw'),
            'earnings_quarterly_growth': try_to_get(data, 'earningsQuarterlyGrowth', 'raw'),
            'revenue_quarterly_growth': try_to_get(data, 'revenueQuarterlyGrowth', 'raw'),
            'net_income_to_common': try_to_get(data, 'netIncomeToCommon', 'raw'),
            'trailing_eps': try_to_get(data, 'trailingEps', 'raw'),
            'forward_eps': try_to_get(data, 'forwardEps', 'raw'),
            'peg_ratio': try_to_get(data, 'pegRatio', 'raw'),
            'last_split_factor': try_to_get(data, 'lastSplitFactor', 'raw'),
            'last_split_date': try_to_get(data, 'lastSplitDate', 'raw'),
            'enterprise_to_revenue': try_to_get(data, 'enterpriseToRevenue', 'raw'),
            'enterprise_to_ebitda': try_to_get(data, 'enterpriseToEbitda', 'raw'),
            'fifty_two_week_change': try_to_get(data, '52WeekChange', 'raw'),
            's_and_p_fifty_two_week_change': try_to_get(data, 'SandP52WeekChange', 'raw'),
            'last_dividend_value':try_to_get(data, 'lastDividendValue', 'raw'),
            'last_dividend_date': try_to_get(data, 'lastDividendDate', 'raw'),
            'last_cap_gain': try_to_get(data, 'lastCapGain', 'raw'),
            'annual_holdings_turnover': try_to_get(data, 'annualHoldingsTurnover', 'raw'),
        }

    else:
        return None


#,calendarEvents,incomeStatementHistory,incomeStatementHistoryQuarterly,cashflowStatementHistory,balanceSheetHistory,earnings,earningsHistory,insiderHolders,cashflowStatementHistory,cashflowStatementHistoryQuarterly,insiderTransactions,secFilings,indexTrend,earningsTrend,netSharePurchaseActivity,upgradeDowngradeHistory,institutionOwnership,recommendationTrend,balanceSheetHistory,balanceSheetHistoryQuarterly,fundOwnership,majorDirectHolders,majorHoldersBreakdown,,price,,quoteType,,esgScores',


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
                'stop_loss': try_to_get(data, 'instrumentInfo', 'keyTechnicals', 'stopLoss'),
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


def get_chart(ticker, range='1y', interval='1d'):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        response = requests.get(
            f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range={range}&interval={interval}',
            headers=headers, verify=False
        )

    data = response.json()

    return {
        'timestamps': try_to_get(data, 'chart', 'result', 0, 'timestamp'),
        'high': try_to_get(data, 'chart', 'result', 0, 'indicators', 'quote', 0, 'high'),
        'low': try_to_get(data, 'chart', 'result', 0, 'indicators', 'quote', 0, 'low'),
        'open': try_to_get(data, 'chart', 'result', 0, 'indicators', 'quote', 0, 'open'),
        'close': try_to_get(data, 'chart', 'result', 0, 'indicators', 'quote', 0, 'close'),
        'volume': try_to_get(data, 'chart', 'result', 0, 'indicators', 'quote', 0, 'volume'),
        'adjusted_close': try_to_get(data, 'chart', 'result', 0, 'indicators', 'adjclose', 0, 'adjclose'),
    }


def get_yfinance_data(ticker):
    data = {}
    data.update(get_insights(ticker))
    data.update(get_quote(ticker))
    data.update(get_quote_summary(ticker))

    return data
