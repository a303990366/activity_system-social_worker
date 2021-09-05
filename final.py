import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import datetime
import plotly.express as px
from emotion import emotion_update

def change_time(df):
    df['日期']=pd.to_datetime(df['日期'])
    df=df.set_index('日期')
    df.sort_index()
    return df

df=change_time(pd.read_csv(r"C:\Users\ACER\Downloads\social_worker\maindata.csv"))
emotion=change_time(pd.read_csv(r"C:\Users\ACER\Downloads\social_worker\emotion.csv"))
if df.index[-1]!=emotion.index[-1]:
    emotion_update()

main_data_file_name='maindata.csv'
restore_activity_path='activity_week.xlsx'

now_date=datetime.datetime.today().strftime('%Y-%m-%d')
weekday_now=datetime.datetime.today().weekday()+1
ac_table=pd.read_excel('activity_week.xlsx')
activ=ac_table[ac_table['星期']==weekday_now]['活動項目'].values[0]

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#page4-maindata內容呈現
tt_main=df.reset_index()
table_view = html.Div(dash_table.DataTable(
    id='table_v',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=tt_main.to_dict('records'),
    style_cell={'textAlign': 'left'},
))
#page3-修改活動期程
activity_function =html.Div(children=[dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in ac_table.columns],
    data=ac_table.to_dict('records'),
    editable=True
        ),
    html.Button('修改', id='submit-on-ac', n_clicks=0),
    html.Div(id='output-if-finish')
        ]
    )

#page2-資料呈現
##page2--style
style_all={"background-color":"#FFFFFF"}

style_1={"padding": "1rem 1rem",
         "background-color":"#FFFFFF",
         "height":"500px"
         }
style_2={"padding": "1rem 1rem",
         "background-color":"#FFFFFF",
         "height":"500px"
         }
style_3={"padding": "1rem 1rem",
         "background-color":"#FFFFFF",
         "height":"500px"
         }
#------
emotion=pd.read_csv('emotion.csv')
df=pd.read_csv('maindata.csv')
df=df.fillna('無')
fig = px.bar(df, x="活動項目", y="參加人數")
fig1 = px.line(df, x="日期", y="參加人數",color='活動項目')#,hover_data=['備註'])
fig2 = px.line(emotion,x="日期",y=['正向','中立','負向','情緒分數'])

dataView = html.Div(children=[
    
    html.Div(children=[html.H3(children='活動參加人數'),dcc.Graph(
        id='bar-graph',
        figure=fig
    )],style=style_1),
    
    html.Div(children=[html.H3(children='各活動項目參加人數變化'),dcc.Graph(
        id='line-graph',
        figure=fig1
    )],style=style_2),
    html.Div(children=[html.H3(children='情緒分析'),dcc.Graph(
        id='line-graph2',
        figure=fig2
    )],style=style_3)
    ],style=style_all
)

#page1-資料庫
drop_dict_list=[]
for i in list(set(ac_table['活動項目'].values)):
    drop_dict=dict()
    drop_dict['value']=i
    drop_dict['label']=i
    drop_dict_list.append(drop_dict)
    
data_input_function = html.Div([
        html.Div(['日期: ',
            dcc.Input(id='input-1-state', type='text', value=now_date)]),
        html.Br(),
        html.Div(['活動項目: ',
            dcc.Dropdown(
            id='input-2-state',
            options=drop_dict_list,
            value=activ,
            style={'width': '50%'}
            )]),
            #dcc.Input(id='input-2-state', type='text', value=activ)]),
        html.Br(),
        html.Div(['參加人數: ',
            dcc.Input(id='input-3-state', type='text', value='13')]),
        html.Br(),
        html.Div(['備註: ',
            dcc.Textarea(
                id='input-4-state',
                value='無',
                style={'width': '100%', 'height': 200})
                  ]),
        html.Br(),
        dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': '新增', 'value': 'add'},
            {'label': '修改', 'value': 'update'},
            {'label': '刪除', 'value': 'delete'}]
                ),
        html.Button(id='submit-button-state', n_clicks=0, children='確認'),
        html.Button(id='submit-button-state1', n_clicks=0, children='下載資料'),
        html.Div(id='output-state'),
        html.Div(id='output-state1')
    ])

sidebar = html.Div(
    [
        html.H2("社工活動", className="display-4"),
        html.Hr(),
        html.P(
            "活動人數統計", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("資料輸入", href="/", active="exact"),
                dbc.NavLink("統計圖表", href="/page-1", active="exact"),
                dbc.NavLink("活動日程表", href="/page-2", active="exact"),
                dbc.NavLink("活動紀錄", href="/page-3", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return data_input_function
    elif pathname == "/page-1":
        return dataView
    elif pathname == "/page-2":
        return activity_function
    elif pathname == "/page-3":
        return table_view
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(Output('output-state', 'children'),
              [dash.dependencies.Input('demo-dropdown', 'value')],
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'),
              State('input-3-state', 'value'),
              State('input-4-state', 'value'),
              )
def deal_data(action,clicks,date,activity,number,note):
    now_value=dash.callback_context.triggered[0]['value']
    if type(now_value) != int:
        now_value=0
    before_value=int()
    if now_value!=0 and now_value>before_value:
        if action=='add':
            data=pd.DataFrame([[date,activity,number,note]],
                columns=['日期','活動項目','參加人數','備註'])
            try:
                table=pd.read_csv(main_data_file_name)
                if table[table['日期']==date].shape[0]>0:
                    return '該筆資料日期已存在'
                else:
                    table=pd.concat([table,data])
                    table.to_csv(main_data_file_name,index=False)
            except:
                data.to_csv(main_data_file_name,index=False)
            
            return '新增完成,日期:{0},活動項目:{1},參加人數:{2},備註:{3}'.format(date,activity,number,note)

        elif action=='update':
            try:
                table=pd.read_csv(main_data_file_name)
                table=update_data(table,date,activity,number,note)
                table.to_csv(main_data_file_name,index=False)
                return '日期:{0}修改完成'.format(date)
            except Exception as e:
                return e
        elif action=='delete':
            try:
                table=pd.read_csv(main_data_file_name)
                table=del_data(table,date)
                table.to_csv(main_data_file_name,index=False)
                return '日期:{0}刪除完成'.format(date)
            except Exception as e:
                return e
    before_value=now_value



#downloads data and turn it into other encoding
@app.callback(Output('output-state1','children'),
               Input('submit-button-state1', 'n_clicks'))
def download_data(clicks):
    if clicks>0:
        df=pd.read_csv(main_data_file_name)
        df=df.sort_values('日期')
        df.to_excel('C:/Users/ACER/Downloads/社工活動資料.xlsx',index=False,encoding='big5')
        return '資料已開始下載...'

#delete data from main dataframe
def del_data(df,date):
    tmp=df[df['日期']!=date]
    return tmp
#alter data from main dataframe
def update_data(df,date,activity,number,note):
    data=[date,activity,number,note]
    if df[df['日期']==date].shape[0]>0:
        #2.如有:則替換該筆資料組
        data_index=df[df['日期']==date].index[0]
        df.iloc[data_index,:]=data
    else:
        #3.反之，直接新增
        tmp=pd.DataFrame([data],columns=df.columns)
        df=pd.concat([df,tmp])
    return df

@app.callback(Output('table','data'),
              Input('submit-on-ac','n_clicks'),
              State('table','data'))
def alter_table(clicks,rows):
    now_value=dash.callback_context.triggered[0]['value']
    if type(now_value) != int:
        now_value=0
    before_value=int()
    if now_value!=0 and now_value>before_value:
        df=pd.DataFrame(data=rows,columns=ac_table.columns)
        df.to_excel(restore_activity_path,index=False)
    before_value=now_value
    return rows

@app.callback(Output('output-if-finish','children'),
              Input('submit-on-ac','n_clicks'))
def return_update_callback(clicks):
    #now_value=dash.callback_context.triggered[0]['value']
    if clicks>0:
        return '已修改'
    
if __name__ == "__main__":
    app.run_server(debug=True)
