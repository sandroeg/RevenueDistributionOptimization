### Revenue Distribution Optimization

This project is to develop a Minimum Viable Product (MVP) that optimizes revenue distribution for short-stay accommodations through code snippets and system architecture schemes. This system aims to showcase technical skills in Python, code review, and system architecture design.

### The system has the following characteristics:

- Python code to read CSV files containing reservation data (Property ID, reservation date, revenue, owner ID, host ID, commission percentage).
- Calculation of revenue distribution for each property based on a simple formula.
- Generation of a new CSV file with revenue distribution for each owner and host.
- Generation of a new CSV file with revenue distribution per property.

### As an additional feature, the system will provide:

A simple API (using Flask) that accepts property IDs and returns the corresponding revenue distribution.
This system aims not only to optimize revenue distribution but also to demonstrate technical skills in Python, providing a functional and easily implementable solution.

### Data File:

As input for the system, a CSV file containing data for the period to be assessed is required. This file must be named 'data.csv' and must contain the following information in this order:

ID_Propriedade,Data_Reserva,Receita,ID_Proprietario,ID_Anfitriao,Percentual_Comissao

ID_Propriedade - Numeric code identifying the property
Data_Reserva - Reservation date for the accommodation
Receita - Amount to be paid for the accommodation
ID_Proprietario - Numeric code identifying the property owner
ID_Anfitriao - Numeric code identifying the host
Percentual_Comissao - Percentage value (without % sign) that the host will receive from the revenue

### Example of data file:
**data.csv**
<pre>
<code>
ID_Propriedade,Data_Reserva,Receita,ID_Proprietario,ID_Anfitriao,Percentual_Comissao
1,2023-12-01,500,1001,2001,10
2,2023-12-05,700,1002,2002,12
3,2023-12-10,600,1001,2001,8
4,2023-12-15,900,1003,2003,15
1,2023-12-20,1400,1001,2001,10
  </code>
</pre>

### System Architecture


### API

### Usage Instructions:
- Clone this repository.
- Run the Python code to demonstrate the functionalities.
For more details about the implementation, refer to the source code.
