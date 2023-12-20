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

The system operates by extracting data from the 'dados.csv' file using the 'relatorio_distribuicao.py' application, generating an output file named 'resultado_distribuicao.csv.' This file details the distributed revenues by entity, namely, property owners or hosts, grouped by their respective IDs.
<pre>
<code>
ID_entidade,Tipo_entidade,Receita_apurada
1003,Proprietario,765.0
1002,Proprietario,616.0
1001,Proprietario,2262.0
2002,Anfitriao,84.0
2003,Anfitriao,135.0
2001,Anfitriao,238.0
</code>
</pre>

Simultaneously, the 'relatorio_propriedade.py' application is employed to generate the 'resultado_propriedade.csv' output file, organizing revenues by property. The resulting file follows this model:
<pre>
<code>
ID_Propriedade,ID_Proprietario,ID_Anfitriao,Data_Reserva,Receita_Proprietario,Receita_Anfitriao
1,1001,2001,2023-12-01,1710.0,190.0
3,1001,2001,2023-12-10,552.0,48.0
2,1002,2002,2023-12-05,616.0,84.0
4,1003,2003,2023-12-15,765.0,135.0
</code>
</pre>

### API
The Revenue Distribution API is designed to receive property IDs and return their revenue distribution by performing queries on the 'resultado_propriedade.csv' CSV file.

### Usage Instructions:
- Clone this repository.
- Run the Python code to demonstrate the functionalities.
  
For more details about the implementation, refer to the source code.
