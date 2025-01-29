# My Python Project

## Overview
This project is a Python application that serves as a template for future development. It includes a basic structure with a main function scaffold and is ready for further implementation.
## Rules for credit card banners

   banner	|Number of Digits|	Prefix (IIN/BIN)
   Mastercard |	16	| 51-55
   Visa |	16	| 4
   American Express |	15 |	34, 37
   Diners Club |	14, 16, 19 |	300-305, 36, 38-39
   Discover |	16 |	6011, 622126-622925, 64, 65
   enRoute |	15 |	2014, 2149
   JCB |	16 |	3528-3589
   Voyager |	15 |	8699
   HiperCard |	13, 16|	637095, 637599, 606282
   Aura |	16 |	5078, 5079, 5080

## Project Structure
```
my-python-project
├── src
│   ├── __init__.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory:
   ```
   cd my-python-project
   ```
3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Project
To run the main application, execute the following command:
```
python src/main.py
```

## Contribution
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.