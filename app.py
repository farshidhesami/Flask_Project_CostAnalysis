from flask import Flask, render_template, request  ## Import necessary modules
from main import calculate_discount
from datetime import datetime

app = Flask(__name__)                            ## Create a Flask application instance

@app.route('/')                                  ## Define the route for the homepage
def index():
    return render_template('index.html')         ## Render the index.html template and return it as the response

@app.route('/calculate', methods=['POST'])       ## Define the route for calculating the discount
def calculate():
    if request.method == 'POST':                 ## Check if the request method is POST
        cost = float(request.form['cost'])
        ## Retrieve the cost value from the submitted form data and convert it to float  

        discount = calculate_discount(cost)
        ## Call the calculate_discount function to calculate the discount based on the cost      
        discounted_price = cost - (cost * discount)     ## Calculate the discounted price

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ## Retrieve the current date and time and format it as a string  

        return render_template('result.html', discount=discount, price=discounted_price, current_time=current_time)
        ## Render the result.html template, passing the discount, price, and current time as variables

if __name__ == '__main__':
    app.run(debug=True)  
    ## Run the Flask application with debug mode enabled
