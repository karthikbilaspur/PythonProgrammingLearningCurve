# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

# data which we are going to display as tables 
DATA = [ 
	[ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
	[ 
		"30/04/2024", 
		"Live Demo", 
		"Lifetime", 
		"500/-", 
	], 
	[ "30/04/2024", "Karthik Programming : Live Session", "4 months", "499.00/-"], 
	[ "Sub Total", "", "", "499.00/-"], 
	[ "Discount", "", "", "-150/-"], 
	[ "Total", "", "", ".350/-"], 
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
title = Paragraph( "Karthik Proramming" , title_style ) 

style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.green ), 
		( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.blue ), 
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.red ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.black ), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.orange ), 
	] 
) 

# creates a table object and passes the style to it 
table = Table( DATA , style = style ) 

# final step which builds the 
# actual pdf putting together all the elements 
pdf.build([ title , table ]) 
