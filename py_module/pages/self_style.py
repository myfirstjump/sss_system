bg_code = '#EEF3F9'
dark_code = '#C1DEF4' #B2CCF2
light_code = '#E1EBF9' #
border_code = '#A8D3F4'
emphsis_code = '#1EABF4'


top_div_bg = '#212130' #1

filter_condition_bg = '#212130' #2
inner_frame_bg = '#17171E' #3
item_bg = '#A9DBFC' #4
result_bg = '#2E2E40' #5
result_words = '#F93A0B' #6

header_div_style = {
    'background-color': top_div_bg,
    'margin':'10px 15px 10px 30px', 
    'padding':'10px',
    #'border':'solid 1px',  
}

header_text_style = {
    'color': 'white',
}

top_div_style = {
    'background-color': top_div_bg,
    'height': '1500px', 
    #'border':'solid 1px',  
}

top_frame_style = {
    'width': '99%', 
    'height': '1300px', 
    'margin':'auto', 
    'padding':'1%',   
    'background-color': top_div_bg,  
    #'border':'solid 1px',        
}


menu_style = {
    # 'background-color': '#E9D9D9', 
    # 'border':'solid 1px #C2B5B5',
    # 'border-radius':'15px',
    'width': '10%', 
    'height': '1300px', 
    # 'margin':'1%', 
    'display':'inline-block',
    'verticalAlign':'middle',
    #'border':'solid 1px',
}

inner_frame_style = {
    'background-color': inner_frame_bg,
    'width': '85%', 
    'height': '1300px',
    'margin': '1%',
    'display':'inline-block',
    'verticalAlign':'middle',
    #'border':'solid 1px',
}

filter_frame = {
    'background-color': filter_condition_bg, 
    'width': '37%', 
    'height': '40%', 
    'overflow': 'auto',
    'margin': '1%',
    'verticalAlign':'middle',
    'display':'inline-block',
    'border-radius':'5px',
    #'border':'solid 1px',  
}

condition_frame = {
    'background-color': filter_condition_bg, #E9D9D9
    'width': '57%', 
    'height': '40%',
    'overflow': 'auto',
    'margin': '1%',
    'verticalAlign': "middle",
    'display': 'inline-block',
    'border-radius':'5px',
    #'border':'solid 1px',
}

selection_btn = {
    'width': '47%',
    'border-radius': '10%',
    'margin': '1%',
}

result_frame = { 
    'background-color': filter_condition_bg, 
    'width': '96%', 
    'height': '55%',
    'border-radius':'8px', 
    'margin':'1%',
    'display':'inline-block',
    #'border':'solid 1px',  
}

result_div_normal = {

    'height': '25%',
    'border-radius': '10px',
    'overflow': 'auto',
    'width': '95%',
    'display': 'inline-block',
    'background-color': result_bg,
    'margin': '0.5%',
}

result_div_etf = {

    'height': '25%',
    'border-radius': '10px',
    'overflow': 'auto',
    'width': '95%',
    'display': 'inline-block',
    'background-color': result_bg,
    'margin': '0.4%',
}

result_content = {
    'margin': '2%',
    'font-size': '28px',
    'color': 'white',
    'height': '500px',
    # 'border': 'solid 1px white',
    # 'overflow': 'auto',
}

menu_btn = {
    'background-color': top_div_bg,
    'color': 'white',
    'border': 'hidden',
    # 'margin': '2px auto',
    'width': '100%', 
    'height': '100%',
    'font-size': '20px',
    'verticalAlign':'middle',
}

menu_btn_onclick = {
    'background-color': 'white',
    'color': 'black',
    'border': 'hidden',
    # 'margin': '2px auto',
    'width': '100%', 
    'height': '100%',
    'font-size': '20px',
    'font-weight': '700',
    'verticalAlign':'middle',
}

menu_arrow = {
    'width': '10%', 
    'margin': '1%',
    'display':'inline-block',
    'verticalAlign':'middle',
}



frame_text_style = {
    'font-size': '20px',
    'color': 'white',
    'verticalAlign':'middle',
    'margin': '1%',
    # 'border-bottom': 'dashed 5px #B2CCF2',
    # 'border-radius':'20px',
    #'border':'solid 1px',  
}

dynamic_output_container_style = {
    'width': '95%', 
    'height': '70%', 
    'margin':'left', 
    'padding':'1%',
    'display':'inline-block',
    'verticalAlign':'middle',
    'overflow': 'auto',
}

item_style = {
    'margin':'1% 2%',
    'padding':'0% 2%',
    #'border':'solid 1px',#bfd5f5',
    'border-color': border_code,
    'border-radius':'5px',
    'background-color': item_bg,
    'display':'inline-block',
    'width': '75%',
    #'border':'solid 1px',  
}

output_item_style = {
    'margin':'1% 1%',
    'padding':'0% 1%',
    #'border':'solid 1px',#bfd5f5',
    'border-color': border_code,
    'border-radius':'5px',
    'background-color': item_bg,
    'display':'inline-block',
    'width': '82%',
    #'border':'solid 1px',  
}

button_style = {
    'background-color': bg_code,
    'margin': '1% 5%',
    'padding':'2%',
    'display':'inline-block',
    'width': '3%',
    'border-radius':'50%',
    'verticalAlign': 'middle',
    #'border':'solid 1px',  
}

link_div_style = {
    # 'background-color': '#090101', # 橘色
    # 'margin':'0%',
    # 'padding':'0%',
    #'border':'solid 1px', 
    'width': '100%', 
    'height': '7%',
}

dropdown_style = {
    'verticalAlign': 'middle',
    # 'padding':'0% 1% 0% 1%',
    'width': '80px',
    'font-size':'15px',
    'background-color': dark_code,
    'border-radius': '8px',
}

large_dropdown_style = {
    'verticalAlign': 'middle',
    # 'padding':'0% 1% 0% 1%',
    'width': '350px',
    'font-size':'15px',
    'background-color': dark_code,
    'border-radius': '8px',
}

short_dropdown_style = {
    'verticalAlign': 'middle',
    # 'padding':'0% 1% 0% 1%',
    'width': '60px',
    'font-size':'15px',
    'background-color': dark_code,
    'border-radius': '8px',
}

dp_div_style = { #dropdown外層div
    'verticalAlign': 'middle', 
    'display':'inline-block',
    #'border':'solid 1px',
    'border-color': emphsis_code,
    'border-radius': '7px',
    'margin': '1%',
}

input_style = {
    'display':'inline-block',
    'verticalAlign': 'middle',
    'width':'80px',
    'height': '27px',
    #'border':'solid 1px',
    'font-size':'15px',
    'background-color':dark_code,
    'border':'hidden',
    'margin': '3%'
}

short_input_style = {
    'display':'inline-block',
    'verticalAlign': 'middle',
    'width':'40px',
    'height': '27px',
    #'border':'solid 1px',
    'font-size':'15px',
    'background-color':dark_code,
    'border':'hidden',
    'margin': '3%'
}

large_input_style = {
    'display':'inline-block',
    'verticalAlign': 'middle',
    'width':'120px',
    'height': '27px',
    #'border':'solid 1px',
    'font-size':'15px',
    'background-color':dark_code,
    'border':'hidden',
    'margin': '3%'
}

ipt_div_style = {
    'verticalAlign': 'middle', 
    'display':'inline-block',
    'width':'95px',# input_style 80px大一些
    #'border':'solid 1px',
    'border-color': emphsis_code,
    'border-radius': '7px',
    'margin': '1%'
}

short_ipt_div_style = {
    'verticalAlign': 'middle', 
    'display':'inline-block',
    'width':'55px', # 要較short_input_style 40px大一些
    #'border':'solid 1px',
    'border-color': emphsis_code,
    'border-radius': '7px',
    'margin': '1%'
}

large_ipt_div_style = {
    'verticalAlign': 'middle', 
    'display':'inline-block',
    'width':'135px', # 要較large_input_style 40px大一些
    #'border':'solid 1px',
    'border-color': emphsis_code,
    'border-radius': '7px',
    'margin': '1%'
}

text_normal = {
    'display': 'inline-block',
    #'height':'25px',
    #'border':'solid 1px',
    'font-size':'15px',
}

text_bold = {
    'display': 'inline-block',
    'font-weight':'900',
    'padding':'0px 5px 0px 5px',
    #'height':'25px',
    #'border':'solid 1px',
    'font-size':'15px',
}

text_color_bold = {
    'display': 'inline-block',
    'font-weight':'900',
    'padding':'0px 5px 0px 5px',
    #'height':'25px',
    #'border':'solid 1px',
    'font-size':'15px',
    'color': '#FF0000',
}



result_words = {
    'color': result_words
}

td_style = {
    'width': '20%'
}