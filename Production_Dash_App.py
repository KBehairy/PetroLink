import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dash import no_update
import pandas as pd 
import numpy as np
import math
import base64
import io
import dash_table

import declinemodule

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

#styling tab selector
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold',
}


tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
}

tab_style_2 = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold',
    'padding': '10px 0',
    'height': 40,
}

tab_selected_style_2 = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'grey',
    'color': 'white',
    'padding': '10px 0',
    'height': 40,
    'width': 235
}


app.layout = html.Div([

	html.Div([
		html.H1('Production Forecasting and Economics'),
    ],style={'text-align': 'center'} ,className = 'row'),

    html.Div([
    	html.H4('Khaled Behairy'),
		html.Label(['LinkedIn Profile: \t', html.A('LinkedIn', href='https://www.linkedin.com/in/khaledbehairy', target="_blank") ]) ,
    	html.Label('Email: kbehairy@ucalgary.ca'),
    ],style={'text-align': 'center'}, className = 'row'),


    html.Div([

	    html.Div([
	    	html.Label('Upload desired data:'),
	    	dcc.Upload(
	            id = 'select_file',
	            children = html.Div([
	                html.A('Select File')
	            ]),
	            style={
	                'width': '50%',
	                'height': '60px',
	                'lineHeight': '60px',
	                'borderWidth': '1px',
	                'borderStyle': 'dashed',
	                'borderRadius': '10px',
	                'textAlign': 'center',
	                'margin': '10px',
	            }
	        ),

			html.Label('Select Well:'),
			dcc.Dropdown(id = 'select_well_dropdown'),

			html.Label('Select Model:'),
			dcc.Dropdown(id = 'select_model_dropdown'),

			html.Label('Select Axis:'),
			dcc.Dropdown(id = 'select_axis_dropdown'),

	    ],style={'box-shadow': '0 0 1px'}, className = 'two columns'),


	    html.Div([
	    	dcc.Tabs(id = 'tab_container', children =[

	    		dcc.Tab(label = 'Data Table', id = 'data_table_tab', style = tab_style, selected_style = tab_selected_style, children = [
					dash_table.DataTable(
					    id='table'
					)
				]),

	    		dcc.Tab(label='Input Parameters',value='input_parameters_tab', id = 'input_parameters_tab', style = tab_style, selected_style = tab_selected_style, children = [
    				dcc.Tabs(id = 'parameters_tab_container', children =[
    					dcc.Tab(label = 'Reservoir Parameters', id = 'reservoir_parameters_tab', style = tab_style_2, selected_style = tab_selected_style_2, children = [
    						
    						html.Div([

		    						html.Div([

			    						html.Div([
			    							html.Div([
						    					html.Label('b value:'),
						    				],className = 'ten columns'),
						    				html.Div([
						    					dcc.Input(id="input1", type="text", placeholder="test", style = {'width': '50px', 'height': '25px'}),
											],className = 'two columns')		    				
					    				],className = 'row', style = {'margin':'5px'}),

					    				html.Div([
			    							html.Div([
						    					html.Label('di value:'),
						    				],className = 'ten columns'),
						    				html.Div([
						    					dcc.Input(id="input2", type="text", placeholder="test", style = {'width': '50px', 'height': '25px'}),
											],className = 'two columns')		    				
					    				],className = 'row', style = {'margin':'5px'}),

					    				html.Div([
			    							html.Div([
						    					html.Label('b value:'),
						    				],className = 'ten columns'),
						    				html.Div([
						    					dcc.Input(id="input3", type="text", placeholder="test", style = {'width': '50px', 'height': '25px'}),
											],className = 'two columns')		    				
					    				],className = 'row', style = {'margin':'5px'}),
				    					
		    						],className = 'six columns',style = {'margin':'5px','display': 'inline-block'}),

	    							html.Div([

			    						html.Div([
			    							html.Div([
						    					html.Label('b value:'),
						    				],className = 'ten columns'),
						    				html.Div([
						    					dcc.Input(id="input4", type="text", placeholder="test", style = {'width': '50px', 'height': '25px'}),
											],className = 'two columns')		    				
					    				],className = 'row', style = {'margin':'5px'}),

					    				html.Div([
			    							html.Div([
						    					html.Label('di value:'),
						    				],className = 'ten columns'),
						    				html.Div([
						    					dcc.Input(id="input5", type="text", placeholder="test", style = {'width': '50px', 'height': '25px'}),
											],className = 'two columns')		    				
					    				],className = 'row', style = {'margin':'5px'}),

					    				html.Div([
			    							html.Div([
						    					html.Label('b value:'),
						    				],className = 'ten columns'),
						    				html.Div([
						    					dcc.Input(id="input6", type="text", placeholder="test", style = {'width': '50px', 'height': '25px'}),
											],className = 'two columns')		    				
					    				],className = 'row', style = {'margin':'5px'}),
				    					
		    						],className = 'six columns',style = {'margin':'5px','display': 'inline-block'}),

	    						], className = 'row')

						]),
    					dcc.Tab(label = 'Fluid Parameters', id = 'fluid_parameters_tab', style = tab_style_2, selected_style = tab_selected_style_2, children = [
							
						]),
						dcc.Tab(label = 'Completion Parameters', id = 'completion_parameters_tab', style = tab_style_2, selected_style = tab_selected_style_2, children = [
							
						])
					], vertical=True, parent_style={'float': 'left'})
    			]),

	    		dcc.Tab(label='Decline Curve Analysis',value='dca_tab', id = 'dca_tab', style = tab_style, selected_style = tab_selected_style, children = [

	    			html.Div([

	    				html.Div([
		    				
		    				html.Div([
			    				dcc.Graph(id = 'dca_graph')
			    			],className = 'eight columns'),

			    			html.Div([
			    				html.Label('b value:', id = 'b_value_output', style = {'marginLeft': '60px', 'marginTop': '120px'}),
			    				html.Label('di value:', id = 'di_value_output', style = {'marginLeft': '60px'}),
			    				html.Label('Match start date:', id = 't1_value_output', style = {'marginLeft': '60px'}),
			    				html.Label('Match end date:', id = 't2_value_output', style = {'marginLeft': '60px'}),
			    			],className = 'four columns'),

	    				],className = 'row')

    				],className = 'row'),

    			]),

	    		dcc.Tab(label='Rate Transient Analysis',value='rta_tab', id = 'rta_tab', style = tab_style, selected_style = tab_selected_style, children = [

    			]),

	    		dcc.Tab(label='Economics',value='economics_tab', id = 'economics_tab', style = tab_style, selected_style = tab_selected_style, children = [

    			]),

			]),

		],style={'box-shadow': '0 0 1px'}, className = 'ten columns')

    
    ], className = 'row')

])

#################################################### callbacks #################################################################

### update drop down list from imported csv file ###

# callback to create data frames and update selectWell dropdown from user uploaded csv file
@app.callback(
    dash.dependencies.Output('select_well_dropdown', 'options'),
    [dash.dependencies.Input('select_file', 'contents')]
)

def uploadData(contents):

	if contents == None:
		return no_update

	else:
	    content_type, content_string = contents.split(',')
	    decoded = base64.b64decode(content_string)
	   
	    masterdf = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
	    global df
	    df = masterdf

	    # store unique UWIs from production data csv in an array called 'uwi_unique'
	    uwi_unique = masterdf.UWI.unique()

	    # set index of df to the UWI column
	    masterdf = masterdf.set_index('UWI')    

	    options = [ {'label': i, 'value': i} for i in uwi_unique]
	    return options

### update dash datatable with filtered data on selected well ###

@app.callback(
    [dash.dependencies.Output('table', 'columns'),dash.dependencies.Output('table', 'data')],
    [dash.dependencies.Input('select_well_dropdown', 'value')]
)

def update_table(selectedWell):

	if selectedWell == None:
		return no_update
	else:
		columns = [{"name": i, "id": i} for i in df.columns]
		data=(df.loc[df['UWI'] == selectedWell]).to_dict('records')
		return columns, data

### decline selected well and update decline graph ###

@app.callback(
    [dash.dependencies.Output('dca_graph', 'figure'), dash.dependencies.Output('b_value_output', 'children'),
     dash.dependencies.Output('di_value_output', 'children'), dash.dependencies.Output('t1_value_output', 'children'),
     dash.dependencies.Output('t2_value_output', 'children')],
    [dash.dependencies.Input('select_well_dropdown', 'value')]
)

def build_DCA_Graph(selectedWell):

	if selectedWell == None:
		return no_update
	else:
	    dcaObj = declinemodule.decline_curve_analysis(selectedWell)

	    outputs = dcaObj.dca_match()

	    dff = outputs[0]

	    figure={
	        'data': [
	            dict(
	            x = dff["Days"],
	            y = dff["Oil Rate (bbl/d)"],
	            name = 'Historical Data'
	            ),
	            dict(
	            x = dff["Days"],
	            y = dff["histMatch"],
	            name = 'DCA Curve'
	            ),
	        ],
	        'layout' : dict(
	                xaxis={'title': 'Days on Prod', 'showgrid': True},
	                yaxis={'title': 'Oil Rate (bbl/d)',  'showgrid': True},
	                title= selectedWell,
	            )
	    } 

	    b_value_output = "b value: " + str(outputs[3])
	    di_value_output = "di value: " + str(round(outputs[4], 5))
	    t1_value_output = "Start Match Day: " + str(outputs[1])
	    t2_value_output = "End Match Day: " + str(outputs[2])

	    return figure, b_value_output, di_value_output, t1_value_output, t2_value_output




if __name__ == '__main__':
    app.run_server(debug=True)