from flask import Flask, request, render_template
from sql import insert_data, get_data

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    # print(f"Request method : {request.method}")
    if request.method == 'GET':
        pass

    if request.method == 'POST':

        User = request.form.get('User')
        Date = request.form.get('Date')
        Stock_Name = request.form.get('Stock_Name')
        Buy_Price = request.form.get('Price')
        Sell_Price = request.form.get('Sell_Price')
        Description = request.form.get('Description')
        Quantity = request.form.get('Quantity')

        insert_data(User,  Stock_Name, Date, Buy_Price,
                    Sell_Price, Quantity, Description)
        
    data = get_data()
    
    return render_template('/home.html', data=data)

if  __name__ == "__main__":
    app.run(debug=True)
