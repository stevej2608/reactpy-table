from typing import List, Optional
from pydantic import BaseModel
from reactpy_table import Column, Columns

# pylint: disable=C0302

class CompanyModel(BaseModel):
    index: int
    symbol: str
    name: str
    sector: str
    industry: str
    headquarters : str
    CIK: str


def get_sp500(rows:Optional[int]=None) -> List[CompanyModel]:
    table_rows = [CompanyModel(index=index+1, **row) for index, row in enumerate(SP500)]
    return table_rows if rows is None else table_rows[0:rows]

COLS: Columns = [
    Column(name='index', label='#'),
    Column(name='symbol', label='Symbol'),
    Column(name='name', label='Name'),
    Column(name='sector', label='Sector'),
    Column(name='industry', label='Industry'),
    Column(name='headquarters', label='Headquarters'),
    Column(name='CIK', label='CIK')
    ]

# https://github.com/noahg/sp500csv/tree/master

# cSpell:disable

SP500 = [
    {
      "symbol": "MMM",
      "name": "3M Company",
      "sector": "Industrials",
      "industry": "Industrial Conglomerates",
      "headquarters": "St. Paul, Minnesota",
      "CIK": "0000066740"
    },
    {
      "symbol": "AOS",
      "name": "A.O. Smith Corp",
      "sector": "Industrials",
      "industry": "Building Products",
      "headquarters": "Milwaukee, Wisconsin",
      "CIK": "0000091142"
    },
    {
      "symbol": "ABT",
      "name": "Abbott Laboratories",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "North Chicago, Illinois",
      "CIK": "0000001800"
    },
    {
      "symbol": "ABBV",
      "name": "AbbVie Inc.",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "North Chicago, Illinois",
      "CIK": "0001551152"
    },
    {
      "symbol": "ABMD",
      "name": "ABIOMED Inc",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Danvers, Massachusetts",
      "CIK": "0000815094"
    },
    {
      "symbol": "ACN",
      "name": "Accenture plc",
      "sector": "Information Technology",
      "industry": "IT Consulting & Other Services",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001467373"
    },
    {
      "symbol": "ATVI",
      "name": "Activision Blizzard",
      "sector": "Communication Services",
      "industry": "Interactive Home Entertainment",
      "headquarters": "Santa Monica, California",
      "CIK": "0000718877"
    },
    {
      "symbol": "ADBE",
      "name": "Adobe Systems Inc",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "San Jose, California",
      "CIK": "0000796343"
    },
    {
      "symbol": "AAP",
      "name": "Advance Auto Parts",
      "sector": "Consumer Discretionary",
      "industry": "Automotive Retail",
      "headquarters": "Raleigh, North Carolina",
      "CIK": "0001158449"
    },
    {
      "symbol": "AMD",
      "name": "Advanced Micro Devices Inc",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Santa Clara, California",
      "CIK": "0000002488"
    },
    {
      "symbol": "AES",
      "name": "AES Corp",
      "sector": "Utilities",
      "industry": "Independent Power Producers & Energy Traders",
      "headquarters": "Arlington, Virginia",
      "CIK": "0000874761"
    },
    {
      "symbol": "AFL",
      "name": "AFLAC Inc",
      "sector": "Financials",
      "industry": "Life & Health Insurance",
      "headquarters": "Columbus, Georgia",
      "CIK": "0000004977"
    },
    {
      "symbol": "A",
      "name": "Agilent Technologies Inc",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Santa Clara, California",
      "CIK": "0001090872"
    },
    {
      "symbol": "APD",
      "name": "Air Products & Chemicals Inc",
      "sector": "Materials",
      "industry": "Industrial Gases",
      "headquarters": "Allentown, Pennsylvania",
      "CIK": "0000002969"
    },
    {
      "symbol": "AKAM",
      "name": "Akamai Technologies Inc",
      "sector": "Information Technology",
      "industry": "Internet Services & Infrastructure",
      "headquarters": "Cambridge, Massachusetts",
      "CIK": "0001086222"
    },
    {
      "symbol": "ALK",
      "name": "Alaska Air Group Inc",
      "sector": "Industrials",
      "industry": "Airlines",
      "headquarters": "Seattle, Washington",
      "CIK": "0000766421"
    },
    {
      "symbol": "ALB",
      "name": "Albemarle Corp",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "Charlotte, North Carolina",
      "CIK": "0000915913"
    },
    {
      "symbol": "ARE",
      "name": "Alexandria Real Estate Equities",
      "sector": "Real Estate",
      "industry": "Office REITs",
      "headquarters": "Pasadena, California",
      "CIK": "0001035443"
    },
    {
      "symbol": "ALXN",
      "name": "Alexion Pharmaceuticals",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Boston, Massachusetts",
      "CIK": "0000899866"
    },
    {
      "symbol": "ALGN",
      "name": "Align Technology",
      "sector": "Health Care",
      "industry": "Health Care Supplies",
      "headquarters": "San Jose, California",
      "CIK": "0001097149"
    },
    {
      "symbol": "ALLE",
      "name": "Allegion",
      "sector": "Industrials",
      "industry": "Building Products",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001579241"
    },
    {
      "symbol": "AGN",
      "name": "Allergan, plc",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001578845"
    },
    {
      "symbol": "ADS",
      "name": "Alliance Data Systems",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Plano, Texas",
      "CIK": "0001101215"
    },
    {
      "symbol": "LNT",
      "name": "Alliant Energy Corp",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Madison, Wisconsin",
      "CIK": "0000352541"
    },
    {
      "symbol": "ALL",
      "name": "Allstate Corp",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "Northfield Township, Illinois",
      "CIK": "0000899051"
    },
    {
      "symbol": "GOOGL",
      "name": "Alphabet Inc Class A",
      "sector": "Communication Services",
      "industry": "Interactive Media & Services",
      "headquarters": "Mountain View, California",
      "CIK": "0001652044"
    },
    {
      "symbol": "GOOG",
      "name": "Alphabet Inc Class C",
      "sector": "Communication Services",
      "industry": "Interactive Media & Services",
      "headquarters": "Mountain View, California",
      "CIK": "0001652044"
    },
    {
      "symbol": "MO",
      "name": "Altria Group Inc",
      "sector": "Consumer Staples",
      "industry": "Tobacco",
      "headquarters": "Richmond, Virginia",
      "CIK": "0000764180"
    },
    {
      "symbol": "AMZN",
      "name": "Amazon.com Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Internet & Direct Marketing Retail",
      "headquarters": "Seattle, Washington",
      "CIK": "0001018724"
    },
    {
      "symbol": "AMCR",
      "name": "Amcor plc",
      "sector": "Materials",
      "industry": "Paper Packaging",
      "headquarters": "Warmley, Bristol, United Kingdom",
      "CIK": "0001748790"
    },
    {
      "symbol": "AEE",
      "name": "Ameren Corp",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "St. Louis, Missouri",
      "CIK": "0001002910"
    },
    {
      "symbol": "AAL",
      "name": "American Airlines Group",
      "sector": "Industrials",
      "industry": "Airlines",
      "headquarters": "Fort Worth, Texas",
      "CIK": "0000006201"
    },
    {
      "symbol": "AEP",
      "name": "American Electric Power",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Columbus, Ohio",
      "CIK": "0000004904"
    },
    {
      "symbol": "AXP",
      "name": "American Express Co",
      "sector": "Financials",
      "industry": "Consumer Finance",
      "headquarters": "New York, New York",
      "CIK": "0000004962"
    },
    {
      "symbol": "AIG",
      "name": "American International Group",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "New York, New York",
      "CIK": "0000005272"
    },
    {
      "symbol": "AMT",
      "name": "American Tower Corp.",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Boston, Massachusetts",
      "CIK": "0001053507"
    },
    {
      "symbol": "AWK",
      "name": "American Water Works Company Inc",
      "sector": "Utilities",
      "industry": "Water Utilities",
      "headquarters": "Camden, New Jersey",
      "CIK": "0001410636"
    },
    {
      "symbol": "AMP",
      "name": "Ameriprise Financial",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "Minneapolis, Minnesota",
      "CIK": "0000820027"
    },
    {
      "symbol": "ABC",
      "name": "AmerisourceBergen Corp",
      "sector": "Health Care",
      "industry": "Health Care Distributors",
      "headquarters": "Chesterbrook, Pennsylvania",
      "CIK": "0001140859"
    },
    {
      "symbol": "AME",
      "name": "AMETEK Inc.",
      "sector": "Industrials",
      "industry": "Electrical Components & Equipment",
      "headquarters": "Berwyn, Pennsylvania",
      "CIK": "0001037868"
    },
    {
      "symbol": "AMGN",
      "name": "Amgen Inc.",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Thousand Oaks, California",
      "CIK": "0000318154"
    },
    {
      "symbol": "APH",
      "name": "Amphenol Corp",
      "sector": "Information Technology",
      "industry": "Electronic Components",
      "headquarters": "Wallingford, Connecticut",
      "CIK": "0000820313"
    },
    {
      "symbol": "ADI",
      "name": "Analog Devices, Inc.",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Norwood, Massachusetts",
      "CIK": "0000006281"
    },
    {
      "symbol": "ANSS",
      "name": "ANSYS",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Canonsburg, Pennsylvania",
      "CIK": "0001013462"
    },
    {
      "symbol": "ANTM",
      "name": "Anthem",
      "sector": "Health Care",
      "industry": "Managed Health Care",
      "headquarters": "Indianapolis, Indiana",
      "CIK": "0001156039"
    },
    {
      "symbol": "AON",
      "name": "Aon plc",
      "sector": "Financials",
      "industry": "Insurance Brokers",
      "headquarters": "London, United Kingdom",
      "CIK": "0000315293"
    },
    {
      "symbol": "APA",
      "name": "Apache Corporation",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0000006769"
    },
    {
      "symbol": "AIV",
      "name": "Apartment Investment & Management",
      "sector": "Real Estate",
      "industry": "Residential REITs",
      "headquarters": "Denver, Colorado",
      "CIK": "0000922864"
    },
    {
      "symbol": "AAPL",
      "name": "Apple Inc.",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Cupertino, California",
      "CIK": "0000320193"
    },
    {
      "symbol": "AMAT",
      "name": "Applied Materials Inc.",
      "sector": "Information Technology",
      "industry": "Semiconductor Equipment",
      "headquarters": "Santa Clara, California",
      "CIK": "0000006951"
    },
    {
      "symbol": "APTV",
      "name": "Aptiv PLC",
      "sector": "Consumer Discretionary",
      "industry": "Auto Parts & Equipment",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001521332"
    },
    {
      "symbol": "ADM",
      "name": "Archer-Daniels-Midland Co",
      "sector": "Consumer Staples",
      "industry": "Agricultural Products",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000007084"
    },
    {
      "symbol": "ARNC",
      "name": "Arconic Inc.",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "New York, New York",
      "CIK": "0000004281"
    },
    {
      "symbol": "ANET",
      "name": "Arista Networks",
      "sector": "Information Technology",
      "industry": "Communications Equipment",
      "headquarters": "Santa Clara, California",
      "CIK": "0001596532"
    },
    {
      "symbol": "AJG",
      "name": "Arthur J. Gallagher & Co.",
      "sector": "Financials",
      "industry": "Insurance Brokers",
      "headquarters": "Itasca, Illinois",
      "CIK": "0000354190"
    },
    {
      "symbol": "AIZ",
      "name": "Assurant",
      "sector": "Financials",
      "industry": "Multi-line Insurance",
      "headquarters": "New York, New York",
      "CIK": "0001267238"
    },
    {
      "symbol": "T",
      "name": "AT&T Inc.",
      "sector": "Communication Services",
      "industry": "Integrated Telecommunication Services",
      "headquarters": "Dallas, Texas",
      "CIK": "0000732717"
    },
    {
      "symbol": "ATO",
      "name": "Atmos Energy Corp",
      "sector": "Utilities",
      "industry": "Gas Utilities",
      "headquarters": "Dallas, Texas",
      "CIK": "0000731802"
    },
    {
      "symbol": "ADSK",
      "name": "Autodesk Inc.",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "San Rafael, California",
      "CIK": "0000769397"
    },
    {
      "symbol": "ADP",
      "name": "Automatic Data Processing",
      "sector": "Information Technology",
      "industry": "Internet Services & Infrastructure",
      "headquarters": "Roseland, New Jersey",
      "CIK": "0000008670"
    },
    {
      "symbol": "AZO",
      "name": "AutoZone Inc",
      "sector": "Consumer Discretionary",
      "industry": "Specialty Stores",
      "headquarters": "Memphis, Tennessee",
      "CIK": "0000866787"
    },
    {
      "symbol": "AVB",
      "name": "AvalonBay Communities, Inc.",
      "sector": "Real Estate",
      "industry": "Residential REITs",
      "headquarters": "Arlington, Virginia[3]",
      "CIK": "0000915912"
    },
    {
      "symbol": "AVY",
      "name": "Avery Dennison Corp",
      "sector": "Materials",
      "industry": "Paper Packaging",
      "headquarters": "Glendale, California",
      "CIK": "0000008818"
    },
    {
      "symbol": "BKR",
      "name": "Baker Hughes Co",
      "sector": "Energy",
      "industry": "Oil & Gas Equipment & Services",
      "headquarters": "Houston, Texas",
      "CIK": "0001701605"
    },
    {
      "symbol": "BLL",
      "name": "Ball Corp",
      "sector": "Materials",
      "industry": "Metal & Glass Containers",
      "headquarters": "Broomfield, Colorado",
      "CIK": "0000009389"
    },
    {
      "symbol": "BAC",
      "name": "Bank of America Corp",
      "sector": "Financials",
      "industry": "Diversified Banks",
      "headquarters": "Charlotte, North Carolina",
      "CIK": "0000070858"
    },
    {
      "symbol": "BAX",
      "name": "Baxter International Inc.",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Deerfield, Illinois",
      "CIK": "0000010456"
    },
    {
      "symbol": "BDX",
      "name": "Becton Dickinson",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Franklin Lakes, New Jersey",
      "CIK": "0000010795"
    },
    {
      "symbol": "BRK.B",
      "name": "Berkshire Hathaway",
      "sector": "Financials",
      "industry": "Multi-Sector Holdings",
      "headquarters": "Omaha, Nebraska",
      "CIK": "0001067983"
    },
    {
      "symbol": "BBY",
      "name": "Best Buy Co. Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Computer & Electronics Retail",
      "headquarters": "Richfield, Minnesota",
      "CIK": "0000764478"
    },
    {
      "symbol": "BIIB",
      "name": "Biogen Inc.",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Cambridge, Massachusetts",
      "CIK": "0000875045"
    },
    {
      "symbol": "BLK",
      "name": "BlackRock",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "New York, New York",
      "CIK": "0001364742"
    },
    {
      "symbol": "BA",
      "name": "Boeing Company",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000012927"
    },
    {
      "symbol": "BKNG",
      "name": "Booking Holdings Inc",
      "sector": "Consumer Discretionary",
      "industry": "Internet & Direct Marketing Retail",
      "headquarters": "Norwalk, Connecticut",
      "CIK": "0001075531"
    },
    {
      "symbol": "BWA",
      "name": "BorgWarner",
      "sector": "Consumer Discretionary",
      "industry": "Auto Parts & Equipment",
      "headquarters": "Auburn Hills, Michigan",
      "CIK": "0000908255"
    },
    {
      "symbol": "BXP",
      "name": "Boston Properties",
      "sector": "Real Estate",
      "industry": "Office REITs",
      "headquarters": "Boston, Massachusetts",
      "CIK": "0001037540"
    },
    {
      "symbol": "BSX",
      "name": "Boston Scientific",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Marlborough, Massachusetts[4]",
      "CIK": "0000885725"
    },
    {
      "symbol": "BMY",
      "name": "Bristol-Myers Squibb",
      "sector": "Health Care",
      "industry": "Health Care Distributors",
      "headquarters": "New York, New York",
      "CIK": "0000014272"
    },
    {
      "symbol": "AVGO",
      "name": "Broadcom Inc.",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "San Jose, California",
      "CIK": "0001730168"
    },
    {
      "symbol": "BR",
      "name": "Broadridge Financial Solutions",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Lake Success, New York",
      "CIK": "0001383312"
    },
    {
      "symbol": "BF.B",
      "name": "Brown-Forman Corp.",
      "sector": "Consumer Staples",
      "industry": "Distillers & Vintners",
      "headquarters": "Louisville, Kentucky",
      "CIK": "0000014693"
    },
    {
      "symbol": "CHRW",
      "name": "C. H. Robinson Worldwide",
      "sector": "Industrials",
      "industry": "Air Freight & Logistics",
      "headquarters": "Eden Prairie, Minnesota",
      "CIK": "0001043277"
    },
    {
      "symbol": "COG",
      "name": "Cabot Oil & Gas",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0000858470"
    },
    {
      "symbol": "CDNS",
      "name": "Cadence Design Systems",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "San Jose, California",
      "CIK": "0000813672"
    },
    {
      "symbol": "CPB",
      "name": "Campbell Soup",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Camden, New Jersey",
      "CIK": "0000016732"
    },
    {
      "symbol": "COF",
      "name": "Capital One Financial",
      "sector": "Financials",
      "industry": "Consumer Finance",
      "headquarters": "Tysons Corner, Virginia",
      "CIK": "0000927628"
    },
    {
      "symbol": "CPRI",
      "name": "Capri Holdings",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "New York, New York",
      "CIK": "0001530721"
    },
    {
      "symbol": "CAH",
      "name": "Cardinal Health Inc.",
      "sector": "Health Care",
      "industry": "Health Care Distributors",
      "headquarters": "Dublin, Ohio",
      "CIK": "0000721371"
    },
    {
      "symbol": "KMX",
      "name": "Carmax Inc",
      "sector": "Consumer Discretionary",
      "industry": "Specialty Stores",
      "headquarters": "Richmond, Virginia",
      "CIK": "0001170010"
    },
    {
      "symbol": "CCL",
      "name": "Carnival Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Hotels, Resorts & Cruise Lines",
      "headquarters": "Miami, Florida",
      "CIK": "0000815097"
    },
    {
      "symbol": "CAT",
      "name": "Caterpillar Inc.",
      "sector": "Industrials",
      "industry": "Construction Machinery & Heavy Trucks",
      "headquarters": "Deerfield, Illinois",
      "CIK": "0000018230"
    },
    {
      "symbol": "CBOE",
      "name": "Cboe Global Markets",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "Chicago, Illinois",
      "CIK": "0001374310"
    },
    {
      "symbol": "CBRE",
      "name": "CBRE Group",
      "sector": "Real Estate",
      "industry": "Real Estate Services",
      "headquarters": "Los Angeles, California",
      "CIK": "0001138118"
    },
    {
      "symbol": "CDW",
      "name": "CDW",
      "sector": "Information Technology",
      "industry": "Technology Distributors",
      "headquarters": "Lincolnshire, Illinois",
      "CIK": "0001402057"
    },
    {
      "symbol": "CE",
      "name": "Celanese",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "Irving, Texas",
      "CIK": "0001306830"
    },
    {
      "symbol": "CNC",
      "name": "Centene Corporation",
      "sector": "Health Care",
      "industry": "Managed Health Care",
      "headquarters": "St Louis, Missouri",
      "CIK": "0001071739"
    },
    {
      "symbol": "CNP",
      "name": "CenterPoint Energy",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Houston, Texas",
      "CIK": "0001130310"
    },
    {
      "symbol": "CTL",
      "name": "CenturyLink Inc",
      "sector": "Communication Services",
      "industry": "Alternative Carriers",
      "headquarters": "Monroe, Louisiana",
      "CIK": "0000018926"
    },
    {
      "symbol": "CERN",
      "name": "Cerner",
      "sector": "Health Care",
      "industry": "Health Care Technology",
      "headquarters": "North Kansas City, Missouri",
      "CIK": "0000804753"
    },
    {
      "symbol": "CF",
      "name": "CF Industries Holdings Inc",
      "sector": "Materials",
      "industry": "Fertilizers & Agricultural Chemicals",
      "headquarters": "Deerfield, Illinois",
      "CIK": "0001324404"
    },
    {
      "symbol": "SCHW",
      "name": "Charles Schwab Corporation",
      "sector": "Financials",
      "industry": "Investment Banking & Brokerage",
      "headquarters": "San Francisco, California",
      "CIK": "0000316709"
    },
    {
      "symbol": "CHTR",
      "name": "Charter Communications",
      "sector": "Communication Services",
      "industry": "Cable & Satellite",
      "headquarters": "Stamford, Connecticut",
      "CIK": "0001091667"
    },
    {
      "symbol": "CVX",
      "name": "Chevron Corp.",
      "sector": "Energy",
      "industry": "Integrated Oil & Gas",
      "headquarters": "San Ramon, California",
      "CIK": "0000093410"
    },
    {
      "symbol": "CMG",
      "name": "Chipotle Mexican Grill",
      "sector": "Consumer Discretionary",
      "industry": "Restaurants",
      "headquarters": "Newport Beach, California",
      "CIK": "0001058090"
    },
    {
      "symbol": "CB",
      "name": "Chubb Limited",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "Zurich, Switzerland",
      "CIK": "0000896159"
    },
    {
      "symbol": "CHD",
      "name": "Church & Dwight",
      "sector": "Consumer Staples",
      "industry": "Household Products",
      "headquarters": "Ewing, New Jersey",
      "CIK": "0000313927"
    },
    {
      "symbol": "CI",
      "name": "CIGNA Corp.",
      "sector": "Health Care",
      "industry": "Managed Health Care",
      "headquarters": "Bloomfield, Connecticut",
      "CIK": "0000701221"
    },
    {
      "symbol": "XEC",
      "name": "Cimarex Energy",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Denver, Colorado",
      "CIK": "0001168054"
    },
    {
      "symbol": "CINF",
      "name": "Cincinnati Financial",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "Fairfield, Ohio",
      "CIK": "0000020286"
    },
    {
      "symbol": "CTAS",
      "name": "Cintas Corporation",
      "sector": "Industrials",
      "industry": "Diversified Support Services",
      "headquarters": "Mason, Ohio",
      "CIK": "0000723254"
    },
    {
      "symbol": "CSCO",
      "name": "Cisco Systems",
      "sector": "Information Technology",
      "industry": "Communications Equipment",
      "headquarters": "San Jose, California",
      "CIK": "0000858877"
    },
    {
      "symbol": "C",
      "name": "Citigroup Inc.",
      "sector": "Financials",
      "industry": "Diversified Banks",
      "headquarters": "New York, New York",
      "CIK": "0000831001"
    },
    {
      "symbol": "CFG",
      "name": "Citizens Financial Group",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Providence, Rhode Island",
      "CIK": "0000759944"
    },
    {
      "symbol": "CTXS",
      "name": "Citrix Systems",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Fort Lauderdale, Florida",
      "CIK": "0000877890"
    },
    {
      "symbol": "CME",
      "name": "CME Group Inc.",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "Chicago, Illinois",
      "CIK": "0001156375"
    },
    {
      "symbol": "CMS",
      "name": "CMS Energy",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Jackson, Michigan",
      "CIK": "0000811156"
    },
    {
      "symbol": "KO",
      "name": "Coca-Cola Company",
      "sector": "Consumer Staples",
      "industry": "Soft Drinks",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000021344"
    },
    {
      "symbol": "CTSH",
      "name": "Cognizant Technology Solutions",
      "sector": "Information Technology",
      "industry": "IT Consulting & Other Services",
      "headquarters": "Teaneck, New Jersey",
      "CIK": "0001058290"
    },
    {
      "symbol": "CL",
      "name": "Colgate-Palmolive",
      "sector": "Consumer Staples",
      "industry": "Household Products",
      "headquarters": "New York, New York",
      "CIK": "0000021665"
    },
    {
      "symbol": "CMCSA",
      "name": "Comcast Corp.",
      "sector": "Communication Services",
      "industry": "Cable & Satellite",
      "headquarters": "Philadelphia, Pennsylvania",
      "CIK": "0001166691"
    },
    {
      "symbol": "CMA",
      "name": "Comerica Inc.",
      "sector": "Financials",
      "industry": "Diversified Banks",
      "headquarters": "Dallas, Texas",
      "CIK": "0000028412"
    },
    {
      "symbol": "CAG",
      "name": "Conagra Brands",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000023217"
    },
    {
      "symbol": "CXO",
      "name": "Concho Resources",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Midland, Texas",
      "CIK": "0001358071"
    },
    {
      "symbol": "COP",
      "name": "ConocoPhillips",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0001163165"
    },
    {
      "symbol": "ED",
      "name": "Consolidated Edison",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "New York, New York",
      "CIK": "0001047862"
    },
    {
      "symbol": "STZ",
      "name": "Constellation Brands",
      "sector": "Consumer Staples",
      "industry": "Distillers & Vintners",
      "headquarters": "Victor, New York",
      "CIK": "0000016918"
    },
    {
      "symbol": "CPRT",
      "name": "Copart Inc",
      "sector": "Industrials",
      "industry": "Diversified Support Services",
      "headquarters": "Dallas, Texas",
      "CIK": "0000900075"
    },
    {
      "symbol": "GLW",
      "name": "Corning Inc.",
      "sector": "Information Technology",
      "industry": "Electronic Components",
      "headquarters": "Corning, New York",
      "CIK": "0000024741"
    },
    {
      "symbol": "CTVA",
      "name": "Corteva",
      "sector": "Materials",
      "industry": "Fertilizers & Agricultural Chemicals",
      "headquarters": "Wilmington, Delaware",
      "CIK": "0001755672"
    },
    {
      "symbol": "COST",
      "name": "Costco Wholesale Corp.",
      "sector": "Consumer Staples",
      "industry": "Hypermarkets & Super Centers",
      "headquarters": "Issaquah, Washington",
      "CIK": "0000909832"
    },
    {
      "symbol": "COTY",
      "name": "Coty, Inc",
      "sector": "Consumer Staples",
      "industry": "Personal Products",
      "headquarters": "New York, New York",
      "CIK": "0001024305"
    },
    {
      "symbol": "CCI",
      "name": "Crown Castle International Corp.",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Houston, Texas",
      "CIK": "0001051470"
    },
    {
      "symbol": "CSX",
      "name": "CSX Corp.",
      "sector": "Industrials",
      "industry": "Railroads",
      "headquarters": "Jacksonville, Florida",
      "CIK": "0000277948"
    },
    {
      "symbol": "CMI",
      "name": "Cummins Inc.",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Columbus, Indiana",
      "CIK": "0000026172"
    },
    {
      "symbol": "CVS",
      "name": "CVS Health",
      "sector": "Health Care",
      "industry": "Health Care Services",
      "headquarters": "Woonsocket, Rhode Island",
      "CIK": "0000064803"
    },
    {
      "symbol": "DHI",
      "name": "D. R. Horton",
      "sector": "Consumer Discretionary",
      "industry": "Homebuilding",
      "headquarters": "Fort Worth, Texas",
      "CIK": "0000882184"
    },
    {
      "symbol": "DHR",
      "name": "Danaher Corp.",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Washington, D.C.",
      "CIK": "0000313616"
    },
    {
      "symbol": "DRI",
      "name": "Darden Restaurants",
      "sector": "Consumer Discretionary",
      "industry": "Restaurants",
      "headquarters": "Orlando, Florida",
      "CIK": "0000940944"
    },
    {
      "symbol": "DVA",
      "name": "DaVita Inc.",
      "sector": "Health Care",
      "industry": "Health Care Facilities",
      "headquarters": "Denver, Colorado",
      "CIK": "0000927066"
    },
    {
      "symbol": "DE",
      "name": "Deere & Co.",
      "sector": "Industrials",
      "industry": "Agricultural & Farm Machinery",
      "headquarters": "Moline, Illinois",
      "CIK": "0000315189"
    },
    {
      "symbol": "DAL",
      "name": "Delta Air Lines Inc.",
      "sector": "Industrials",
      "industry": "Airlines",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000027904"
    },
    {
      "symbol": "XRAY",
      "name": "Dentsply Sirona",
      "sector": "Health Care",
      "industry": "Health Care Supplies",
      "headquarters": "York, Pennsylvania",
      "CIK": "0000818479"
    },
    {
      "symbol": "DVN",
      "name": "Devon Energy",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Oklahoma City, Oklahoma",
      "CIK": "0001090012"
    },
    {
      "symbol": "FANG",
      "name": "Diamondback Energy",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Midland, Texas",
      "CIK": "0001539838"
    },
    {
      "symbol": "DLR",
      "name": "Digital Realty Trust Inc",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "San Francisco, California",
      "CIK": "0001297996"
    },
    {
      "symbol": "DFS",
      "name": "Discover Financial Services",
      "sector": "Financials",
      "industry": "Consumer Finance",
      "headquarters": "Riverwoods, Illinois",
      "CIK": "0001393612"
    },
    {
      "symbol": "DISCA",
      "name": "Discovery Inc. Class A",
      "sector": "Communication Services",
      "industry": "Broadcasting",
      "headquarters": "Silver Spring, Maryland",
      "CIK": "0001437107"
    },
    {
      "symbol": "DISCK",
      "name": "Discovery Inc. Class C",
      "sector": "Communication Services",
      "industry": "Broadcasting",
      "headquarters": "Silver Spring, Maryland",
      "CIK": "0001437107"
    },
    {
      "symbol": "DISH",
      "name": "Dish Network",
      "sector": "Communication Services",
      "industry": "Cable & Satellite",
      "headquarters": "Meridian, Colorado",
      "CIK": "0001001082"
    },
    {
      "symbol": "DG",
      "name": "Dollar General",
      "sector": "Consumer Discretionary",
      "industry": "General Merchandise Stores",
      "headquarters": "Goodlettsville, Tennessee",
      "CIK": "0000029534"
    },
    {
      "symbol": "DLTR",
      "name": "Dollar Tree",
      "sector": "Consumer Discretionary",
      "industry": "General Merchandise Stores",
      "headquarters": "Chesapeake, Virginia",
      "CIK": "0000935703"
    },
    {
      "symbol": "D",
      "name": "Dominion Energy",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Richmond, Virginia",
      "CIK": "0000715957"
    },
    {
      "symbol": "DOV",
      "name": "Dover Corp.",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Downers Grove, Illinois",
      "CIK": "0000029905"
    },
    {
      "symbol": "DOW",
      "name": "Dow Inc.",
      "sector": "Materials",
      "industry": "Commodity Chemicals",
      "headquarters": "Midland, Michigan",
      "CIK": "0001751788"
    },
    {
      "symbol": "DTE",
      "name": "DTE Energy Co.",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Detroit, Michigan",
      "CIK": "0000936340"
    },
    {
      "symbol": "DUK",
      "name": "Duke Energy",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Charlotte, North Carolina",
      "CIK": "0001326160"
    },
    {
      "symbol": "DRE",
      "name": "Duke Realty Corp",
      "sector": "Real Estate",
      "industry": "Industrial REITs",
      "headquarters": "Indianapolis, Indiana",
      "CIK": "0000783280"
    },
    {
      "symbol": "DD",
      "name": "DuPont de Nemours Inc",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "Midland, Michigan",
      "CIK": "0001666700"
    },
    {
      "symbol": "DXC",
      "name": "DXC Technology",
      "sector": "Information Technology",
      "industry": "IT Consulting & Other Services",
      "headquarters": "Tysons Corner, Virginia",
      "CIK": "0001688568"
    },
    {
      "symbol": "ETFC",
      "name": "E*Trade",
      "sector": "Financials",
      "industry": "Investment Banking & Brokerage",
      "headquarters": "New York, New York",
      "CIK": "0001015780"
    },
    {
      "symbol": "EMN",
      "name": "Eastman Chemical",
      "sector": "Materials",
      "industry": "Diversified Chemicals",
      "headquarters": "Kingsport, Tennessee",
      "CIK": "0000915389"
    },
    {
      "symbol": "ETN",
      "name": "Eaton Corporation",
      "sector": "Industrials",
      "industry": "Electrical Components & Equipment",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001551182"
    },
    {
      "symbol": "EBAY",
      "name": "eBay Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Internet & Direct Marketing Retail",
      "headquarters": "San Jose, California",
      "CIK": "0001065088"
    },
    {
      "symbol": "ECL",
      "name": "Ecolab Inc.",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "St. Paul, Minnesota",
      "CIK": "0000031462"
    },
    {
      "symbol": "EIX",
      "name": "Edison Int'l",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Rosemead, California",
      "CIK": "0000827052"
    },
    {
      "symbol": "EW",
      "name": "Edwards Lifesciences",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Irvine, California",
      "CIK": "0001099800"
    },
    {
      "symbol": "EA",
      "name": "Electronic Arts",
      "sector": "Communication Services",
      "industry": "Interactive Home Entertainment",
      "headquarters": "Redwood City, California",
      "CIK": "0000712515"
    },
    {
      "symbol": "EMR",
      "name": "Emerson Electric Company",
      "sector": "Industrials",
      "industry": "Electrical Components & Equipment",
      "headquarters": "Ferguson, Missouri",
      "CIK": "0000032604"
    },
    {
      "symbol": "ETR",
      "name": "Entergy Corp.",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "New Orleans, Louisiana",
      "CIK": "0000065984"
    },
    {
      "symbol": "EOG",
      "name": "EOG Resources",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0000821189"
    },
    {
      "symbol": "EFX",
      "name": "Equifax Inc.",
      "sector": "Industrials",
      "industry": "Research & Consulting Services",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000033185"
    },
    {
      "symbol": "EQIX",
      "name": "Equinix",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Redwood City, California",
      "CIK": "0001101239"
    },
    {
      "symbol": "EQR",
      "name": "Equity Residential",
      "sector": "Real Estate",
      "industry": "Residential REITs",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000906107"
    },
    {
      "symbol": "ESS",
      "name": "Essex Property Trust, Inc.",
      "sector": "Real Estate",
      "industry": "Residential REITs",
      "headquarters": "Palo Alto, California",
      "CIK": "0000920522"
    },
    {
      "symbol": "EL",
      "name": "Estee Lauder Cos.",
      "sector": "Consumer Staples",
      "industry": "Personal Products",
      "headquarters": "New York, New York",
      "CIK": "0001001250"
    },
    {
      "symbol": "RE",
      "name": "Everest Re Group Ltd.",
      "sector": "Financials",
      "industry": "Reinsurance",
      "headquarters": "Hamilton, Bermuda",
      "CIK": "0001095073"
    },
    {
      "symbol": "EVRG",
      "name": "Evergy",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Kansas City, Missouri",
      "CIK": "0001711269"
    },
    {
      "symbol": "ES",
      "name": "Eversource Energy",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Springfield, Massachusetts",
      "CIK": "0000072741"
    },
    {
      "symbol": "EXC",
      "name": "Exelon Corp.",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Chicago, Illinois",
      "CIK": "0001109357"
    },
    {
      "symbol": "EXPE",
      "name": "Expedia Group",
      "sector": "Consumer Discretionary",
      "industry": "Internet & Direct Marketing Retail",
      "headquarters": "Bellevue, Washington",
      "CIK": "0001324424"
    },
    {
      "symbol": "EXPD",
      "name": "Expeditors",
      "sector": "Industrials",
      "industry": "Air Freight & Logistics",
      "headquarters": "Seattle, Washington",
      "CIK": "0000746515"
    },
    {
      "symbol": "EXR",
      "name": "Extra Space Storage",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Salt Lake City, Utah",
      "CIK": "0001289490"
    },
    {
      "symbol": "XOM",
      "name": "Exxon Mobil Corp.",
      "sector": "Energy",
      "industry": "Integrated Oil & Gas",
      "headquarters": "Irving, Texas",
      "CIK": "0000034088"
    },
    {
      "symbol": "FFIV",
      "name": "F5 Networks",
      "sector": "Information Technology",
      "industry": "Communications Equipment",
      "headquarters": "Seattle, Washington",
      "CIK": "0001048695"
    },
    {
      "symbol": "FB",
      "name": "Facebook, Inc.",
      "sector": "Communication Services",
      "industry": "Interactive Media & Services",
      "headquarters": "Menlo Park, California",
      "CIK": "0001326801"
    },
    {
      "symbol": "FAST",
      "name": "Fastenal Co",
      "sector": "Industrials",
      "industry": "Building Products",
      "headquarters": "Winona, Minnesota",
      "CIK": "0000815556"
    },
    {
      "symbol": "FRT",
      "name": "Federal Realty Investment Trust",
      "sector": "Real Estate",
      "industry": "Retail REITs",
      "headquarters": "Rockville, Maryland",
      "CIK": "0000034903"
    },
    {
      "symbol": "FDX",
      "name": "FedEx Corporation",
      "sector": "Industrials",
      "industry": "Air Freight & Logistics",
      "headquarters": "Memphis, Tennessee",
      "CIK": "0001048911"
    },
    {
      "symbol": "FIS",
      "name": "Fidelity National Information Services",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Jacksonville, Florida",
      "CIK": "0001136893"
    },
    {
      "symbol": "FITB",
      "name": "Fifth Third Bancorp",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Cincinnati, Ohio",
      "CIK": "0000035527"
    },
    {
      "symbol": "FRC",
      "name": "First Republic Bank",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "San Francisco, California",
      "CIK": "0001132979"
    },
    {
      "symbol": "FE",
      "name": "FirstEnergy Corp",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Akron, Ohio",
      "CIK": "0001031296"
    },
    {
      "symbol": "FISV",
      "name": "Fiserv Inc",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Brookfield, Wisconsin",
      "CIK": "0000798354"
    },
    {
      "symbol": "FLT",
      "name": "FleetCor Technologies Inc",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Norcross, Georgia",
      "CIK": "0001175454"
    },
    {
      "symbol": "FLIR",
      "name": "FLIR Systems",
      "sector": "Information Technology",
      "industry": "Electronic Equipment & Instruments",
      "headquarters": "Wilsonville, Oregon",
      "CIK": "0000354908"
    },
    {
      "symbol": "FLS",
      "name": "Flowserve Corporation",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Irving, Texas",
      "CIK": "0000030625"
    },
    {
      "symbol": "FMC",
      "name": "FMC Corporation",
      "sector": "Materials",
      "industry": "Fertilizers & Agricultural Chemicals",
      "headquarters": "Philadelphia, Pennsylvania",
      "CIK": "0000037785"
    },
    {
      "symbol": "F",
      "name": "Ford Motor",
      "sector": "Consumer Discretionary",
      "industry": "Automobile Manufacturers",
      "headquarters": "Dearborn, Michigan",
      "CIK": "0000037996"
    },
    {
      "symbol": "FTNT",
      "name": "Fortinet",
      "sector": "Information Technology",
      "industry": "Systems Software",
      "headquarters": "Sunnyvale, California",
      "CIK": "0001262039"
    },
    {
      "symbol": "FTV",
      "name": "Fortive Corp",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Everett, Washington",
      "CIK": "0001659166"
    },
    {
      "symbol": "FBHS",
      "name": "Fortune Brands Home & Security",
      "sector": "Industrials",
      "industry": "Building Products",
      "headquarters": "Deerfield, Illinois",
      "CIK": "0001519751"
    },
    {
      "symbol": "FOXA",
      "name": "Fox Corporation Class A",
      "sector": "Communication Services",
      "industry": "Movies & Entertainment",
      "headquarters": "New York, New York",
      "CIK": "0001308161"
    },
    {
      "symbol": "FOX",
      "name": "Fox Corporation Class B",
      "sector": "Communication Services",
      "industry": "Movies & Entertainment",
      "headquarters": "New York, New York",
      "CIK": "0001308161"
    },
    {
      "symbol": "BEN",
      "name": "Franklin Resources",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "San Mateo, California",
      "CIK": "0000038777"
    },
    {
      "symbol": "FCX",
      "name": "Freeport-McMoRan Inc.",
      "sector": "Materials",
      "industry": "Copper",
      "headquarters": "Phoenix, Arizona",
      "CIK": "0000831259"
    },
    {
      "symbol": "GPS",
      "name": "Gap Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel Retail",
      "headquarters": "San Francisco, California",
      "CIK": "0000039911"
    },
    {
      "symbol": "GRMN",
      "name": "Garmin Ltd.",
      "sector": "Consumer Discretionary",
      "industry": "Consumer Electronics",
      "headquarters": "Schaffhausen, Switzerland",
      "CIK": "0001121788"
    },
    {
      "symbol": "IT",
      "name": "Gartner Inc",
      "sector": "Information Technology",
      "industry": "IT Consulting & Other Services",
      "headquarters": "Stamford, Connecticut",
      "CIK": "0000749251"
    },
    {
      "symbol": "GD",
      "name": "General Dynamics",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Falls Church, Virginia",
      "CIK": "0000040533"
    },
    {
      "symbol": "GE",
      "name": "General Electric",
      "sector": "Industrials",
      "industry": "Industrial Conglomerates",
      "headquarters": "Boston, Massachusetts",
      "CIK": "0000040545"
    },
    {
      "symbol": "GIS",
      "name": "General Mills",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Golden Valley, Minnesota",
      "CIK": "0000040704"
    },
    {
      "symbol": "GM",
      "name": "General Motors",
      "sector": "Consumer Discretionary",
      "industry": "Automobile Manufacturers",
      "headquarters": "Detroit, Michigan",
      "CIK": "0001467858"
    },
    {
      "symbol": "GPC",
      "name": "Genuine Parts",
      "sector": "Consumer Discretionary",
      "industry": "Specialty Stores",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000040987"
    },
    {
      "symbol": "GILD",
      "name": "Gilead Sciences",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Foster City, California",
      "CIK": "0000882095"
    },
    {
      "symbol": "GPN",
      "name": "Global Payments Inc.",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0001123360"
    },
    {
      "symbol": "GL",
      "name": "Globe Life Inc.",
      "sector": "Financials",
      "industry": "Life & Health Insurance",
      "headquarters": "McKinney, Texas",
      "CIK": "0000320335"
    },
    {
      "symbol": "GS",
      "name": "Goldman Sachs Group",
      "sector": "Financials",
      "industry": "Investment Banking & Brokerage",
      "headquarters": "New York, New York",
      "CIK": "0000886982"
    },
    {
      "symbol": "GWW",
      "name": "Grainger (W.W.) Inc.",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Lake Forest, Illinois",
      "CIK": "0000277135"
    },
    {
      "symbol": "HRB",
      "name": "H&R Block",
      "sector": "Consumer Discretionary",
      "industry": "Specialized Consumer Services",
      "headquarters": "Kansas City, Missouri",
      "CIK": "0000012659"
    },
    {
      "symbol": "HAL",
      "name": "Halliburton Co.",
      "sector": "Energy",
      "industry": "Oil & Gas Equipment & Services",
      "headquarters": "Houston, Texas",
      "CIK": "0000045012"
    },
    {
      "symbol": "HBI",
      "name": "Hanesbrands Inc",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "Winston-Salem, North Carolina",
      "CIK": "0001359841"
    },
    {
      "symbol": "HOG",
      "name": "Harley-Davidson",
      "sector": "Consumer Discretionary",
      "industry": "Motorcycle Manufacturers",
      "headquarters": "Milwaukee, Wisconsin",
      "CIK": "0000793952"
    },
    {
      "symbol": "HIG",
      "name": "Hartford Financial Svc.Gp.",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "Hartford, Connecticut",
      "CIK": "0000874766"
    },
    {
      "symbol": "HAS",
      "name": "Hasbro Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Leisure Products",
      "headquarters": "Pawtucket, Rhode Island",
      "CIK": "0000046080"
    },
    {
      "symbol": "HCA",
      "name": "HCA Healthcare",
      "sector": "Health Care",
      "industry": "Health Care Facilities",
      "headquarters": "Nashville, Tennessee",
      "CIK": "0000860730"
    },
    {
      "symbol": "PEAK",
      "name": "Healthpeak Properties",
      "sector": "Real Estate",
      "industry": "Health Care REITs",
      "headquarters": "Long Beach, California",
      "CIK": "0000765880"
    },
    {
      "symbol": "HP",
      "name": "Helmerich & Payne",
      "sector": "Energy",
      "industry": "Oil & Gas Drilling",
      "headquarters": "Tulsa, Oklahoma[5]",
      "CIK": "0000046765"
    },
    {
      "symbol": "HSIC",
      "name": "Henry Schein",
      "sector": "Health Care",
      "industry": "Health Care Distributors",
      "headquarters": "Melville, New York",
      "CIK": "0001000228"
    },
    {
      "symbol": "HES",
      "name": "Hess Corporation",
      "sector": "Energy",
      "industry": "Integrated Oil & Gas",
      "headquarters": "New York, New York",
      "CIK": "0000004447"
    },
    {
      "symbol": "HPE",
      "name": "Hewlett Packard Enterprise",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Palo Alto, California",
      "CIK": "0001645590"
    },
    {
      "symbol": "HLT",
      "name": "Hilton Worldwide Holdings Inc",
      "sector": "Consumer Discretionary",
      "industry": "Hotels, Resorts & Cruise Lines",
      "headquarters": "Tysons Corner, Virginia",
      "CIK": "0001585689"
    },
    {
      "symbol": "HFC",
      "name": "HollyFrontier Corp",
      "sector": "Energy",
      "industry": "Oil & Gas Refining & Marketing",
      "headquarters": "Dallas, Texas",
      "CIK": "0000048039"
    },
    {
      "symbol": "HOLX",
      "name": "Hologic",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Marlborough, Massachusetts",
      "CIK": "0000859737"
    },
    {
      "symbol": "HD",
      "name": "Home Depot",
      "sector": "Consumer Discretionary",
      "industry": "Home Improvement Retail",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000354950"
    },
    {
      "symbol": "HON",
      "name": "Honeywell Int'l Inc.",
      "sector": "Industrials",
      "industry": "Industrial Conglomerates",
      "headquarters": "Morristown, New Jersey",
      "CIK": "0000773840"
    },
    {
      "symbol": "HRL",
      "name": "Hormel Foods Corp.",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Austin, Minnesota",
      "CIK": "0000048465"
    },
    {
      "symbol": "HST",
      "name": "Host Hotels & Resorts",
      "sector": "Real Estate",
      "industry": "Hotel & Resort REITs",
      "headquarters": "Bethesda, Maryland",
      "CIK": "0001070750"
    },
    {
      "symbol": "HPQ",
      "name": "HP Inc.",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Palo Alto, California",
      "CIK": "0000047217"
    },
    {
      "symbol": "HUM",
      "name": "Humana Inc.",
      "sector": "Health Care",
      "industry": "Managed Health Care",
      "headquarters": "Louisville, Kentucky",
      "CIK": "0000049071"
    },
    {
      "symbol": "HBAN",
      "name": "Huntington Bancshares",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Columbus, Ohio",
      "CIK": "0000049196"
    },
    {
      "symbol": "HII",
      "name": "Huntington Ingalls Industries",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Newport News, Virginia",
      "CIK": "0001501585"
    },
    {
      "symbol": "IEX",
      "name": "IDEX Corporation",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Lake Forest, Illinois",
      "CIK": "0000832101"
    },
    {
      "symbol": "IDXX",
      "name": "IDEXX Laboratories",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Westbrook, Maine",
      "CIK": "0000874716"
    },
    {
      "symbol": "INFO",
      "name": "IHS Markit Ltd.",
      "sector": "Industrials",
      "industry": "Research & Consulting Services",
      "headquarters": "London, United Kingdom",
      "CIK": "0001598014"
    },
    {
      "symbol": "ITW",
      "name": "Illinois Tool Works",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Glenview, Illinois",
      "CIK": "0000049826"
    },
    {
      "symbol": "ILMN",
      "name": "Illumina Inc",
      "sector": "Health Care",
      "industry": "Life Sciences Tools & Services",
      "headquarters": "San Diego, California",
      "CIK": "0001110803"
    },
    {
      "symbol": "INCY",
      "name": "Incyte",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Wilmington, Delaware",
      "CIK": "0000879169"
    },
    {
      "symbol": "IR",
      "name": "Ingersoll-Rand PLC",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001466258"
    },
    {
      "symbol": "INTC",
      "name": "Intel Corp.",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Santa Clara, California",
      "CIK": "0000050863"
    },
    {
      "symbol": "ICE",
      "name": "Intercontinental Exchange",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0001571949"
    },
    {
      "symbol": "IBM",
      "name": "International Business Machines",
      "sector": "Information Technology",
      "industry": "IT Consulting & Other Services",
      "headquarters": "Armonk, New York",
      "CIK": "0000051143"
    },
    {
      "symbol": "IP",
      "name": "International Paper",
      "sector": "Materials",
      "industry": "Paper Packaging",
      "headquarters": "Memphis, Tennessee",
      "CIK": "0000051434"
    },
    {
      "symbol": "IPG",
      "name": "Interpublic Group",
      "sector": "Communication Services",
      "industry": "Advertising",
      "headquarters": "New York, New York",
      "CIK": "0000051644"
    },
    {
      "symbol": "IFF",
      "name": "Intl Flavors & Fragrances",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "New York, New York",
      "CIK": "0000051253"
    },
    {
      "symbol": "INTU",
      "name": "Intuit Inc.",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Mountain View, California",
      "CIK": "0000896878"
    },
    {
      "symbol": "ISRG",
      "name": "Intuitive Surgical Inc.",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Sunnyvale, California",
      "CIK": "0001035267"
    },
    {
      "symbol": "IVZ",
      "name": "Invesco Ltd.",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000914208"
    },
    {
      "symbol": "IPGP",
      "name": "IPG Photonics Corp.",
      "sector": "Information Technology",
      "industry": "Electronic Manufacturing Services",
      "headquarters": "Oxford, Massachusetts",
      "CIK": "0001111928"
    },
    {
      "symbol": "IQV",
      "name": "IQVIA Holdings Inc.",
      "sector": "Health Care",
      "industry": "Life Sciences Tools & Services",
      "headquarters": "Durham, North Carolina",
      "CIK": "0001478242"
    },
    {
      "symbol": "IRM",
      "name": "Iron Mountain Incorporated",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Boston, Massachusetts",
      "CIK": "0001020569"
    },
    {
      "symbol": "JBHT",
      "name": "J. B. Hunt Transport Services",
      "sector": "Industrials",
      "industry": "Trucking",
      "headquarters": "Lowell, Arkansas",
      "CIK": "0000728535"
    },
    {
      "symbol": "JKHY",
      "name": "Jack Henry & Associates",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Monett, Missouri",
      "CIK": "0000779152"
    },
    {
      "symbol": "J",
      "name": "Jacobs Engineering Group",
      "sector": "Industrials",
      "industry": "Construction & Engineering",
      "headquarters": "Pasadena, California",
      "CIK": "0000052988"
    },
    {
      "symbol": "SJM",
      "name": "JM Smucker",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Orrville, Ohio",
      "CIK": "0000091419"
    },
    {
      "symbol": "JNJ",
      "name": "Johnson & Johnson",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "New Brunswick, New Jersey",
      "CIK": "0000200406"
    },
    {
      "symbol": "JCI",
      "name": "Johnson Controls International",
      "sector": "Industrials",
      "industry": "Building Products",
      "headquarters": "Cork, Ireland",
      "CIK": "0000833444"
    },
    {
      "symbol": "JPM",
      "name": "JPMorgan Chase & Co.",
      "sector": "Financials",
      "industry": "Diversified Banks",
      "headquarters": "New York, New York",
      "CIK": "0000019617"
    },
    {
      "symbol": "JNPR",
      "name": "Juniper Networks",
      "sector": "Information Technology",
      "industry": "Communications Equipment",
      "headquarters": "Sunnyvale, California",
      "CIK": "0001043604"
    },
    {
      "symbol": "KSU",
      "name": "Kansas City Southern",
      "sector": "Industrials",
      "industry": "Railroads",
      "headquarters": "Kansas City, Missouri",
      "CIK": "0000054480"
    },
    {
      "symbol": "K",
      "name": "Kellogg Co.",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Battle Creek, Michigan",
      "CIK": "0000055067"
    },
    {
      "symbol": "KEY",
      "name": "KeyCorp",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Cleveland, Ohio",
      "CIK": "0000091576"
    },
    {
      "symbol": "KEYS",
      "name": "Keysight Technologies",
      "sector": "Information Technology",
      "industry": "Electronic Equipment & Instruments",
      "headquarters": "Santa Rosa, California",
      "CIK": "0001601046"
    },
    {
      "symbol": "KMB",
      "name": "Kimberly-Clark",
      "sector": "Consumer Staples",
      "industry": "Household Products",
      "headquarters": "Irving, Texas",
      "CIK": "0000055785"
    },
    {
      "symbol": "KIM",
      "name": "Kimco Realty",
      "sector": "Real Estate",
      "industry": "Retail REITs",
      "headquarters": "New Hyde Park, New York",
      "CIK": "0000879101"
    },
    {
      "symbol": "KMI",
      "name": "Kinder Morgan",
      "sector": "Energy",
      "industry": "Oil & Gas Storage & Transportation",
      "headquarters": "Houston, Texas",
      "CIK": "0001506307"
    },
    {
      "symbol": "KLAC",
      "name": "KLA Corporation",
      "sector": "Information Technology",
      "industry": "Semiconductor Equipment",
      "headquarters": "Milpitas, California",
      "CIK": "0000319201"
    },
    {
      "symbol": "KSS",
      "name": "Kohl's Corp.",
      "sector": "Consumer Discretionary",
      "industry": "General Merchandise Stores",
      "headquarters": "Menomonee Falls, Wisconsin",
      "CIK": "0000885639"
    },
    {
      "symbol": "KHC",
      "name": "Kraft Heinz Co",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Chicago, Illinois; Pittsburgh, Pennsylvania",
      "CIK": "0001637459"
    },
    {
      "symbol": "KR",
      "name": "Kroger Co.",
      "sector": "Consumer Staples",
      "industry": "Food Retail",
      "headquarters": "Cincinnati, Ohio",
      "CIK": "0000056873"
    },
    {
      "symbol": "LB",
      "name": "L Brands Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel Retail",
      "headquarters": "Columbus, Ohio",
      "CIK": "0000701985"
    },
    {
      "symbol": "LHX",
      "name": "L3Harris Technologies",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Melbourne, Florida",
      "CIK": "0000202058"
    },
    {
      "symbol": "LH",
      "name": "Laboratory Corp. of America Holding",
      "sector": "Health Care",
      "industry": "Health Care Services",
      "headquarters": "Burlington, North Carolina",
      "CIK": "0000920148"
    },
    {
      "symbol": "LRCX",
      "name": "Lam Research",
      "sector": "Information Technology",
      "industry": "Semiconductor Equipment",
      "headquarters": "Fremont, California",
      "CIK": "0000707549"
    },
    {
      "symbol": "LW",
      "name": "Lamb Weston Holdings Inc",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Eagle, Idaho",
      "CIK": "0001679273"
    },
    {
      "symbol": "LVS",
      "name": "Las Vegas Sands",
      "sector": "Consumer Discretionary",
      "industry": "Casinos & Gaming",
      "headquarters": "Las Vegas, Nevada",
      "CIK": "0001300514"
    },
    {
      "symbol": "LEG",
      "name": "Leggett & Platt",
      "sector": "Consumer Discretionary",
      "industry": "Home Furnishings",
      "headquarters": "Carthage, Missouri",
      "CIK": "0000058492"
    },
    {
      "symbol": "LDOS",
      "name": "Leidos Holdings",
      "sector": "Information Technology",
      "industry": "IT Consulting & Other Services",
      "headquarters": "Reston, Virginia",
      "CIK": "0001336920"
    },
    {
      "symbol": "LEN",
      "name": "Lennar Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Homebuilding",
      "headquarters": "Miami, Florida",
      "CIK": "0000920760"
    },
    {
      "symbol": "LLY",
      "name": "Lilly (Eli) & Co.",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "Indianapolis, Indiana",
      "CIK": "0000059478"
    },
    {
      "symbol": "LNC",
      "name": "Lincoln National",
      "sector": "Financials",
      "industry": "Multi-line Insurance",
      "headquarters": "Radnor, Pennsylvania",
      "CIK": "0000059558"
    },
    {
      "symbol": "LIN",
      "name": "Linde plc",
      "sector": "Materials",
      "industry": "Industrial Gases",
      "headquarters": "Guildford, Surrey, United Kingdom",
      "CIK": "0001707925"
    },
    {
      "symbol": "LYV",
      "name": "Live Nation Entertainment",
      "sector": "Communication Services",
      "industry": "Movies & Entertainment",
      "headquarters": "Beverly Hills, California",
      "CIK": "0001335258"
    },
    {
      "symbol": "LKQ",
      "name": "LKQ Corporation",
      "sector": "Consumer Discretionary",
      "industry": "Distributors",
      "headquarters": "Chicago, Illinois",
      "CIK": "0001065696"
    },
    {
      "symbol": "LMT",
      "name": "Lockheed Martin Corp.",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Bethesda, Maryland",
      "CIK": "0000936468"
    },
    {
      "symbol": "L",
      "name": "Loews Corp.",
      "sector": "Financials",
      "industry": "Multi-line Insurance",
      "headquarters": "New York, New York",
      "CIK": "0000060086"
    },
    {
      "symbol": "LOW",
      "name": "Lowe's Cos.",
      "sector": "Consumer Discretionary",
      "industry": "Home Improvement Retail",
      "headquarters": "Mooresville, North Carolina",
      "CIK": "0000060667"
    },
    {
      "symbol": "LYB",
      "name": "LyondellBasell",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "Rotterdam, Netherlands",
      "CIK": "0001489393"
    },
    {
      "symbol": "MTB",
      "name": "M&T Bank Corp.",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Buffalo, New York",
      "CIK": "0000036270"
    },
    {
      "symbol": "M",
      "name": "Macy's Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Department Stores",
      "headquarters": "Cincinnati, Ohio",
      "CIK": "0000794367"
    },
    {
      "symbol": "MRO",
      "name": "Marathon Oil Corp.",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0000101778"
    },
    {
      "symbol": "MPC",
      "name": "Marathon Petroleum",
      "sector": "Energy",
      "industry": "Oil & Gas Refining & Marketing",
      "headquarters": "Findlay, Ohio",
      "CIK": "0001510295"
    },
    {
      "symbol": "MKTX",
      "name": "MarketAxess",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "New York, New York",
      "CIK": "0001278021"
    },
    {
      "symbol": "MAR",
      "name": "Marriott Int'l.",
      "sector": "Consumer Discretionary",
      "industry": "Hotels, Resorts & Cruise Lines",
      "headquarters": "Bethesda, Maryland",
      "CIK": "0001048286"
    },
    {
      "symbol": "MMC",
      "name": "Marsh & McLennan",
      "sector": "Financials",
      "industry": "Insurance Brokers",
      "headquarters": "New York, New York",
      "CIK": "0000062709"
    },
    {
      "symbol": "MLM",
      "name": "Martin Marietta Materials",
      "sector": "Materials",
      "industry": "Construction Materials",
      "headquarters": "Raleigh, North Carolina",
      "CIK": "0000916076"
    },
    {
      "symbol": "MAS",
      "name": "Masco Corp.",
      "sector": "Industrials",
      "industry": "Building Products",
      "headquarters": "Taylor, Michigan",
      "CIK": "0000062996"
    },
    {
      "symbol": "MA",
      "name": "Mastercard Inc.",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Harrison, New York",
      "CIK": "0001141391"
    },
    {
      "symbol": "MXIM",
      "name": "Maxim Integrated Products Inc",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "San Jose, California",
      "CIK": "0000743316"
    },
    {
      "symbol": "MKC",
      "name": "McCormick & Co.",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Sparks, Maryland",
      "CIK": "0000063754"
    },
    {
      "symbol": "MCD",
      "name": "McDonald's Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Restaurants",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000063908"
    },
    {
      "symbol": "MCK",
      "name": "McKesson Corp.",
      "sector": "Health Care",
      "industry": "Health Care Distributors",
      "headquarters": "Irving, Texas",
      "CIK": "0000927653"
    },
    {
      "symbol": "MDT",
      "name": "Medtronic plc",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001613103"
    },
    {
      "symbol": "MRK",
      "name": "Merck & Co.",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "Whitehouse Station, New Jersey",
      "CIK": "0000310158"
    },
    {
      "symbol": "MET",
      "name": "MetLife Inc.",
      "sector": "Financials",
      "industry": "Life & Health Insurance",
      "headquarters": "New York, New York",
      "CIK": "0001099219"
    },
    {
      "symbol": "MTD",
      "name": "Mettler Toledo",
      "sector": "Health Care",
      "industry": "Life Sciences Tools & Services",
      "headquarters": "Columbus, Ohio",
      "CIK": "0001037646"
    },
    {
      "symbol": "MGM",
      "name": "MGM Resorts International",
      "sector": "Consumer Discretionary",
      "industry": "Casinos & Gaming",
      "headquarters": "Paradise, Nevada",
      "CIK": "0000789570"
    },
    {
      "symbol": "MCHP",
      "name": "Microchip Technology",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Chandler, Arizona",
      "CIK": "0000827054"
    },
    {
      "symbol": "MU",
      "name": "Micron Technology",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Boise, Idaho",
      "CIK": "0000723125"
    },
    {
      "symbol": "MSFT",
      "name": "Microsoft Corp.",
      "sector": "Information Technology",
      "industry": "Systems Software",
      "headquarters": "Redmond, Washington",
      "CIK": "0000789019"
    },
    {
      "symbol": "MAA",
      "name": "Mid-America Apartments",
      "sector": "Real Estate",
      "industry": "Residential REITs",
      "headquarters": "Memphis, Tennessee",
      "CIK": "0000912595"
    },
    {
      "symbol": "MHK",
      "name": "Mohawk Industries",
      "sector": "Consumer Discretionary",
      "industry": "Home Furnishings",
      "headquarters": "Amsterdam, New York",
      "CIK": "0000851968"
    },
    {
      "symbol": "TAP",
      "name": "Molson Coors Brewing Company",
      "sector": "Consumer Staples",
      "industry": "Brewers",
      "headquarters": "Denver, Colorado",
      "CIK": "0000024545"
    },
    {
      "symbol": "MDLZ",
      "name": "Mondelez International",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Deerfield, Illinois",
      "CIK": "0001103982"
    },
    {
      "symbol": "MNST",
      "name": "Monster Beverage",
      "sector": "Consumer Staples",
      "industry": "Soft Drinks",
      "headquarters": "Corona, California",
      "CIK": "0000865752"
    },
    {
      "symbol": "MCO",
      "name": "Moody's Corp",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "New York, New York",
      "CIK": "0001059556"
    },
    {
      "symbol": "MS",
      "name": "Morgan Stanley",
      "sector": "Financials",
      "industry": "Investment Banking & Brokerage",
      "headquarters": "New York, New York",
      "CIK": "0000895421"
    },
    {
      "symbol": "MSI",
      "name": "Motorola Solutions Inc.",
      "sector": "Information Technology",
      "industry": "Communications Equipment",
      "headquarters": "Schaumburg, Illinois",
      "CIK": "0000068505"
    },
    {
      "symbol": "MSCI",
      "name": "MSCI Inc",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "New York, New York",
      "CIK": "0001408198"
    },
    {
      "symbol": "MYL",
      "name": "Mylan N.V.",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "Amsterdam, Netherlands",
      "CIK": "0001623613"
    },
    {
      "symbol": "NDAQ",
      "name": "Nasdaq, Inc.",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "New York, New York",
      "CIK": "0001120193"
    },
    {
      "symbol": "NOV",
      "name": "National Oilwell Varco Inc.",
      "sector": "Energy",
      "industry": "Oil & Gas Equipment & Services",
      "headquarters": "Houston, Texas",
      "CIK": "0001021860"
    },
    {
      "symbol": "NTAP",
      "name": "NetApp",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Sunnyvale, California",
      "CIK": "0001002047"
    },
    {
      "symbol": "NFLX",
      "name": "Netflix Inc.",
      "sector": "Communication Services",
      "industry": "Movies & Entertainment",
      "headquarters": "Los Gatos, California",
      "CIK": "0001065280"
    },
    {
      "symbol": "NWL",
      "name": "Newell Brands",
      "sector": "Consumer Discretionary",
      "industry": "Housewares & Specialties",
      "headquarters": "Hoboken, New Jersey",
      "CIK": "0000814453"
    },
    {
      "symbol": "NEM",
      "name": "Newmont Corporation",
      "sector": "Materials",
      "industry": "Gold",
      "headquarters": "Denver, Colorado",
      "CIK": "0001164727"
    },
    {
      "symbol": "NWSA",
      "name": "News Corp. Class A",
      "sector": "Communication Services",
      "industry": "Publishing",
      "headquarters": "New York, New York",
      "CIK": "0001564708"
    },
    {
      "symbol": "NWS",
      "name": "News Corp. Class B",
      "sector": "Communication Services",
      "industry": "Publishing",
      "headquarters": "New York, New York",
      "CIK": "0001564708"
    },
    {
      "symbol": "NEE",
      "name": "NextEra Energy",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Juno Beach, Florida",
      "CIK": "0000753308"
    },
    {
      "symbol": "NLSN",
      "name": "Nielsen Holdings",
      "sector": "Industrials",
      "industry": "Research & Consulting Services",
      "headquarters": "New York, New York",
      "CIK": "0001492633"
    },
    {
      "symbol": "NKE",
      "name": "Nike",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "Washington County, Oregon",
      "CIK": "0000320187"
    },
    {
      "symbol": "NI",
      "name": "NiSource Inc.",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Merrillville, Indiana",
      "CIK": "0001111711"
    },
    {
      "symbol": "NBL",
      "name": "Noble Energy Inc",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0000072207"
    },
    {
      "symbol": "JWN",
      "name": "Nordstrom",
      "sector": "Consumer Discretionary",
      "industry": "Department Stores",
      "headquarters": "Seattle, Washington",
      "CIK": "0000072333"
    },
    {
      "symbol": "NSC",
      "name": "Norfolk Southern Corp.",
      "sector": "Industrials",
      "industry": "Railroads",
      "headquarters": "Norfolk, Virginia",
      "CIK": "0000702165"
    },
    {
      "symbol": "NTRS",
      "name": "Northern Trust Corp.",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000073124"
    },
    {
      "symbol": "NOC",
      "name": "Northrop Grumman",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "West Falls Church, Virginia",
      "CIK": "0001133421"
    },
    {
      "symbol": "NLOK",
      "name": "NortonLifeLock",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Tempe, Arizona",
      "CIK": "0000849399"
    },
    {
      "symbol": "NCLH",
      "name": "Norwegian Cruise Line Holdings",
      "sector": "Consumer Discretionary",
      "industry": "Hotels, Resorts & Cruise Lines",
      "headquarters": "Miami, Florida",
      "CIK": "0001513761"
    },
    {
      "symbol": "NRG",
      "name": "NRG Energy",
      "sector": "Utilities",
      "industry": "Independent Power Producers & Energy Traders",
      "headquarters": "Princeton, New Jersey",
      "CIK": "0001013871"
    },
    {
      "symbol": "NUE",
      "name": "Nucor Corp.",
      "sector": "Materials",
      "industry": "Steel",
      "headquarters": "Charlotte, North Carolina",
      "CIK": "0000073309"
    },
    {
      "symbol": "NVDA",
      "name": "Nvidia Corporation",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Santa Clara, California",
      "CIK": "0001045810"
    },
    {
      "symbol": "NVR",
      "name": "NVR Inc",
      "sector": "Consumer Discretionary",
      "industry": "Homebuilding",
      "headquarters": "Reston, VA",
      "CIK": "0000906163"
    },
    {
      "symbol": "ORLY",
      "name": "O'Reilly Automotive",
      "sector": "Consumer Discretionary",
      "industry": "Specialty Stores",
      "headquarters": "Springfield, Missouri",
      "CIK": "0000898173"
    },
    {
      "symbol": "OXY",
      "name": "Occidental Petroleum",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Houston, Texas",
      "CIK": "0000797468"
    },
    {
      "symbol": "ODFL",
      "name": "Old Dominion Freight Line",
      "sector": "Industrials",
      "industry": "Trucking",
      "headquarters": "Thomasville, North Carolina",
      "CIK": "0000878927"
    },
    {
      "symbol": "OMC",
      "name": "Omnicom Group",
      "sector": "Communication Services",
      "industry": "Advertising",
      "headquarters": "New York, New York",
      "CIK": "0000029989"
    },
    {
      "symbol": "OKE",
      "name": "ONEOK",
      "sector": "Energy",
      "industry": "Oil & Gas Storage & Transportation",
      "headquarters": "Tulsa, Oklahoma",
      "CIK": "0001039684"
    },
    {
      "symbol": "ORCL",
      "name": "Oracle Corp.",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Redwood Shores, California",
      "CIK": "0001341439"
    },
    {
      "symbol": "PCAR",
      "name": "PACCAR Inc.",
      "sector": "Industrials",
      "industry": "Construction Machinery & Heavy Trucks",
      "headquarters": "Bellevue, Washington",
      "CIK": "0000075362"
    },
    {
      "symbol": "PKG",
      "name": "Packaging Corporation of America",
      "sector": "Materials",
      "industry": "Paper Packaging",
      "headquarters": "Lake Forest, Illinois",
      "CIK": "0000075677"
    },
    {
      "symbol": "PH",
      "name": "Parker-Hannifin",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Cleveland, Ohio",
      "CIK": "0000076334"
    },
    {
      "symbol": "PAYX",
      "name": "Paychex Inc.",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Penfield, New York",
      "CIK": "0000723531"
    },
    {
      "symbol": "PAYC",
      "name": "Paycom",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Oklahoma City, Oklahoma",
      "CIK": "0001590955"
    },
    {
      "symbol": "PYPL",
      "name": "PayPal",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "San Jose, California",
      "CIK": "0001633917"
    },
    {
      "symbol": "PNR",
      "name": "Pentair plc",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Worsley, UK",
      "CIK": "0000077360"
    },
    {
      "symbol": "PBCT",
      "name": "People's United Financial",
      "sector": "Financials",
      "industry": "Thrifts & Mortgage Finance",
      "headquarters": "Bridgeport, Connecticut",
      "CIK": "0001378946"
    },
    {
      "symbol": "PEP",
      "name": "PepsiCo Inc.",
      "sector": "Consumer Staples",
      "industry": "Soft Drinks",
      "headquarters": "Purchase, New York",
      "CIK": "0000077476"
    },
    {
      "symbol": "PKI",
      "name": "PerkinElmer",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Waltham, Massachusetts",
      "CIK": "0000031791"
    },
    {
      "symbol": "PRGO",
      "name": "Perrigo",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001585364"
    },
    {
      "symbol": "PFE",
      "name": "Pfizer Inc.",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "New York, New York",
      "CIK": "0000078003"
    },
    {
      "symbol": "PM",
      "name": "Philip Morris International",
      "sector": "Consumer Staples",
      "industry": "Tobacco",
      "headquarters": "New York, New York",
      "CIK": "0001413329"
    },
    {
      "symbol": "PSX",
      "name": "Phillips 66",
      "sector": "Energy",
      "industry": "Oil & Gas Refining & Marketing",
      "headquarters": "Houston, Texas",
      "CIK": "0001534701"
    },
    {
      "symbol": "PNW",
      "name": "Pinnacle West Capital",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Phoenix, Arizona",
      "CIK": "0000764622"
    },
    {
      "symbol": "PXD",
      "name": "Pioneer Natural Resources",
      "sector": "Energy",
      "industry": "Oil & Gas Exploration & Production",
      "headquarters": "Irving, Texas",
      "CIK": "0001038357"
    },
    {
      "symbol": "PNC",
      "name": "PNC Financial Services",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Pittsburgh, Pennsylvania",
      "CIK": "0000713676"
    },
    {
      "symbol": "PPG",
      "name": "PPG Industries",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "Pittsburgh, Pennsylvania",
      "CIK": "0000079879"
    },
    {
      "symbol": "PPL",
      "name": "PPL Corp.",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Allentown, Pennsylvania",
      "CIK": "0000922224"
    },
    {
      "symbol": "PFG",
      "name": "Principal Financial Group",
      "sector": "Financials",
      "industry": "Life & Health Insurance",
      "headquarters": "Des Moines, Iowa",
      "CIK": "0001126328"
    },
    {
      "symbol": "PG",
      "name": "Procter & Gamble",
      "sector": "Consumer Staples",
      "industry": "Personal Products",
      "headquarters": "Cincinnati, Ohio",
      "CIK": "0000080424"
    },
    {
      "symbol": "PGR",
      "name": "Progressive Corp.",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "Mayfield Village, Ohio",
      "CIK": "0000080661"
    },
    {
      "symbol": "PLD",
      "name": "Prologis",
      "sector": "Real Estate",
      "industry": "Industrial REITs",
      "headquarters": "San Francisco, California",
      "CIK": "0001045609"
    },
    {
      "symbol": "PRU",
      "name": "Prudential Financial",
      "sector": "Financials",
      "industry": "Life & Health Insurance",
      "headquarters": "Newark, New Jersey",
      "CIK": "0001137774"
    },
    {
      "symbol": "PEG",
      "name": "Public Serv. Enterprise Inc.",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Newark, New Jersey",
      "CIK": "0000788784"
    },
    {
      "symbol": "PSA",
      "name": "Public Storage",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Glendale, California",
      "CIK": "0001393311"
    },
    {
      "symbol": "PHM",
      "name": "Pulte Homes Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Homebuilding",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000822416"
    },
    {
      "symbol": "PVH",
      "name": "PVH Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "New York, New York",
      "CIK": "0000078239"
    },
    {
      "symbol": "QRVO",
      "name": "Qorvo",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Greensboro, North Carolina",
      "CIK": "0001604778"
    },
    {
      "symbol": "QCOM",
      "name": "QUALCOMM Inc.",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "San Diego, California",
      "CIK": "0000804328"
    },
    {
      "symbol": "PWR",
      "name": "Quanta Services Inc.",
      "sector": "Industrials",
      "industry": "Construction & Engineering",
      "headquarters": "Houston, Texas",
      "CIK": "0001050915"
    },
    {
      "symbol": "DGX",
      "name": "Quest Diagnostics",
      "sector": "Health Care",
      "industry": "Health Care Services",
      "headquarters": "Madison, New Jersey",
      "CIK": "0001022079"
    },
    {
      "symbol": "RL",
      "name": "Ralph Lauren Corporation",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "New York, New York",
      "CIK": "0001037038"
    },
    {
      "symbol": "RJF",
      "name": "Raymond James Financial Inc.",
      "sector": "Financials",
      "industry": "Investment Banking & Brokerage",
      "headquarters": "St. Petersburg, Florida",
      "CIK": "0000720005"
    },
    {
      "symbol": "RTN",
      "name": "Raytheon Co.",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Waltham, Massachusetts",
      "CIK": "0001047122"
    },
    {
      "symbol": "O",
      "name": "Realty Income Corporation",
      "sector": "Real Estate",
      "industry": "Retail REITs",
      "headquarters": "San Diego, California",
      "CIK": "0000726728"
    },
    {
      "symbol": "REG",
      "name": "Regency Centers Corporation",
      "sector": "Real Estate",
      "industry": "Retail REITs",
      "headquarters": "Jacksonville, Florida",
      "CIK": "0000910606"
    },
    {
      "symbol": "REGN",
      "name": "Regeneron Pharmaceuticals",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Tarrytown, New York",
      "CIK": "0000872589"
    },
    {
      "symbol": "RF",
      "name": "Regions Financial Corp.",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Birmingham, Alabama",
      "CIK": "0001281761"
    },
    {
      "symbol": "RSG",
      "name": "Republic Services Inc",
      "sector": "Industrials",
      "industry": "Environmental & Facilities Services",
      "headquarters": "Phoenix, Arizona",
      "CIK": "0001060391"
    },
    {
      "symbol": "RMD",
      "name": "ResMed",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "San Diego, California",
      "CIK": "0000943819"
    },
    {
      "symbol": "RHI",
      "name": "Robert Half International",
      "sector": "Industrials",
      "industry": "Human Resource & Employment Services",
      "headquarters": "Menlo Park, California",
      "CIK": "0000315213"
    },
    {
      "symbol": "ROK",
      "name": "Rockwell Automation Inc.",
      "sector": "Industrials",
      "industry": "Electrical Components & Equipment",
      "headquarters": "Milwaukee, Wisconsin",
      "CIK": "0001024478"
    },
    {
      "symbol": "ROL",
      "name": "Rollins Inc.",
      "sector": "Industrials",
      "industry": "Environmental & Facilities Services",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000084839"
    },
    {
      "symbol": "ROP",
      "name": "Roper Technologies",
      "sector": "Industrials",
      "industry": "Industrial Conglomerates",
      "headquarters": "Sarasota, Florida",
      "CIK": "0000882835"
    },
    {
      "symbol": "ROST",
      "name": "Ross Stores",
      "sector": "Consumer Discretionary",
      "industry": "Apparel Retail",
      "headquarters": "Pleasanton, California",
      "CIK": "0000745732"
    },
    {
      "symbol": "RCL",
      "name": "Royal Caribbean Cruises Ltd",
      "sector": "Consumer Discretionary",
      "industry": "Hotels, Resorts & Cruise Lines",
      "headquarters": "Miami, Florida",
      "CIK": "0000884887"
    },
    {
      "symbol": "SPGI",
      "name": "S&P Global, Inc.",
      "sector": "Financials",
      "industry": "Financial Exchanges & Data",
      "headquarters": "New York, New York",
      "CIK": "0000064040"
    },
    {
      "symbol": "CRM",
      "name": "Salesforce.com",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "San Francisco, California",
      "CIK": "0001108524"
    },
    {
      "symbol": "SBAC",
      "name": "SBA Communications",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Boca Raton, Florida",
      "CIK": "0001034054"
    },
    {
      "symbol": "SLB",
      "name": "Schlumberger Ltd.",
      "sector": "Energy",
      "industry": "Oil & Gas Equipment & Services",
      "headquarters": "Curaçao, Kingdom of the Netherlands",
      "CIK": "0000087347"
    },
    {
      "symbol": "STX",
      "name": "Seagate Technology",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001137789"
    },
    {
      "symbol": "SEE",
      "name": "Sealed Air",
      "sector": "Materials",
      "industry": "Paper Packaging",
      "headquarters": "Elmwood Park, New Jersey",
      "CIK": "0001012100"
    },
    {
      "symbol": "SRE",
      "name": "Sempra Energy",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "San Diego, California",
      "CIK": "0001032208"
    },
    {
      "symbol": "NOW",
      "name": "ServiceNow",
      "sector": "Information Technology",
      "industry": "Systems Software",
      "headquarters": "Santa Clara, California",
      "CIK": "0001373715"
    },
    {
      "symbol": "SHW",
      "name": "Sherwin-Williams",
      "sector": "Materials",
      "industry": "Specialty Chemicals",
      "headquarters": "Cleveland, Ohio",
      "CIK": "0000089800"
    },
    {
      "symbol": "SPG",
      "name": "Simon Property Group Inc",
      "sector": "Real Estate",
      "industry": "Retail REITs",
      "headquarters": "Indianapolis, Indiana",
      "CIK": "0001063761"
    },
    {
      "symbol": "SWKS",
      "name": "Skyworks Solutions",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Woburn, Massachusetts",
      "CIK": "0000004127"
    },
    {
      "symbol": "SLG",
      "name": "SL Green Realty",
      "sector": "Real Estate",
      "industry": "Office REITs",
      "headquarters": "New York, New York",
      "CIK": "0001040971"
    },
    {
      "symbol": "SNA",
      "name": "Snap-on",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "Kenosha, Wisconsin",
      "CIK": "0000091440"
    },
    {
      "symbol": "SO",
      "name": "Southern Co.",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0000092122"
    },
    {
      "symbol": "LUV",
      "name": "Southwest Airlines",
      "sector": "Industrials",
      "industry": "Airlines",
      "headquarters": "Dallas, Texas",
      "CIK": "0000092380"
    },
    {
      "symbol": "SWK",
      "name": "Stanley Black & Decker",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "New Britain, Connecticut",
      "CIK": "0000093556"
    },
    {
      "symbol": "SBUX",
      "name": "Starbucks Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Restaurants",
      "headquarters": "Seattle, Washington",
      "CIK": "0000829224"
    },
    {
      "symbol": "STT",
      "name": "State Street Corp.",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "Boston, Massachusetts",
      "CIK": "0000093751"
    },
    {
      "symbol": "STE",
      "name": "STERIS plc",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Dublin, Ireland",
      "CIK": "0001757898"
    },
    {
      "symbol": "SYK",
      "name": "Stryker Corp.",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Kalamazoo, Michigan",
      "CIK": "0000310764"
    },
    {
      "symbol": "SIVB",
      "name": "SVB Financial",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Santa Clara, California",
      "CIK": "0000719739"
    },
    {
      "symbol": "SYF",
      "name": "Synchrony Financial",
      "sector": "Financials",
      "industry": "Consumer Finance",
      "headquarters": "Stamford, Connecticut",
      "CIK": "0001601712"
    },
    {
      "symbol": "SNPS",
      "name": "Synopsys Inc.",
      "sector": "Information Technology",
      "industry": "Application Software",
      "headquarters": "Mountain View, California",
      "CIK": "0000883241"
    },
    {
      "symbol": "SYY",
      "name": "Sysco Corp.",
      "sector": "Consumer Staples",
      "industry": "Food Distributors",
      "headquarters": "Houston, Texas",
      "CIK": "0000096021"
    },
    {
      "symbol": "TMUS",
      "name": "T-Mobile US",
      "sector": "Communication Services",
      "industry": "Wireless Telecommunication Services",
      "headquarters": "Bellevue, Washington",
      "CIK": "0001283699"
    },
    {
      "symbol": "TROW",
      "name": "T. Rowe Price Group",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "Baltimore, Maryland",
      "CIK": "0001113169"
    },
    {
      "symbol": "TTWO",
      "name": "Take-Two Interactive",
      "sector": "Communication Services",
      "industry": "Interactive Home Entertainment",
      "headquarters": "New York, New York",
      "CIK": "0000946581"
    },
    {
      "symbol": "TPR",
      "name": "Tapestry, Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "New York, New York",
      "CIK": "0001116132"
    },
    {
      "symbol": "TGT",
      "name": "Target Corp.",
      "sector": "Consumer Discretionary",
      "industry": "General Merchandise Stores",
      "headquarters": "Minneapolis, Minnesota",
      "CIK": "0000027419"
    },
    {
      "symbol": "TEL",
      "name": "TE Connectivity Ltd.",
      "sector": "Information Technology",
      "industry": "Electronic Manufacturing Services",
      "headquarters": "Schaffhausen, Switzerland",
      "CIK": "0001385157"
    },
    {
      "symbol": "FTI",
      "name": "TechnipFMC",
      "sector": "Energy",
      "industry": "Oil & Gas Equipment & Services",
      "headquarters": "London, United Kingdom",
      "CIK": "0001681459"
    },
    {
      "symbol": "TFX",
      "name": "Teleflex",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Wayne, Pennsylvania",
      "CIK": "0000096943"
    },
    {
      "symbol": "TXN",
      "name": "Texas Instruments",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "Dallas, Texas",
      "CIK": "0000097476"
    },
    {
      "symbol": "TXT",
      "name": "Textron Inc.",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Providence, Rhode Island",
      "CIK": "0000217346"
    },
    {
      "symbol": "BK",
      "name": "The Bank of New York Mellon Corp.",
      "sector": "Financials",
      "industry": "Asset Management & Custody Banks",
      "headquarters": "New York, New York",
      "CIK": "0001390777"
    },
    {
      "symbol": "CLX",
      "name": "The Clorox Company",
      "sector": "Consumer Staples",
      "industry": "Household Products",
      "headquarters": "Oakland, California",
      "CIK": "0000021076"
    },
    {
      "symbol": "COO",
      "name": "The Cooper Companies",
      "sector": "Health Care",
      "industry": "Health Care Supplies",
      "headquarters": "San Ramon, California",
      "CIK": "0000711404"
    },
    {
      "symbol": "HSY",
      "name": "The Hershey Company",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Hershey, Pennsylvania",
      "CIK": "0000047111"
    },
    {
      "symbol": "MOS",
      "name": "The Mosaic Company",
      "sector": "Materials",
      "industry": "Fertilizers & Agricultural Chemicals",
      "headquarters": "Plymouth, Minnesota",
      "CIK": "0001285785"
    },
    {
      "symbol": "TRV",
      "name": "The Travelers Companies Inc.",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "New York, New York",
      "CIK": "0000086312"
    },
    {
      "symbol": "DIS",
      "name": "The Walt Disney Company",
      "sector": "Communication Services",
      "industry": "Movies & Entertainment",
      "headquarters": "Burbank, California",
      "CIK": "0001001039"
    },
    {
      "symbol": "TMO",
      "name": "Thermo Fisher Scientific",
      "sector": "Health Care",
      "industry": "Life Sciences Tools & Services",
      "headquarters": "Waltham, Massachusetts",
      "CIK": "0000097745"
    },
    {
      "symbol": "TIF",
      "name": "Tiffany & Co.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "New York, New York",
      "CIK": "0000098246"
    },
    {
      "symbol": "TJX",
      "name": "TJX Companies Inc.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel Retail",
      "headquarters": "Framingham, Massachusetts",
      "CIK": "0000109198"
    },
    {
      "symbol": "TSCO",
      "name": "Tractor Supply Company",
      "sector": "Consumer Discretionary",
      "industry": "Specialty Stores",
      "headquarters": "Brentwood, Tennessee",
      "CIK": "0000916365"
    },
    {
      "symbol": "TDG",
      "name": "TransDigm Group",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Cleveland, Ohio",
      "CIK": "0001260221"
    },
    {
      "symbol": "TFC",
      "name": "Truist Financial",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Charlotte, North Carolina",
      "CIK": "0000092230"
    },
    {
      "symbol": "TWTR",
      "name": "Twitter, Inc.",
      "sector": "Communication Services",
      "industry": "Interactive Media & Services",
      "headquarters": "San Francisco, California",
      "CIK": "0001418091"
    },
    {
      "symbol": "TSN",
      "name": "Tyson Foods",
      "sector": "Consumer Staples",
      "industry": "Packaged Foods & Meats",
      "headquarters": "Springdale, Arkansas",
      "CIK": "0000100493"
    },
    {
      "symbol": "USB",
      "name": "U.S. Bancorp",
      "sector": "Financials",
      "industry": "Diversified Banks",
      "headquarters": "Minneapolis, Minnesota",
      "CIK": "0000036104"
    },
    {
      "symbol": "UDR",
      "name": "UDR, Inc.",
      "sector": "Real Estate",
      "industry": "Residential REITs",
      "headquarters": "Highlands Ranch, Colorado",
      "CIK": "0000074208"
    },
    {
      "symbol": "ULTA",
      "name": "Ulta Beauty",
      "sector": "Consumer Discretionary",
      "industry": "Specialty Stores",
      "headquarters": "Bolingbrook, Illinois",
      "CIK": "0001403568"
    },
    {
      "symbol": "UAA",
      "name": "Under Armour Class A",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "Baltimore, Maryland",
      "CIK": "0001336917"
    },
    {
      "symbol": "UA",
      "name": "Under Armour Class C",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "Baltimore, Maryland",
      "CIK": "0001336917"
    },
    {
      "symbol": "UNP",
      "name": "Union Pacific Corp",
      "sector": "Industrials",
      "industry": "Railroads",
      "headquarters": "Omaha, Nebraska",
      "CIK": "0000100885"
    },
    {
      "symbol": "UAL",
      "name": "United Airlines Holdings",
      "sector": "Industrials",
      "industry": "Airlines",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000100517"
    },
    {
      "symbol": "UNH",
      "name": "United Health Group Inc.",
      "sector": "Health Care",
      "industry": "Managed Health Care",
      "headquarters": "Minnetonka, Minnesota",
      "CIK": "0000731766"
    },
    {
      "symbol": "UPS",
      "name": "United Parcel Service",
      "sector": "Industrials",
      "industry": "Air Freight & Logistics",
      "headquarters": "Atlanta, Georgia",
      "CIK": "0001090727"
    },
    {
      "symbol": "URI",
      "name": "United Rentals, Inc.",
      "sector": "Industrials",
      "industry": "Trading Companies & Distributors",
      "headquarters": "Stamford, Connecticut",
      "CIK": "0001067701"
    },
    {
      "symbol": "UTX",
      "name": "United Technologies",
      "sector": "Industrials",
      "industry": "Aerospace & Defense",
      "headquarters": "Hartford, Connecticut",
      "CIK": "0000101829"
    },
    {
      "symbol": "UHS",
      "name": "Universal Health Services, Inc.",
      "sector": "Health Care",
      "industry": "Health Care Facilities",
      "headquarters": "King of Prussia, Pennsylvania",
      "CIK": "0000352915"
    },
    {
      "symbol": "UNM",
      "name": "Unum Group",
      "sector": "Financials",
      "industry": "Life & Health Insurance",
      "headquarters": "Chattanooga, Tennessee",
      "CIK": "0000005513"
    },
    {
      "symbol": "VFC",
      "name": "V.F. Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Apparel, Accessories & Luxury Goods",
      "headquarters": "Greensboro, North Carolina",
      "CIK": "0000103379"
    },
    {
      "symbol": "VLO",
      "name": "Valero Energy",
      "sector": "Energy",
      "industry": "Oil & Gas Refining & Marketing",
      "headquarters": "San Antonio, Texas",
      "CIK": "0001035002"
    },
    {
      "symbol": "VAR",
      "name": "Varian Medical Systems",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Palo Alto, California",
      "CIK": "0000203527"
    },
    {
      "symbol": "VTR",
      "name": "Ventas Inc",
      "sector": "Real Estate",
      "industry": "Health Care REITs",
      "headquarters": "Chicago, Illinois",
      "CIK": "0000740260"
    },
    {
      "symbol": "VRSN",
      "name": "Verisign Inc.",
      "sector": "Information Technology",
      "industry": "Internet Services & Infrastructure",
      "headquarters": "Dulles, Virginia",
      "CIK": "0001014473"
    },
    {
      "symbol": "VRSK",
      "name": "Verisk Analytics",
      "sector": "Industrials",
      "industry": "Research & Consulting Services",
      "headquarters": "Jersey City, New Jersey",
      "CIK": "0001442145"
    },
    {
      "symbol": "VZ",
      "name": "Verizon Communications",
      "sector": "Communication Services",
      "industry": "Integrated Telecommunication Services",
      "headquarters": "New York, New York",
      "CIK": "0000732712"
    },
    {
      "symbol": "VRTX",
      "name": "Vertex Pharmaceuticals Inc",
      "sector": "Health Care",
      "industry": "Biotechnology",
      "headquarters": "Cambridge, Massachusetts",
      "CIK": "0000875320"
    },
    {
      "symbol": "VIAC",
      "name": "ViacomCBS",
      "sector": "Communication Services",
      "industry": "Movies & Entertainment",
      "headquarters": "New York, New York",
      "CIK": "0001339947"
    },
    {
      "symbol": "V",
      "name": "Visa Inc.",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "San Francisco, California",
      "CIK": "0001403161"
    },
    {
      "symbol": "VNO",
      "name": "Vornado Realty Trust",
      "sector": "Real Estate",
      "industry": "Office REITs",
      "headquarters": "New York, New York",
      "CIK": "0000899689"
    },
    {
      "symbol": "VMC",
      "name": "Vulcan Materials",
      "sector": "Materials",
      "industry": "Construction Materials",
      "headquarters": "Birmingham, Alabama",
      "CIK": "0001396009"
    },
    {
      "symbol": "WRB",
      "name": "W. R. Berkley Corporation",
      "sector": "Financials",
      "industry": "Property & Casualty Insurance",
      "headquarters": "Greenwich, Connecticut",
      "CIK": "0000011544"
    },
    {
      "symbol": "WAB",
      "name": "Wabtec Corporation",
      "sector": "Industrials",
      "industry": "Construction Machinery & Heavy Trucks",
      "headquarters": "Wilmerding, Pennsylvania",
      "CIK": "0000943452"
    },
    {
      "symbol": "WBA",
      "name": "Walgreens Boots Alliance",
      "sector": "Consumer Staples",
      "industry": "Drug Retail",
      "headquarters": "Deerfield, Illinois",
      "CIK": "0001618921"
    },
    {
      "symbol": "WMT",
      "name": "Walmart",
      "sector": "Consumer Staples",
      "industry": "Hypermarkets & Super Centers",
      "headquarters": "Bentonville, Arkansas",
      "CIK": "0000104169"
    },
    {
      "symbol": "WM",
      "name": "Waste Management Inc.",
      "sector": "Industrials",
      "industry": "Environmental & Facilities Services",
      "headquarters": "Houston, Texas",
      "CIK": "0000823768"
    },
    {
      "symbol": "WAT",
      "name": "Waters Corporation",
      "sector": "Health Care",
      "industry": "Health Care Distributors",
      "headquarters": "Milford, Massachusetts",
      "CIK": "0001000697"
    },
    {
      "symbol": "WEC",
      "name": "Wec Energy Group Inc",
      "sector": "Utilities",
      "industry": "Electric Utilities",
      "headquarters": "Milwaukee, Wisconsin",
      "CIK": "0000783325"
    },
    {
      "symbol": "WFC",
      "name": "Wells Fargo",
      "sector": "Financials",
      "industry": "Diversified Banks",
      "headquarters": "San Francisco, California",
      "CIK": "0000072971"
    },
    {
      "symbol": "WELL",
      "name": "Welltower Inc.",
      "sector": "Real Estate",
      "industry": "Health Care REITs",
      "headquarters": "Toledo, Ohio",
      "CIK": "0000766704"
    },
    {
      "symbol": "WDC",
      "name": "Western Digital",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Irvine, California",
      "CIK": "0000106040"
    },
    {
      "symbol": "WU",
      "name": "Western Union Co",
      "sector": "Information Technology",
      "industry": "Data Processing & Outsourced Services",
      "headquarters": "Englewood, Colorado",
      "CIK": "0001365135"
    },
    {
      "symbol": "WRK",
      "name": "WestRock",
      "sector": "Materials",
      "industry": "Paper Packaging",
      "headquarters": "Richmond, Virginia",
      "CIK": "0001636023"
    },
    {
      "symbol": "WY",
      "name": "Weyerhaeuser",
      "sector": "Real Estate",
      "industry": "Specialized REITs",
      "headquarters": "Federal Way, Washington",
      "CIK": "0000106535"
    },
    {
      "symbol": "WHR",
      "name": "Whirlpool Corp.",
      "sector": "Consumer Discretionary",
      "industry": "Household Appliances",
      "headquarters": "Benton Harbor, Michigan",
      "CIK": "0000106640"
    },
    {
      "symbol": "WMB",
      "name": "Williams Cos.",
      "sector": "Energy",
      "industry": "Oil & Gas Storage & Transportation",
      "headquarters": "Tulsa, Oklahoma",
      "CIK": "0000107263"
    },
    {
      "symbol": "WLTW",
      "name": "Willis Towers Watson",
      "sector": "Financials",
      "industry": "Insurance Brokers",
      "headquarters": "London, United Kingdom",
      "CIK": "0001140536"
    },
    {
      "symbol": "WYNN",
      "name": "Wynn Resorts Ltd",
      "sector": "Consumer Discretionary",
      "industry": "Casinos & Gaming",
      "headquarters": "Paradise, Nevada",
      "CIK": "0001174922"
    },
    {
      "symbol": "XEL",
      "name": "Xcel Energy Inc",
      "sector": "Utilities",
      "industry": "Multi-Utilities",
      "headquarters": "Minneapolis, Minnesota",
      "CIK": "0000072903"
    },
    {
      "symbol": "XRX",
      "name": "Xerox",
      "sector": "Information Technology",
      "industry": "Technology Hardware, Storage & Peripherals",
      "headquarters": "Norwalk, Connecticut",
      "CIK": "0000108772"
    },
    {
      "symbol": "XLNX",
      "name": "Xilinx",
      "sector": "Information Technology",
      "industry": "Semiconductors",
      "headquarters": "San Jose, California",
      "CIK": "0000743988"
    },
    {
      "symbol": "XYL",
      "name": "Xylem Inc.",
      "sector": "Industrials",
      "industry": "Industrial Machinery",
      "headquarters": "White Plains, New York",
      "CIK": "0001524472"
    },
    {
      "symbol": "YUM",
      "name": "Yum! Brands Inc",
      "sector": "Consumer Discretionary",
      "industry": "Restaurants",
      "headquarters": "Louisville, Kentucky",
      "CIK": "0001041061"
    },
    {
      "symbol": "ZBRA",
      "name": "Zebra Technologies",
      "sector": "Information Technology",
      "industry": "Electronic Equipment & Instruments",
      "headquarters": "Lincolnshire, Illinois",
      "CIK": "0000877212"
    },
    {
      "symbol": "ZBH",
      "name": "Zimmer Biomet Holdings",
      "sector": "Health Care",
      "industry": "Health Care Equipment",
      "headquarters": "Warsaw, Indiana",
      "CIK": "0001136869"
    },
    {
      "symbol": "ZION",
      "name": "Zions Bancorp",
      "sector": "Financials",
      "industry": "Regional Banks",
      "headquarters": "Salt Lake City, Utah",
      "CIK": "0000109380"
    },
    {
      "symbol": "ZTS",
      "name": "Zoetis",
      "sector": "Health Care",
      "industry": "Pharmaceuticals",
      "headquarters": "Florham Park, New Jersey",
      "CIK": "0001555280"
    }
  ]
