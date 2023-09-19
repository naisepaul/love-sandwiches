import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()

# print(data)

def get_sales_data():
    """ 
    get sales figures input from the user
    
    """
    while True:
        print("please enter sales data from the last market")
        print("Data should be six numbers, seperated by comas.")
        print("example :10, 20, 30, 40, 50,60\n")

        data_str = input("Enter the data here :") 
        
        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print('data is valid')
            break

def validate_data(values):
    """
    Inside the try, converts all string values into integers
    Raises Valueerror if strings cannot be converted into
    int or if there aren't exactly 6 values
    """

    try:
        [int(value) for value in values]
        if len(values) !=6 :
            raise ValueError (
                f"exactly 6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.\n")
        return False

    return True       

get_sales_data()    
