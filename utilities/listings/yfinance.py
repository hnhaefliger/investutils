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

    return response.json()

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
        'city': try_to_get(data, 'assetProfile', 'city'),
        'state': try_to_get(data, 'assetProfile', 'state'),
        'country': try_to_get(data, 'assetProfile', 'country'),
        'website': try_to_get(data, 'assetProfile', 'website'),
        'industry': try_to_get(data, 'assetProfile', 'industry'),
        'sector': try_to_get(data, 'assetProfile', 'sector'),
        'description': try_to_get(data, 'assetProfile', 'longBusinessSummary'),
        'employees': try_to_get(data, 'assetProfile', 'fillTimeEmployees'),
        'officers': [
            {
                'name': try_to_get(officer, 'name'),
                'age': try_to_get(officer, 'age'),
                'title': try_to_get(officer, 'title'),
                'born': try_to_get(officer, 'yearBorn'),
                'pay': try_to_get(officer, 'totalPay', 'raw'),
                'exercised_value': try_to_get(officer, 'exercisedValue', 'raw'),
                'unexercised_value': try_to_get(officer, 'unexercisedValue', 'raw'),
            } for officer in try_to_get(data, 'assetProfile', 'companyOfficers')
        ],
        'audit_risk': try_to_get(data, 'assetProfile', 'auditRisk'),
        'board_risk': try_to_get(data, 'assetProfile', 'boardRisk'),
        'compensation_risk': try_to_get(data, 'assetProfile', 'compensationRisk'),
        'shareholder_rights_risk': try_to_get(data, 'assetProfile', 'shareHolderRightsRisk'),
        'overall_risk': try_to_get(data, 'assetProfile', 'overallRisk'),
        'governance_epoch_date': try_to_get(data, 'assetProfile', 'governanceEpochDate'),
        'compensation_as_of_epoch_date': try_to_get(data, 'assetProfile', 'compensationAsOfEpochDate'),
        'trends': [
            {
                'period': try_to_get(trend, 'period'),
                'strong_buy': try_to_get(trend, 'strongBuy'),
                'buy': try_to_get(trend, 'buy'),
                'hold': try_to_get(trend, 'hold'),
                'sell': try_to_get(trend, 'sell'),
                'strong_sell': try_to_get(trend, 'strongSell'),
            } for trend in try_to_get(data, 'recommendationTrend', 'trend')
        ],
        'cashflow': {
            'end_date': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'endDate', 'raw'),
            'net_income': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'netIncome', 'raw'),
            'depreciation': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'depreciation', 'raw'),
            'change_to_net_income': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'changeToNetincome', 'raw'),
            'change_to_account_receivables': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'changeToAccountReceivables', 'raw'),
            'change_to_liabilities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'changeToLiabilities', 'raw'),
            'change_to_inventory': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'changeToInventory', 'raw'),
            'change_to_operating_activities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'changeToOperatingActivities', 'raw'),
            'total_cash_from_operating_activities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'totalCashFromOperatingActivities', 'raw'),
            'capital_expenditures': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'capitalExpenditures', 'raw'),
            'other_cashflows_from_investing_activities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'otherCashflowsFromInvestingActivities', 'raw'),
            'total_cashflows_from_investing_activities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'totalCashflowsFromInvestingActivities', 'raw'),
            'net_borrowings': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'netBorrowings', 'raw'),
            'other_cashflows_from_financial_activities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'otherCashflowsFromFinancingActivities', 'raw'),
            'total_cash_from_financing_activities': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'totalCashFromFinancingActivities', 'raw'),
            'effect_of_exchange_rate': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'effectOfExchangeRate', 'raw'),
            'change_in_cash': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'changeInCash', 'raw'),
            'issuance_of_stock': try_to_get(data, 'cashflowStatementHistory', 'cashflowStatements', 0, 'issuanceOfStock', 'raw'),
        },
        'price_hint': try_to_get(data, 'defaultKeyStatistics', 'priceHint', 'raw'),
        'forward_pe': try_to_get(data, 'defaultKeyStatistics', 'forwardPE', 'raw'),
        'enterprise_value': try_to_get(data, 'defaultKeyStatistics', 'enterpriseValue', 'raw'),
        'profit_margins': try_to_get(data, 'defaultKeyStatistics', 'profitMargins', 'raw'),
        'float_shares': try_to_get(data, 'defaultKeyStatistics', 'floatShares', 'raw'),
        'shares_outstanding': try_to_get(data, 'defaultKeyStatistics', 'sharesOutstanding', 'raw'),
        'shares_short': try_to_get(data, 'defaultKeyStatistics', 'sharesShort', 'raw'),
        'shares_short_prior_month': try_to_get(data, 'defaultKeyStatistics', 'sharesShortPriorMonth', 'raw'),
        'shares_short_previous_month_date': try_to_get(data, 'defaultKeyStatistics', 'sharesShortPreviousMonthDate', 'raw'),
        'shares_short_interest': try_to_get(data, 'defaultKeyStatistics', 'dateShortInterest', 'raw'),
        'shares_percent_shares_out': try_to_get(data, 'defaultKeyStatistics', 'sharesPercentSharesOut', 'raw'),
        'held_percent_insiders': try_to_get(data, 'defaultKeyStatistics', 'heldPercentInsiders', 'raw'),
        'held_percent_institutions': try_to_get(data, 'defaultKeyStatistics', 'heldPercentInstitutions', 'raw'),
        'short_ratio': try_to_get(data, 'defaultKeyStatistics', 'shortRatio', 'raw'),
        'short_percent_of_float': try_to_get(data, 'defaultKeyStatistics', 'shortPercentOfFloat', 'raw'),
        'beta': try_to_get(data, 'defaultKeyStatistics', 'beta', 'raw'),
        'implied_shares_outstanding': try_to_get(data, 'defaultKeyStatistics', 'impliedSharesOutstanding'),
        'morningstar_overall_rating': try_to_get(data, 'defaultKeyStatistics', 'morningStarOverallRating'),
        'morningstar_risk_rating': try_to_get(data, 'defaultKeyStatistics', 'morningStarRiskRating'),
    }

    '''
            "category": null,
            "bookValue": {
                "raw": 25.207,
            },
            "priceToBook": {
                "raw": 31.133217,
            },
            "annualReportExpenseRatio": {},
            "ytdReturn": {},
            "beta3Year": {},
            "totalAssets": {},
            "yield": {},
            "fundFamily": null,
            "fundInceptionDate": {},
            "legalType": null,
            "threeYearAverageReturn": {},
            "fiveYearAverageReturn": {},
            "priceToSalesTrailing12Months": {},
            "lastFiscalYearEnd": {
                "raw": 1609372800,
            },
            "nextFiscalYearEnd": {
                "raw": 1672444800,
            },
            "mostRecentQuarter": {
                "raw": 1625011200,
            },
            "earningsQuarterlyGrowth": {
                "raw": 9.981,
            },
            "revenueQuarterlyGrowth": {},
            "netIncomeToCommon": {
                "raw": 2150000128,
            },
            "trailingEps": {
                "raw": 1.897,
            },
            "forwardEps": {
                "raw": 7.11,
            },
            "pegRatio": {
                "raw": 2.67,
            },
            "lastSplitFactor": null,
            "lastSplitDate": {},
            "enterpriseToRevenue": {
                "raw": 18.228,
            },
            "enterpriseToEbitda": {
                "raw": 132.68,
            },
            "52WeekChange": {
                "raw": 0.8883718,
            },
            "SandP52WeekChange": {
                "raw": 0.33207917,
            },
            "lastDividendValue": {},
            "lastDividendDate": {},
            "lastCapGain": {},
            "annualHoldingsTurnover": {}
        },
        "incomeStatementHistory": {
            "incomeStatementHistory": [
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1609372800,
                    },
                    "totalRevenue": {
                        "raw": 31536000000,
                    },
                    "costOfRevenue": {
                        "raw": 24906000000,
                    },
                    "grossProfit": {
                        "raw": 6630000000,
                    },
                    "researchDevelopment": {
                        "raw": 1491000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 3188000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {},
                    "totalOperatingExpenses": {
                        "raw": 29585000000,
                    },
                    "operatingIncome": {
                        "raw": 1951000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -797000000,
                    },
                    "ebit": {
                        "raw": 1951000000,
                    },
                    "interestExpense": {
                        "raw": -784000000,
                    },
                    "incomeBeforeTax": {
                        "raw": 1154000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 292000000,
                    },
                    "minorityInterest": {
                        "raw": 1454000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": 862000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": 721000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": 690000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1577750400,
                    },
                    "totalRevenue": {
                        "raw": 24578000000,
                    },
                    "costOfRevenue": {
                        "raw": 20509000000,
                    },
                    "grossProfit": {
                        "raw": 4069000000,
                    },
                    "researchDevelopment": {
                        "raw": 1343000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 2646000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {},
                    "totalOperatingExpenses": {
                        "raw": 24498000000,
                    },
                    "operatingIncome": {
                        "raw": 80000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -745000000,
                    },
                    "ebit": {
                        "raw": 80000000,
                    },
                    "interestExpense": {
                        "raw": -725000000,
                    },
                    "incomeBeforeTax": {
                        "raw": -665000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 110000000,
                    },
                    "minorityInterest": {
                        "raw": 1492000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": -775000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": -862000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": -870000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1546214400,
                    },
                    "totalRevenue": {
                        "raw": 21461000000,
                    },
                    "costOfRevenue": {
                        "raw": 17419000000,
                    },
                    "grossProfit": {
                        "raw": 4042000000,
                    },
                    "researchDevelopment": {
                        "raw": 1460000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 2835000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {},
                    "totalOperatingExpenses": {
                        "raw": 21714000000,
                    },
                    "operatingIncome": {
                        "raw": -253000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -752000000,
                    },
                    "ebit": {
                        "raw": -253000000,
                    },
                    "interestExpense": {
                        "raw": -653000000,
                    },
                    "incomeBeforeTax": {
                        "raw": -1005000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 58000000,
                    },
                    "minorityInterest": {
                        "raw": 1390000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": -1063000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": -976000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": -976000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1514678400,
                    },
                    "totalRevenue": {
                        "raw": 11759000000,
                    },
                    "costOfRevenue": {
                        "raw": 9536000000,
                    },
                    "grossProfit": {
                        "raw": 2223000000,
                    },
                    "researchDevelopment": {
                        "raw": 1378000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 2477000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {},
                    "totalOperatingExpenses": {
                        "raw": 13391000000,
                    },
                    "operatingIncome": {
                        "raw": -1632000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -577000000,
                    },
                    "ebit": {
                        "raw": -1632000000,
                    },
                    "interestExpense": {
                        "raw": -477000000,
                    },
                    "incomeBeforeTax": {
                        "raw": -2209000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 32000000,
                    },
                    "minorityInterest": {
                        "raw": 1395080000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": -2241000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": -1962000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": -1962000000,
                    }
                }
            ],
            "maxAge": 86400
        },
        "summaryDetail": {
            "maxAge": 1,
            "priceHint": {
                "raw": 2,
            },
            "previousClose": {
                "raw": 791.36,
            },
            "open": {
                "raw": 787.2,
            },
            "dayLow": {
                "raw": 776.55,
            },
            "dayHigh": {
                "raw": 795.64,
            },
            "regularMarketPreviousClose": {
                "raw": 791.36,
            },
            "regularMarketOpen": {
                "raw": 787.2,
            },
            "regularMarketDayLow": {
                "raw": 776.55,
            },
            "regularMarketDayHigh": {
                "raw": 795.64,
            },
            "dividendRate": {},
            "dividendYield": {},
            "exDividendDate": {},
            "payoutRatio": {
                "raw": 0.0,
            },
            "fiveYearAvgDividendYield": {},
            "beta": {
                "raw": 1.961244,
            },
            "trailingPE": {
                "raw": 413.6927,
            },
            "forwardPE": {
                "raw": 110.37623,
            },
            "volume": {
                "raw": 9241253,
            },
            "regularMarketVolume": {
                "raw": 9241253,
            },
            "averageVolume": {
                "raw": 18955229,
            },
            "averageVolume10days": {
                "raw": 19582600,
            },
            "averageDailyVolume10Day": {
                "raw": 19582600,
            },
            "bid": {
                "raw": 783.56,
            },
            "ask": {
                "raw": 784.79,
            },
            "bidSize": {
                "raw": 1200,
            },
            "askSize": {
                "raw": 900,
            },
            "marketCap": {
                "raw": 786164088832,
            },
        "calendarEvents": {
            "maxAge": 1,
            "earnings": {
                "earningsDate": [
                    {
                        "raw": 1634641140,
                    },
                    {
                        "raw": 1635163200,
                    }
                ],
                "earningsAverage": {
                    "raw": 1.4,
                },
                "earningsLow": {
                    "raw": 0.93,
                },
                "earningsHigh": {
                    "raw": 1.91,
                },
                "revenueAverage": {
                    "raw": 13147100000,
                },
                "revenueLow": {
                    "raw": 11708000000,
                },
                "revenueHigh": {
                    "raw": 15805400000,
                }
            },
            "exDividendDate": {},
            "dividendDate": {}
        },
        "price": {
            "maxAge": 1,
            "preMarketChangePercent": {
                "raw": -0.00515563,
            },
            "preMarketChange": {
                "raw": -4.07996,
            },
            "preMarketTime": 1632835799,
            "preMarketPrice": {
                "raw": 787.28,
            },
            "preMarketSource": "FREE_REALTIME",
            "postMarketChange": {},
            "postMarketPrice": {},
            "regularMarketChangePercent": {
                "raw": -0.008321069,
            },
            "regularMarketChange": {
                "raw": -6.584961,
            },
            "regularMarketTime": 1632840779,
            "priceHint": {
                "raw": 2,
            },
            "regularMarketPrice": {
                "raw": 784.775,
            },
            "regularMarketDayHigh": {
                "raw": 795.64,
            },
            "regularMarketDayLow": {
                "raw": 776.55,
            },
            "regularMarketVolume": {
                "raw": 9241253,
            },
            "averageDailyVolume10Day": {
                "raw": 19582600,
            },
            "averageDailyVolume3Month": {
                "raw": 18955229,
            },
            "regularMarketPreviousClose": {
                "raw": 791.36,
            },
            "regularMarketSource": "FREE_REALTIME",
            "regularMarketOpen": {
                "raw": 787.2,
            },
            "strikePrice": {},
            "openInterest": {},
            "exchange": "NMS",
            "exchangeName": "NasdaqGS",
            "exchangeDataDelayedBy": 0,
            "marketState": "REGULAR",
            "quoteType": "EQUITY",
            "symbol": "TSLA",
            "underlyingSymbol": null,
            "shortName": "Tesla, Inc.",
            "longName": "Tesla, Inc.",
            "currency": "USD",
            "quoteSourceName": "Nasdaq Real Time Price",
            "currencySymbol": "$",
            "fromCurrency": null,
            "toCurrency": null,
            "lastMarket": null,
            "volume24Hr": {},
            "volumeAllCurrencies": {},
            "circulatingSupply": {},
            "marketCap": {
                "raw": 786164088832,
            }
        },
        "balanceSheetHistory": {
            "balanceSheetStatements": [
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1609372800,
                    },
                    "cash": {
                        "raw": 19384000000,
                    },
                    "netReceivables": {
                        "raw": 1903000000,
                    },
                    "inventory": {
                        "raw": 4101000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 238000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 26717000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 23375000000,
                    },
                    "goodWill": {
                        "raw": 207000000,
                    },
                    "intangibleAssets": {
                        "raw": 313000000,
                    },
                    "otherAssets": {
                        "raw": 1536000000,
                    },
                    "totalAssets": {
                        "raw": 52148000000,
                    },
                    "accountsPayable": {
                        "raw": 6051000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 1758000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 4147000000,
                    },
                    "longTermDebt": {
                        "raw": 8571000000,
                    },
                    "otherLiab": {
                        "raw": 3302000000,
                    },
                    "minorityInterest": {
                        "raw": 1454000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 14248000000,
                    },
                    "totalLiab": {
                        "raw": 28469000000,
                    },
                    "commonStock": {
                        "raw": 1000000,
                    },
                    "retainedEarnings": {
                        "raw": -5399000000,
                    },
                    "treasuryStock": {
                        "raw": 363000000,
                    },
                    "capitalSurplus": {
                        "raw": 27260000000,
                    },
                    "otherStockholderEquity": {
                        "raw": 363000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 22225000000,
                    },
                    "netTangibleAssets": {
                        "raw": 21705000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1577750400,
                    },
                    "cash": {
                        "raw": 6268000000,
                    },
                    "netReceivables": {
                        "raw": 1324000000,
                    },
                    "inventory": {
                        "raw": 3552000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 246000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 12103000000,
                    },
                    "longTermInvestments": {
                        "raw": 1000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 20199000000,
                    },
                    "goodWill": {
                        "raw": 198000000,
                    },
                    "intangibleAssets": {
                        "raw": 339000000,
                    },
                    "otherAssets": {
                        "raw": 1469000000,
                    },
                    "totalAssets": {
                        "raw": 34309000000,
                    },
                    "accountsPayable": {
                        "raw": 3771000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 1399000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 3693000000,
                    },
                    "longTermDebt": {
                        "raw": 10375000000,
                    },
                    "otherLiab": {
                        "raw": 2969000000,
                    },
                    "minorityInterest": {
                        "raw": 1492000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 10667000000,
                    },
                    "totalLiab": {
                        "raw": 26199000000,
                    },
                    "commonStock": {
                        "raw": 1000000,
                    },
                    "retainedEarnings": {
                        "raw": -6083000000,
                    },
                    "treasuryStock": {
                        "raw": -36000000,
                    },
                    "capitalSurplus": {
                        "raw": 12736000000,
                    },
                    "otherStockholderEquity": {
                        "raw": -36000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 6618000000,
                    },
                    "netTangibleAssets": {
                        "raw": 6081000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1546214400,
                    },
                    "cash": {
                        "raw": 3686000000,
                    },
                    "netReceivables": {
                        "raw": 949000000,
                    },
                    "inventory": {
                        "raw": 3113000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 193000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 8307000000,
                    },
                    "longTermInvestments": {
                        "raw": 12000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 19691000000,
                    },
                    "goodWill": {
                        "raw": 68000000,
                    },
                    "intangibleAssets": {
                        "raw": 282000000,
                    },
                    "otherAssets": {
                        "raw": 1380000000,
                    },
                    "totalAssets": {
                        "raw": 29740000000,
                    },
                    "accountsPayable": {
                        "raw": 3405000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 2284000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 2955000000,
                    },
                    "longTermDebt": {
                        "raw": 8461000000,
                    },
                    "otherLiab": {
                        "raw": 2318000000,
                    },
                    "minorityInterest": {
                        "raw": 1390000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 9993000000,
                    },
                    "totalLiab": {
                        "raw": 23427000000,
                    },
                    "retainedEarnings": {
                        "raw": -5318000000,
                    },
                    "treasuryStock": {
                        "raw": -8000000,
                    },
                    "capitalSurplus": {
                        "raw": 10249000000,
                    },
                    "otherStockholderEquity": {
                        "raw": -8000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 4923000000,
                    },
                    "netTangibleAssets": {
                        "raw": 4573000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1514678400,
                    },
                    "cash": {
                        "raw": 3367914000,
                    },
                    "netReceivables": {
                        "raw": 515381000,
                    },
                    "inventory": {
                        "raw": 2263537000,
                    },
                    "otherCurrentAssets": {
                        "raw": 155323000,
                    },
                    "totalCurrentAssets": {
                        "raw": 6570520000,
                    },
                    "longTermInvestments": {
                        "raw": 5304000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 20491616000,
                    },
                    "goodWill": {
                        "raw": 60237000,
                    },
                    "intangibleAssets": {
                        "raw": 361502000,
                    },
                    "otherAssets": {
                        "raw": 1166193000,
                    },
                    "totalAssets": {
                        "raw": 28655372000,
                    },
                    "accountsPayable": {
                        "raw": 2390250000,
                    },
                    "shortLongTermDebt": {
                        "raw": 963932000,
                    },
                    "otherCurrentLiab": {
                        "raw": 3098379000,
                    },
                    "longTermDebt": {
                        "raw": 9486248000,
                    },
                    "otherLiab": {
                        "raw": 4196294000,
                    },
                    "minorityInterest": {
                        "raw": 1395080000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 7674740000,
                    },
                    "totalLiab": {
                        "raw": 23023050000,
                    },
                    "commonStock": {
                        "raw": 169000,
                    },
                    "retainedEarnings": {
                        "raw": -4974299000,
                    },
                    "treasuryStock": {
                        "raw": 33348000,
                    },
                    "capitalSurplus": {
                        "raw": 9178024000,
                    },
                    "otherStockholderEquity": {
                        "raw": 33348000,
                    },
                    "totalStockholderEquity": {
                        "raw": 4237242000,
                    },
                    "netTangibleAssets": {
                        "raw": 3815503000,
                    }
                }
            ],
            "maxAge": 86400
        },
        "earningsTrend": {
            "trend": [
                {
                    "maxAge": 1,
                    "period": "0q",
                    "endDate": "2021-09-30",
                    "growth": {
                        "raw": 0.84199995,
                    },
                    "earningsEstimate": {
                        "avg": {
                            "raw": 1.4,
                        },
                        "low": {
                            "raw": 0.93,
                        },
                        "high": {
                            "raw": 1.91,
                        },
                        "yearAgoEps": {
                            "raw": 0.76,
                        },
                        "numberOfAnalysts": {
                            "raw": 22,
                        },
                        "growth": {
                            "raw": 0.84199995,
                        }
                    },
                    "revenueEstimate": {
                        "avg": {
                            "raw": 13147100000,
                        },
                        "low": {
                            "raw": 11708000000,
                        },
                        "high": {
                            "raw": 15805400000,
                        },
                        "numberOfAnalysts": {
                            "raw": 22,
                        },
                        "yearAgoRevenue": {
                            "raw": 8771000000,
                        },
                        "growth": {
                            "raw": 0.499,
                        }
                    },
                    "epsTrend": {
                        "current": {
                            "raw": 1.4,
                        },
                        "7daysAgo": {
                            "raw": 1.39,
                        },
                        "30daysAgo": {
                            "raw": 1.38,
                        },
                        "60daysAgo": {
                            "raw": 1.2,
                        },
                        "90daysAgo": {
                            "raw": 1.18,
                        }
                    },
                    "epsRevisions": {
                        "upLast7days": {
                            "raw": 0,
                        },
                        "upLast30days": {
                            "raw": 1,
                        },
                        "downLast30days": {
                            "raw": 0,
                        },
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "+1q",
                    "endDate": "2021-12-31",
                    "growth": {
                        "raw": 1.05,
                    },
                    "earningsEstimate": {
                        "avg": {
                            "raw": 1.64,
                        },
                        "low": {
                            "raw": 0.84,
                        },
                        "high": {
                            "raw": 2.42,
                        },
                        "yearAgoEps": {
                            "raw": 0.8,
                        },
                        "numberOfAnalysts": {
                            "raw": 21,
                        },
                        "growth": {
                            "raw": 1.05,
                        }
                    },
                    "revenueEstimate": {
                        "avg": {
                            "raw": 14795000000,
                        },
                        "low": {
                            "raw": 12622800000,
                        },
                        "high": {
                            "raw": 17534400000,
                        },
                        "numberOfAnalysts": {
                            "raw": 21,
                        },
                        "yearAgoRevenue": {
                            "raw": 10744000000,
                        },
                        "growth": {
                            "raw": 0.377,
                        }
                    },
                    "epsTrend": {
                        "current": {
                            "raw": 1.64,
                        },
                        "7daysAgo": {
                            "raw": 1.62,
                        },
                        "30daysAgo": {
                            "raw": 1.62,
                        },
                        "60daysAgo": {
                            "raw": 1.42,
                        },
                        "90daysAgo": {
                            "raw": 1.42,
                        }
                    },
                    "epsRevisions": {
                        "upLast7days": {
                            "raw": 0,
                        },
                        "upLast30days": {
                            "raw": 1,
                        },
                        "downLast30days": {
                            "raw": 0,
                        },
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "0y",
                    "endDate": "2021-12-31",
                    "growth": {
                        "raw": 1.371,
                    },
                    "earningsEstimate": {
                        "avg": {
                            "raw": 5.31,
                        },
                        "low": {
                            "raw": 3.58,
                        },
                        "high": {
                            "raw": 6.7,
                        },
                        "yearAgoEps": {
                            "raw": 2.24,
                        },
                        "numberOfAnalysts": {
                            "raw": 32,
                        },
                        "growth": {
                            "raw": 1.371,
                        }
                    },
                    "revenueEstimate": {
                        "avg": {
                            "raw": 50121700000,
                        },
                        "low": {
                            "raw": 40325800000,
                        },
                        "high": {
                            "raw": 54932100000,
                        },
                        "numberOfAnalysts": {
                            "raw": 39,
                        },
                        "yearAgoRevenue": {
                            "raw": 31536000000,
                        },
                        "growth": {
                            "raw": 0.589,
                        }
                    },
                    "epsTrend": {
                        "current": {
                            "raw": 5.31,
                        },
                        "7daysAgo": {
                            "raw": 5.27,
                        },
                        "30daysAgo": {
                            "raw": 5.27,
                        },
                        "60daysAgo": {
                            "raw": 4.52,
                        },
                        "90daysAgo": {
                            "raw": 4.53,
                        }
                    },
                    "epsRevisions": {
                        "upLast7days": {
                            "raw": 1,
                        },
                        "upLast30days": {
                            "raw": 3,
                        },
                        "downLast30days": {
                            "raw": 0,
                        },
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "+1y",
                    "endDate": "2022-12-31",
                    "growth": {
                        "raw": 0.33900002,
                    },
                    "earningsEstimate": {
                        "avg": {
                            "raw": 7.11,
                        },
                        "low": {
                            "raw": 4.25,
                        },
                        "high": {
                            "raw": 10.0,
                        },
                        "yearAgoEps": {
                            "raw": 5.31,
                        },
                        "numberOfAnalysts": {
                            "raw": 30,
                        },
                        "growth": {
                            "raw": 0.33900002,
                        }
                    },
                    "revenueEstimate": {
                        "avg": {
                            "raw": 67410100000,
                        },
                        "low": {
                            "raw": 52796000000,
                        },
                        "high": {
                            "raw": 78825000000,
                        },
                        "numberOfAnalysts": {
                            "raw": 36,
                        },
                        "yearAgoRevenue": {
                            "raw": 50121700000,
                        },
                        "growth": {
                            "raw": 0.345,
                        }
                    },
                    "epsTrend": {
                        "current": {
                            "raw": 7.11,
                        },
                        "7daysAgo": {
                            "raw": 7.07,
                        },
                        "30daysAgo": {
                            "raw": 6.97,
                        },
                        "60daysAgo": {
                            "raw": 6.21,
                        },
                        "90daysAgo": {
                            "raw": 6.22,
                        }
                    },
                    "epsRevisions": {
                        "upLast7days": {
                            "raw": 0,
                        },
                        "upLast30days": {
                            "raw": 2,
                        },
                        "downLast30days": {
                            "raw": 1,
                        },
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "+5y",
                    "endDate": null,
                    "growth": {
                        "raw": 0.5175,
                    },
                    "earningsEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "yearAgoEps": {},
                        "numberOfAnalysts": {},
                        "growth": {}
                    },
                    "revenueEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "numberOfAnalysts": {},
                        "yearAgoRevenue": {},
                        "growth": {}
                    },
                    "epsTrend": {
                        "current": {},
                        "7daysAgo": {},
                        "30daysAgo": {},
                        "60daysAgo": {},
                        "90daysAgo": {}
                    },
                    "epsRevisions": {
                        "upLast7days": {},
                        "upLast30days": {},
                        "downLast30days": {},
                        "downLast90days": {}
                    }
                },
                {
                    "maxAge": 1,
                    "period": "-5y",
                    "endDate": null,
                    "growth": {},
                    "earningsEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "yearAgoEps": {},
                        "numberOfAnalysts": {},
                        "growth": {}
                    },
                    "revenueEstimate": {
                        "avg": {},
                        "low": {},
                        "high": {},
                        "numberOfAnalysts": {},
                        "yearAgoRevenue": {},
                        "growth": {}
                    },
                    "epsTrend": {
                        "current": {},
                        "7daysAgo": {},
                        "30daysAgo": {},
                        "60daysAgo": {},
                        "90daysAgo": {}
                    },
                    "epsRevisions": {
                        "upLast7days": {},
                        "upLast30days": {},
                        "downLast30days": {},
                        "downLast90days": {}
                    }
                }
            ],
            "maxAge": 1
        },
        "majorHoldersBreakdown": {
            "maxAge": 1,
            "insidersPercentHeld": {
                "raw": 0.18962,
            },
            "institutionsPercentHeld": {
                "raw": 0.41364,
            },
            "institutionsFloatPercentHeld": {
                "raw": 0.51042,
            },
            "institutionsCount": {
                "raw": 2713,
            }
        },
        "balanceSheetHistoryQuarterly": {
            "balanceSheetStatements": [
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1625011200,
                    },
                    "cash": {
                        "raw": 16229000000,
                    },
                    "netReceivables": {
                        "raw": 2159000000,
                    },
                    "inventory": {
                        "raw": 4733000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 326000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 24693000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 27030000000,
                    },
                    "goodWill": {
                        "raw": 203000000,
                    },
                    "intangibleAssets": {
                        "raw": 283000000,
                    },
                    "otherAssets": {
                        "raw": 2937000000,
                    },
                    "totalAssets": {
                        "raw": 55146000000,
                    },
                    "accountsPayable": {
                        "raw": 7558000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 1082000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 4621000000,
                    },
                    "longTermDebt": {
                        "raw": 6915000000,
                    },
                    "otherLiab": {
                        "raw": 3210000000,
                    },
                    "minorityInterest": {
                        "raw": 1446000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 16371000000,
                    },
                    "totalLiab": {
                        "raw": 28896000000,
                    },
                    "commonStock": {
                        "raw": 1000000,
                    },
                    "retainedEarnings": {
                        "raw": -3608000000,
                    },
                    "treasuryStock": {
                        "raw": 206000000,
                    },
                    "capitalSurplus": {
                        "raw": 28205000000,
                    },
                    "otherStockholderEquity": {
                        "raw": 206000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 24804000000,
                    },
                    "netTangibleAssets": {
                        "raw": 24318000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1617148800,
                    },
                    "cash": {
                        "raw": 17141000000,
                    },
                    "netReceivables": {
                        "raw": 1913000000,
                    },
                    "inventory": {
                        "raw": 4132000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 305000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 24705000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 24844000000,
                    },
                    "goodWill": {
                        "raw": 206000000,
                    },
                    "intangibleAssets": {
                        "raw": 299000000,
                    },
                    "otherAssets": {
                        "raw": 2918000000,
                    },
                    "totalAssets": {
                        "raw": 52972000000,
                    },
                    "accountsPayable": {
                        "raw": 6648000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 1415000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 4412000000,
                    },
                    "longTermDebt": {
                        "raw": 8019000000,
                    },
                    "otherLiab": {
                        "raw": 3247000000,
                    },
                    "minorityInterest": {
                        "raw": 1448000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 14877000000,
                    },
                    "totalLiab": {
                        "raw": 28507000000,
                    },
                    "commonStock": {
                        "raw": 1000000,
                    },
                    "retainedEarnings": {
                        "raw": -4750000000,
                    },
                    "treasuryStock": {
                        "raw": 143000000,
                    },
                    "capitalSurplus": {
                        "raw": 27623000000,
                    },
                    "otherStockholderEquity": {
                        "raw": 143000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 23017000000,
                    },
                    "netTangibleAssets": {
                        "raw": 22512000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1609372800,
                    },
                    "cash": {
                        "raw": 19384000000,
                    },
                    "netReceivables": {
                        "raw": 1903000000,
                    },
                    "inventory": {
                        "raw": 4101000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 238000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 26717000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 23375000000,
                    },
                    "goodWill": {
                        "raw": 207000000,
                    },
                    "intangibleAssets": {
                        "raw": 313000000,
                    },
                    "otherAssets": {
                        "raw": 1536000000,
                    },
                    "totalAssets": {
                        "raw": 52148000000,
                    },
                    "accountsPayable": {
                        "raw": 6051000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 1758000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 4147000000,
                    },
                    "longTermDebt": {
                        "raw": 8571000000,
                    },
                    "otherLiab": {
                        "raw": 3302000000,
                    },
                    "minorityInterest": {
                        "raw": 1454000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 14248000000,
                    },
                    "totalLiab": {
                        "raw": 28469000000,
                    },
                    "commonStock": {
                        "raw": 1000000,
                    },
                    "retainedEarnings": {
                        "raw": -5399000000,
                    },
                    "treasuryStock": {
                        "raw": 363000000,
                    },
                    "capitalSurplus": {
                        "raw": 27260000000,
                    },
                    "otherStockholderEquity": {
                        "raw": 363000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 22225000000,
                    },
                    "netTangibleAssets": {
                        "raw": 21705000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1601424000,
                    },
                    "cash": {
                        "raw": 14531000000,
                    },
                    "netReceivables": {
                        "raw": 1766000000,
                    },
                    "inventory": {
                        "raw": 4218000000,
                    },
                    "otherCurrentAssets": {
                        "raw": 174000000,
                    },
                    "totalCurrentAssets": {
                        "raw": 21744000000,
                    },
                    "propertyPlantEquipment": {
                        "raw": 21990000000,
                    },
                    "goodWill": {
                        "raw": 203000000,
                    },
                    "intangibleAssets": {
                        "raw": 318000000,
                    },
                    "otherAssets": {
                        "raw": 1436000000,
                    },
                    "totalAssets": {
                        "raw": 45691000000,
                    },
                    "accountsPayable": {
                        "raw": 4958000000,
                    },
                    "shortLongTermDebt": {
                        "raw": 2814000000,
                    },
                    "otherCurrentLiab": {
                        "raw": 3655000000,
                    },
                    "longTermDebt": {
                        "raw": 9506000000,
                    },
                    "otherLiab": {
                        "raw": 3151000000,
                    },
                    "minorityInterest": {
                        "raw": 1469000000,
                    },
                    "totalCurrentLiabilities": {
                        "raw": 13302000000,
                    },
                    "totalLiab": {
                        "raw": 28191000000,
                    },
                    "commonStock": {
                        "raw": 1000000,
                    },
                    "retainedEarnings": {
                        "raw": -5669000000,
                    },
                    "treasuryStock": {
                        "raw": 125000000,
                    },
                    "capitalSurplus": {
                        "raw": 21574000000,
                    },
                    "otherStockholderEquity": {
                        "raw": 125000000,
                    },
                    "totalStockholderEquity": {
                        "raw": 16031000000,
                    },
                    "netTangibleAssets": {
                        "raw": 15510000000,
                    }
                }
            ],
            "maxAge": 86400
        },
        "earningsHistory": {
            "history": [
                {
                    "maxAge": 1,
                    "epsActual": {
                        "raw": 0.76,
                    },
                    "epsEstimate": {
                        "raw": 0.58,
                    },
                    "epsDifference": {
                        "raw": 0.18,
                    },
                    "surprisePercent": {
                        "raw": 0.31,
                    },
                    "quarter": {
                        "raw": 1601424000,
                    },
                    "period": "-4q"
                },
                {
                    "maxAge": 1,
                    "epsActual": {
                        "raw": 0.8,
                    },
                    "epsEstimate": {
                        "raw": 1.03,
                    },
                    "epsDifference": {
                        "raw": -0.23,
                    },
                    "surprisePercent": {
                        "raw": -0.22299999,
                    },
                    "quarter": {
                        "raw": 1609372800,
                    },
                    "period": "-3q"
                },
                {
                    "maxAge": 1,
                    "epsActual": {
                        "raw": 0.93,
                    },
                    "epsEstimate": {
                        "raw": 0.79,
                    },
                    "epsDifference": {
                        "raw": 0.14,
                    },
                    "surprisePercent": {
                        "raw": 0.177,
                    },
                    "quarter": {
                        "raw": 1617148800,
                    },
                    "period": "-2q"
                },
                {
                    "maxAge": 1,
                    "epsActual": {
                        "raw": 1.45,
                    },
                    "epsEstimate": {
                        "raw": 0.98,
                    },
                    "epsDifference": {
                        "raw": 0.47,
                    },
                    "surprisePercent": {
                        "raw": 0.48,
                    },
                    "quarter": {
                        "raw": 1625011200,
                    },
                    "period": "-1q"
                }
            ],
            "maxAge": 86400
        },
        "majorDirectHolders": {
            "holders": [],
            "maxAge": 1
        },
        "esgScores": {
            "maxAge": 86400,
            "totalEsg": {
                "raw": 30.46,
            },
            "environmentScore": {
                "raw": 2.95,
            },
            "socialScore": {
                "raw": 17.31,
            },
            "governanceScore": {
                "raw": 10.2,
            },
            "ratingYear": 2021,
            "ratingMonth": 9,
            "highestControversy": 3.0,
            "peerCount": 37,
            "esgPerformance": "OUT_PERF",
            "peerGroup": "Automobiles",
            "relatedControversy": [
                "Employee Incidents",
                "Governance Incidents"
            ],
            "peerEsgScorePerformance": {
                "min": 12.42,
                "avg": 25.961081081081087,
                "max": 35.93
            },
            "peerGovernancePerformance": {
                "min": 5.85,
                "avg": 8.547837837837838,
                "max": 11.28
            },
            "peerSocialPerformance": {
                "min": 3.39,
                "avg": 10.48756756756757,
                "max": 17.31
            },
            "peerEnvironmentPerformance": {
                "min": 2.09,
                "avg": 6.925945945945946,
                "max": 10.28
            },
            "peerHighestControversyPerformance": {
                "min": 0.0,
                "avg": 2.4054054054054053,
                "max": 4.0
            },
            "percentile": {
                "raw": 61.16,
            },
            "environmentPercentile": null,
            "socialPercentile": null,
            "governancePercentile": null,
            "adult": false,
            "alcoholic": false,
            "animalTesting": false,
            "catholic": false,
            "controversialWeapons": false,
            "smallArms": false,
            "furLeather": false,
            "gambling": false,
            "gmo": false,
            "militaryContract": false,
            "nuclear": false,
            "pesticides": false,
            "palmOil": false,
            "coal": false,
            "tobacco": false
        },
        "incomeStatementHistoryQuarterly": {
            "incomeStatementHistory": [
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1625011200,
                    },
                    "totalRevenue": {
                        "raw": 11958000000,
                    },
                    "costOfRevenue": {
                        "raw": 9074000000,
                    },
                    "grossProfit": {
                        "raw": 2884000000,
                    },
                    "researchDevelopment": {
                        "raw": 576000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 973000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {
                        "raw": 23000000,
                    },
                    "totalOperatingExpenses": {
                        "raw": 10646000000,
                    },
                    "operatingIncome": {
                        "raw": 1312000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -19000000,
                    },
                    "ebit": {
                        "raw": 1312000000,
                    },
                    "interestExpense": {
                        "raw": -84000000,
                    },
                    "incomeBeforeTax": {
                        "raw": 1293000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 115000000,
                    },
                    "minorityInterest": {
                        "raw": 1446000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": 1178000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": 1142000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": 1142000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1617148800,
                    },
                    "totalRevenue": {
                        "raw": 10389000000,
                    },
                    "costOfRevenue": {
                        "raw": 8174000000,
                    },
                    "grossProfit": {
                        "raw": 2215000000,
                    },
                    "researchDevelopment": {
                        "raw": 666000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 1056000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {
                        "raw": -101000000,
                    },
                    "totalOperatingExpenses": {
                        "raw": 9795000000,
                    },
                    "operatingIncome": {
                        "raw": 594000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -61000000,
                    },
                    "ebit": {
                        "raw": 594000000,
                    },
                    "interestExpense": {
                        "raw": -79000000,
                    },
                    "incomeBeforeTax": {
                        "raw": 533000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 69000000,
                    },
                    "minorityInterest": {
                        "raw": 1448000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": 464000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": 438000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": 438000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1609372800,
                    },
                    "totalRevenue": {
                        "raw": 10744000000,
                    },
                    "costOfRevenue": {
                        "raw": 8678000000,
                    },
                    "grossProfit": {
                        "raw": 2066000000,
                    },
                    "researchDevelopment": {
                        "raw": 522000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 969000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {
                        "raw": -101000000,
                    },
                    "totalOperatingExpenses": {
                        "raw": 10169000000,
                    },
                    "operatingIncome": {
                        "raw": 575000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -196000000,
                    },
                    "ebit": {
                        "raw": 575000000,
                    },
                    "interestExpense": {
                        "raw": -241000000,
                    },
                    "incomeBeforeTax": {
                        "raw": 379000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 83000000,
                    },
                    "minorityInterest": {
                        "raw": 1454000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": 296000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": 270000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": 270000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1601424000,
                    },
                    "totalRevenue": {
                        "raw": 8771000000,
                    },
                    "costOfRevenue": {
                        "raw": 6708000000,
                    },
                    "grossProfit": {
                        "raw": 2063000000,
                    },
                    "researchDevelopment": {
                        "raw": 366000000,
                    },
                    "sellingGeneralAdministrative": {
                        "raw": 931000000,
                    },
                    "nonRecurring": {},
                    "otherOperatingExpenses": {
                        "raw": -101000000,
                    },
                    "totalOperatingExpenses": {
                        "raw": 8005000000,
                    },
                    "operatingIncome": {
                        "raw": 766000000,
                    },
                    "totalOtherIncomeExpenseNet": {
                        "raw": -211000000,
                    },
                    "ebit": {
                        "raw": 766000000,
                    },
                    "interestExpense": {
                        "raw": -162000000,
                    },
                    "incomeBeforeTax": {
                        "raw": 555000000,
                    },
                    "incomeTaxExpense": {
                        "raw": 186000000,
                    },
                    "minorityInterest": {
                        "raw": 1469000000,
                    },
                    "netIncomeFromContinuingOps": {
                        "raw": 369000000,
                    },
                    "discontinuedOperations": {},
                    "extraordinaryItems": {},
                    "effectOfAccountingCharges": {},
                    "otherItems": {},
                    "netIncome": {
                        "raw": 331000000,
                    },
                    "netIncomeApplicableToCommonShares": {
                        "raw": 300000000,
                    }
                }
            ],
            "maxAge": 86400
        },
        "cashflowStatementHistoryQuarterly": {
            "cashflowStatements": [
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1625011200,
                    },
                    "netIncome": {
                        "raw": 1142000000,
                    },
                    "depreciation": {
                        "raw": 681000000,
                    },
                    "changeToNetincome": {
                        "raw": 625000000,
                    },
                    "changeToAccountReceivables": {
                        "raw": -259000000,
                    },
                    "changeToLiabilities": {
                        "raw": 1037000000,
                    },
                    "changeToInventory": {
                        "raw": -581000000,
                    },
                    "changeToOperatingActivities": {
                        "raw": -521000000,
                    },
                    "totalCashFromOperatingActivities": {
                        "raw": 2124000000,
                    },
                    "capitalExpenditures": {
                        "raw": -1515000000,
                    },
                    "totalCashflowsFromInvestingActivities": {
                        "raw": -1515000000,
                    },
                    "netBorrowings": {
                        "raw": -1588000000,
                    },
                    "otherCashflowsFromFinancingActivities": {
                        "raw": -31000000,
                    },
                    "totalCashFromFinancingActivities": {
                        "raw": -1549000000,
                    },
                    "effectOfExchangeRate": {
                        "raw": 42000000,
                    },
                    "changeInCash": {
                        "raw": -898000000,
                    },
                    "issuanceOfStock": {
                        "raw": 70000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1617148800,
                    },
                    "netIncome": {
                        "raw": 438000000,
                    },
                    "depreciation": {
                        "raw": 621000000,
                    },
                    "changeToNetincome": {
                        "raw": 594000000,
                    },
                    "changeToAccountReceivables": {
                        "raw": -24000000,
                    },
                    "changeToLiabilities": {
                        "raw": 834000000,
                    },
                    "changeToInventory": {
                        "raw": -106000000,
                    },
                    "changeToOperatingActivities": {
                        "raw": -716000000,
                    },
                    "totalCashFromOperatingActivities": {
                        "raw": 1641000000,
                    },
                    "capitalExpenditures": {
                        "raw": -2860000000,
                    },
                    "otherCashflowsFromInvestingActivities": {
                        "raw": 6000000,
                    },
                    "totalCashflowsFromInvestingActivities": {
                        "raw": -2582000000,
                    },
                    "netBorrowings": {
                        "raw": -1162000000,
                    },
                    "otherCashflowsFromFinancingActivities": {
                        "raw": -37000000,
                    },
                    "totalCashFromFinancingActivities": {
                        "raw": -1016000000,
                    },
                    "effectOfExchangeRate": {
                        "raw": -221000000,
                    },
                    "changeInCash": {
                        "raw": -2178000000,
                    },
                    "issuanceOfStock": {
                        "raw": 183000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1609372800,
                    },
                    "netIncome": {
                        "raw": 270000000,
                    },
                    "depreciation": {
                        "raw": 618000000,
                    },
                    "changeToNetincome": {
                        "raw": 853000000,
                    },
                    "changeToAccountReceivables": {
                        "raw": -102000000,
                    },
                    "changeToLiabilities": {
                        "raw": 1540000000,
                    },
                    "changeToInventory": {
                        "raw": 180000000,
                    },
                    "changeToOperatingActivities": {
                        "raw": -376000000,
                    },
                    "totalCashFromOperatingActivities": {
                        "raw": 3019000000,
                    },
                    "capitalExpenditures": {
                        "raw": -1164000000,
                    },
                    "otherCashflowsFromInvestingActivities": {
                        "raw": 122000000,
                    },
                    "totalCashflowsFromInvestingActivities": {
                        "raw": -1047000000,
                    },
                    "netBorrowings": {
                        "raw": -2305000000,
                    },
                    "otherCashflowsFromFinancingActivities": {
                        "raw": -46000000,
                    },
                    "totalCashFromFinancingActivities": {
                        "raw": 2692000000,
                    },
                    "effectOfExchangeRate": {
                        "raw": 234000000,
                    },
                    "changeInCash": {
                        "raw": 4898000000,
                    },
                    "issuanceOfStock": {
                        "raw": 5043000000,
                    }
                },
                {
                    "maxAge": 1,
                    "endDate": {
                        "raw": 1601424000,
                    },
                    "netIncome": {
                        "raw": 331000000,
                    },
                    "depreciation": {
                        "raw": 584000000,
                    },
                    "changeToNetincome": {
                        "raw": 800000000,
                    },
                    "changeToAccountReceivables": {
                        "raw": -314000000,
                    },
                    "changeToLiabilities": {
                        "raw": 1275000000,
                    },
                    "changeToInventory": {
                        "raw": -67000000,
                    },
                    "changeToOperatingActivities": {
                        "raw": -259000000,
                    },
                    "totalCashFromOperatingActivities": {
                        "raw": 2400000000,
                    },
                    "capitalExpenditures": {
                        "raw": -1021000000,
                    },
                    "otherCashflowsFromInvestingActivities": {
                        "raw": 122000000,
                    },
                    "totalCashflowsFromInvestingActivities": {
                        "raw": -1039000000,
                    },
                    "netBorrowings": {
                        "raw": -581000000,
                    },
                    "otherCashflowsFromFinancingActivities": {
                        "raw": -86000000,
                    },
                    "totalCashFromFinancingActivities": {
                        "raw": 4450000000,
                    },
                    "effectOfExchangeRate": {
                        "raw": 86000000,
                    },
                    "changeInCash": {
                        "raw": 5897000000,
                    },
                    "issuanceOfStock": {
                        "raw": 5117000000,
                    }
                }
            ],
            "maxAge": 86400
        },
        "earnings": {
            "maxAge": 86400,
            "earningsChart": {
                "quarterly": [
                    {
                        "date": "3Q2020",
                        "actual": {
                            "raw": 0.76,
                        },
                        "estimate": {
                            "raw": 0.58,
                        }
                    },
                    {
                        "date": "4Q2020",
                        "actual": {
                            "raw": 0.8,
                        },
                        "estimate": {
                            "raw": 1.03,
                        }
                    },
                    {
                        "date": "1Q2021",
                        "actual": {
                            "raw": 0.93,
                        },
                        "estimate": {
                            "raw": 0.79,
                        }
                    },
                    {
                        "date": "2Q2021",
                        "actual": {
                            "raw": 1.45,
                        },
                        "estimate": {
                            "raw": 0.98,
                        }
                    }
                ],
                "currentQuarterEstimate": {
                    "raw": 1.4,
                },
                "currentQuarterEstimateDate": "3Q",
                "currentQuarterEstimateYear": 2021,
                "earningsDate": [
                    {
                        "raw": 1634641140,
                    },
                    {
                        "raw": 1635163200,
                    }
                ]
            },
            "financialsChart": {
                "yearly": [
                    {
                        "date": 2017,
                        "revenue": {
                            "raw": 11759000000,
                        },
                        "earnings": {
                            "raw": -1962000000,
                        }
                    },
                    {
                        "date": 2018,
                        "revenue": {
                            "raw": 21461000000,
                        },
                        "earnings": {
                            "raw": -976000000,
                        }
                    },
                    {
                        "date": 2019,
                        "revenue": {
                            "raw": 24578000000,
                        },
                        "earnings": {
                            "raw": -862000000,
                        }
                    },
                    {
                        "date": 2020,
                        "revenue": {
                            "raw": 31536000000,
                        },
                        "earnings": {
                            "raw": 721000000,
                        }
                    }
                ],
                "quarterly": [
                    {
                        "date": "3Q2020",
                        "revenue": {
                            "raw": 8771000000,
                        },
                        "earnings": {
                            "raw": 331000000,
                        }
                    },
                    {
                        "date": "4Q2020",
                        "revenue": {
                            "raw": 10744000000,
                        },
                        "earnings": {
                            "raw": 270000000,
                        }
                    },
                    {
                        "date": "1Q2021",
                        "revenue": {
                            "raw": 10389000000,
                        },
                        "earnings": {
                            "raw": 438000000,
                        }
                    },
                    {
                        "date": "2Q2021",
                        "revenue": {
                            "raw": 11958000000,
                        },
                        "earnings": {
                            "raw": 1142000000,
                        }
                    }
                ]
            },
            "financialCurrency": "USD"
        },
        "financialData": {
            "maxAge": 86400,
            "currentPrice": {
                "raw": 784.775,
            },
            "targetHighPrice": {
                "raw": 1591.0,
            },
            "targetLowPrice": {
                "raw": 67.0,
            },
            "targetMeanPrice": {
                "raw": 699.87,
            },
            "targetMedianPrice": {
                "raw": 751.0,
            },
            "recommendationMean": {
                "raw": 2.6,
            },
            "recommendationKey": "hold",
            "numberOfAnalystOpinions": {
                "raw": 36,
            },
            "totalCash": {
                "raw": 16229000192,
            },
            "totalCashPerShare": {
                "raw": 16.393,
            },
            "ebitda": {
                "raw": 5751000064,
            },
            "totalDebt": {
                "raw": 11169999872,
            },
            "quickRatio": {
                "raw": 1.123,
            },
            "currentRatio": {
                "raw": 1.508,
            },
            "totalRevenue": {
                "raw": 41862000640,
            },
            "debtToEquity": {
                "raw": 42.552,
            },
            "revenuePerShare": {
                "raw": 43.812,
            },
            "returnOnAssets": {
                "raw": 0.043509997,
            },
            "returnOnEquity": {
                "raw": 0.12275,
            },
            "grossProfits": {
                "raw": 6630000000,
            },
            "freeCashflow": {
                "raw": 4515624960,
            },
            "operatingCashflow": {
                "raw": 9184000000,
            },
            "earningsGrowth": {
                "raw": 9.2,
            },
            "revenueGrowth": {
                "raw": 0.981,
            },
            "grossMargins": {
                "raw": 0.22044,
            },
            "ebitdaMargins": {
                "raw": 0.13738,
            },
            "operatingMargins": {
                "raw": 0.07756,
            },
            "profitMargins": {
                "raw": 0.0521,
            },
            "financialCurrency": "USD"
        }
        }


        }
            }
        '''

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
