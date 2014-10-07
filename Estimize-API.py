
import requests
import pdb
import sys

from optparse import OptionParser

"""
-API requests should be made to http://api.estimize.com/
-You must supply your API key in the HTTP header X-Estimize-Key, otherwise you will receive a 403 Forbidden response
-Responses are in JSON. You need to specifiy in the HTTP header that content-type should be application/json (see example below)
-Parameters should be specified as query string parameters
-Successful responses will have a status code of 200
-Invalid requests will return a status code of 422 with a JSON object that specifies the errors as an array of strings
within the errors property
"""


url = "http://api.estimize.com" 
headers = {"X-Estimize-Key" : "INSERT API KEY HERE!!!", "content-type" : "application/json"}


def request_company_information(ticker):
    """
    Overview: returns a dictionary of the company information for the company specified with ticker
    Required params: None
    Optional params: None
    Response:
	-name: The name of the company
	-ticker: The ticker/symbol for the company
    """
    function_url = url + "/companies/%s" % ticker
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_releases_for_company(ticker):
    """
    Overview: returns a list of dictionaries of the past financial releases for the speficied company (by ticker)
    Required params: None
    Optional params: None
    Response: 
	-fiscal_year: The fiscal year for the release
	-fiscal_quarter: The fiscal quarter for the release
	-release_date: The date of the release
	-eps: The earnings per share for the specified fiscal quarter
	-revenue: The revenue for the speified fiscal quarter
	-wallstreet_eps_estimate: The estimated EPS from Wall Street
	-wallstreet_revenue_estimate: The estimated revenue from Wall Street
	-consensus_eps_estimate: The average estimated EPS by the Estimize community 
	-consensus_revenue_estimate: The average estimated revenue by the Estimize community
    """
    function_url = url + "/companies/%s/releases" % ticker
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_releases_for_company_for_year(ticker,year):
    """
    Overview: returns a list of all the financial releases for the specified company(ticker) for the specified fiscal year(year)
    Required params: None
    Optional params: None
    Response:
	-fiscal_year: The fiscal year for the release
	-fiscal_quarter: The fiscal quarter for the release
	-release_date: The date of the release
	-eps: The earnings per share for the specified fiscal quarter
	-revenue: The revenue for the speified fiscal quarter
	-wallstreet_eps_estimate: The estimated EPS from Wall Street
	-wallstreet_revenue_estimate: The estimated revenue from Wall Street
	-consensus_eps_estimate: The average estimated EPS by the Estimize community 
	-consensus_revenue_estimate: The average estimated revenue by the Estimize community
    """
    function_url = url + "/companies/%s/releases/%s" % (ticker,year)
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_releases_for_company_for_year_for_quarter(ticker,year,quarter):
    """
    Overview: returns a dictionary of the financial release for the specified company(ticker) for the specified fiscal year(year)
    for a specified quarter(quarter)
    Required params: None
    Optional params: None
    Response:
	-fiscal_year: The fiscal year for the release
	-fiscal_quarter: The fiscal quarter for the release
	-release_date: The date of the release
	-eps: The earnings per share for the specified fiscal quarter
	-revenue: The revenue for the speified fiscal quarter
	-wallstreet_eps_estimate: The estimated EPS from Wall Street
	-wallstreet_revenue_estimate: The estimated revenue from Wall Street
	-consensus_eps_estimate: The average estimated EPS by the Estimize community 
	-consensus_revenue_estimate: The average estimated revenue by the Estimize community
    """
    function_url = url + "/companies/%s/releases/%s/%s" % (ticker,year,quarter)
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_estimates_for_company(ticker):
    """
    Overview: returns all the estimates for a company (specified by ticker)
    Required params: None
    Optional params: None
    Returns: an array of estimate objects where each estimate has the following properties
	-id: the unique identifier for the estimate
	-ticker: the ticker for the company being estimated
	-fiscal_year: the fiscal year of the quarter being estimated 
	-fiscal_quarter: the fiscal quarter of the quarter being estimated
	-eps: the estimated earnings per share for the company in the specified fiscal quarter
	-revenue: the estimated revenue for the company in the specified fiscal quarter
	-username: the author of the estimate
	-created_at: the time that the estimate was created (UTC)
    """
    function_url = url + "/companies/%s/estimates" % ticker
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_estimates_for_company_for_year(ticker,year):
    """
    Overview: returns all the estimates for a company (specified by ticker) for the specified fiscal year
    Required params: None
    Optional params: None
    Returns: an array of estimate objects where each estimate has the following properties
	-id: the unique identifier for the estimate
	-ticker: the ticker for the company being estimated
	-fiscal_year: the fiscal year of the quarter being estimated 
	-fiscal_quarter: the fiscal quarter of the quarter being estimated
	-eps: the estimated earnings per share for the company in the specified fiscal quarter
	-revenue: the estimated revenue for the company in the specified fiscal quarter
	-username: the author of the estimate
	-created_at: the time that the estimate was created (UTC)
    """
    function_url = url + "/companies/%s/estimates/%s" % (ticker,year)
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_estimates_for_company_for_year_for_quarter(ticker,year,quarter):
    """
    Overview: returns all the estimates for a company (specified by ticker) for the specified fiscal year
    for a specified quarter(quarter)
    Required params: None
    Optional params: None
    Returns: an array of estimate objects where each estimate has the following properties
	-id: the unique identifier for the estimate
	-ticker: the ticker for the company being estimated
	-fiscal_year: the fiscal year of the quarter being estimated 
	-fiscal_quarter: the fiscal quarter of the quarter being estimated
	-eps: the estimated earnings per share for the company in the specified fiscal quarter
	-revenue: the estimated revenue for the company in the specified fiscal quarter
	-username: the author of the estimate
	-created_at: the time that the estimate was created (UTC)
    """
    function_url = url + "/companies/%s/estimates/%s/%s" % (ticker,year,quarter)
    req = requests.get(function_url, headers=headers)
    if req.status_code != 200 : return None
    return req.json()


def request_estimates(start_date,end_date):
    """
    Overview: returns all estimates in the specified date-range for all companies 
    Required params: 
	start_date: the start date for the date range of estimates to return YYYY-MM-DD
	end_date: the end date for the date range of estimates to return YYYY-MM-DD
    Optional params: None
    Returns: an array of estimate objects where each estimate has the following properties
	-id: the unique identifier for the estimate
	-ticker: the ticker for the company being estimated
	-fiscal_year: the fiscal year of the quarter being estimated 
	-fiscal_quarter: the fiscal quarter of the quarter being estimated
	-eps: the estimated earnings per share for the company in the specified fiscal quarter
	-revenue: the estimated revenue for the company in the specified fiscal quarter
	-username: the author of the estimate
	-created_at: the time that the estimate was created (UTC)
    """
    function_url = url + "/estimates"
    params = {"start_date" : start_date, "end_date" : end_date}
    req = requests.get(function_url, params=params, headers=headers)
    pdb.set_trace()
    if req.status_code != 200 : return None
    return req.json()


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--t", "--test", type="int", dest="test", 
			help="""
				test 1: request_company_information
				test 2: request_releases_for_company
				test 3: request_releases_for_company_for_year
				test 4: request_releases_for_company_for_year_for_quarter
				test 5: request_estimates_for_company
				test 6: request_estimates_for_company_for_year
				test 7: request_estimates_for_company_for_year_for_quarter
				test 8: request_estimates
			     """, default=1)
    (options, args) = parser.parse_args()
    if options.test == 1 : request_company_information("AAPL")
    elif options.test == 2 : request_releases_for_company("AAPL")
    elif options.test == 3 : request_releases_for_company_for_year("AAPL","2013")
    elif options.test == 4 : request_releases_for_company_for_year_for_quarter("AAPL","2013","4")
    elif options.test == 5 : request_estimates_for_company("AAPL")
    elif options.test == 6 : request_estimates_for_company_for_year("AAPL","2013")
    elif options.test == 7 : request_estimates_for_company_for_year_for_quarter("AAPL","2013","4")
    elif options.test == 8 : request_estimates("2014-01-01","2014-01-10")
    else : sys.exit("Useless option passed. Try again.")




