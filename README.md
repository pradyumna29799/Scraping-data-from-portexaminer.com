# Scraping-data-from-portexaminer.com

This project involves scraping data from PortExaminer.com, a website that provides access to US customs import records for millions of real ocean shipments. The aim is to collect data about the shipping activities of five manufacturing companies - Ford Motor Company, Toyota, Tesla Motors, Mercedes-Benz, and General Motors. The data collected will be used to analyze the supply chains of the manufacturing companies.

# Steps to scrape data:

Go to https://portexaminer.com/
Change the dropdown option from ‘Supplier Name’ to ‘Importer Name’.
Search for the name of the company.
Parse the data from all links on the first page and get the output.
The output should include the Searched Importer, Shipper, Consignee, Notify Party, and Bill of Lading No. fields.

The goal of the project is to automate the process of collecting data and store it in a structured format such as a CSV or JSON file. The extracted data can then be used to analyze the supply chain activities of the manufacturing companies.

# Libraries used:

BeautifulSoup: For web scraping

requests: For sending HTTP requests to the website

pandas: For storing and manipulating the extracted data

selenium: For automatic storing and scraping data from site
# Output:
The final output can be used to identify the suppliers of the manufacturing companies, the commodities or products they import, and the countries they import from. This information can be used by management consultancies to analyze the supply chains of their customers and help them make informed decisions.
