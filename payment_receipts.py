# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

# data which we are going to display as tables 
DATA = [ 
	[ "Date" , "Name", "Quantity", "Price (Rs.)" ], 
	[ 
		"3/7/2024", 
		"Sweat shirt", 
		"1", 
		"999.00/-", 
	], 
	[ "3/7/2024", "shirt", "4", "5,999.00/-"], 
	[ "Sub Total", "", "", "6,999.00/-"], 
	[ "Discount", "", "", "-3,000.00/-"], 
	[ "Total", "", "", "4,998.00/-"], 
] 

# creating a Base Document Template of page size A4 
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 

# standard stylesheet defined within reportlab itself 
styles = getSampleStyleSheet() 

# fetching the style of Top level heading (Heading1) 
title_style = styles[ "Heading1" ] 

# 0: left, 1: center, 2: right 
title_style.alignment = 1

# creating the paragraph with 
# the heading text and passing the styles of it 
title = Paragraph( "GeeksforGeeks" , title_style ) 

# creates a Table Style object and in it, 
# defines the styles row wise 
# the tuples which look like coordinates 
# are nothing but rows and columns 
style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
		( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
	] 
) 

# creates a table object and passes the style to it 
table = Table( DATA , style = style ) 

# final step which builds the 
# actual pdf putting together all the elements 
pdf.build([ title , table ]) 


