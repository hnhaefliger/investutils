# investutils

An API designed to provide a unified interface for future personal investment applications by gathering updated info from exchanges, data apis and other websites.

## Current utilities

### Ticker info

To retrieve info about a specific ticker (will return additional insights from sources such as yahoo finance) (in progress):

```
GET http://investmentutilities.herokuapp.com/api/listings/ticker/{ticker}
```

To retrieve a list based on filters:

```
GET http://investmentutilities.herokuapp.com/api/listings/ticker?{params}

GET params (optional):
ticker_type: [equity, etf, etc.]
offset: [0-infinity]
limit: [0-infinity]
on_robinhood: [true/false]
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

