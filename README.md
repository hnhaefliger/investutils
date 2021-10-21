# investutils

An API designed to provide a unified interface for future personal investment applications by gathering updated info from exchanges, data apis and other websites. In the future it will be combined with [media analysis](https://github.com/hnhaefliger/MediaAnalysis).

## Current utilities

### Ticker info

To retrieve info about a specific ticker (will return additional insights from sources such as yahoo finance) (in progress):

```
GET http://investmentutilities.herokuapp.com/api/listings/ticker/{ticker}
```

To retrieve a list based on filters:

```
GET http://investmentutilities.herokuapp.com/api/listings/ticker?{params}

GET params:
ticker_type: [equity, etf, etc.] (optional)
offset: [0-infinity] (optional)
limit: [0-infinity] (optional)
on_robinhood: [true/false] (optional)
```

If you think that a ticker is missing but should be added to the list:

```
POST http://investmentutilities.herokuapp.com/api/listings/ticker/

POST params:
ticker: {symbol}
```

To get the chart data for a ticker.

```
GET http://investmentutilities.herokuapp.com/api/listings/chart/{ticker}?{params}

GET params:
range: [1d, 1w, 1m, 1y, max, etc.] (required)
interval: [1d, 1m, 1h, etc.] (required)
```

To get data about a ticker.
Currently available {data} urls: summary_detail, asset_profile, financial_data, key_statistics, calendar_events, income_statement_quarterly, cashflow, balancesheet, earnings, esg, insights.

```
GET http://investmentutilities.herokuapp.com/api/listings/{data}/{ticker}
```

### Community-based data

To get all posts during the last 24-hours from a given subreddit.

```
GET http://investmentutilities.herokuapp.com/api/community/reddit/posts/{subreddit}
```

To get trending symbols from yahoo finance.

```
GET http://investmentutilities.herokuapp.com/api/community/yfinance/trending/
```

To get trending related symbols from yahoo finance.

```
GET http://investmentutilities.herokuapp.com/api/community/yfinance/trending/{ticker}
```

To get trending symbols from stocktwits.

```
GET http://investmentutilities.herokuapp.com/api/community/stocktwits/watchlist/
```

To get the number of times that a symbol appears on a stocktwits watchlist.

```
GET http://investmentutilities.herokuapp.com/api/community/stocktwits/watchlist/{ticker}
```

To get the most recent comments about a symbol on stocktwits.

```
GET http://investmentutilities.herokuapp.com/api/community/stocktwits/comments/{ticker}
```

To get stocktwits sentiment history about a symbol based on user comments.

```
GET http://investmentutilities.herokuapp.com/api/community/stocktwits/sentiment/{ticker}
```

To get stocktwits message volume history about a symbol based on user comments.

```
GET http://investmentutilities.herokuapp.com/api/community/stocktwits/message_volume/{ticker}
```

To get recent news articles about a symbol

```
GET http://investmentutilities.herokuapp.com/api/community/google/news/{ticker}?{params}

GET params:
days: get news articles published in the last n days (default=7)
```