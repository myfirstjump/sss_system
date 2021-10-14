bg_code = '#EEF3F9'
dark_code = '#C1DEF4' #B2CCF2
light_code = '#E1EBF9' #
border_code = '#A8D3F4'
emphsis_code = '#1EABF4'


top_div_bg = '#212130' #1

filter_condition_bg = '#212130' #2
inner_frame_bg = '#17171E' #3
item_bg = '#83CEFF' #4
result_bg = '#2E2E40' #5
result_words = '#F93A0B' #6

header_div_style = {
    'margin':'10px 15px 10px 30px', 
    'padding':'10px',
    #'border':'solid 1px',  
}


top_div_style = {
    'background-color': top_div_bg,
    #'border':'solid 1px',  
}

top_frame_style = {
    'width': '99%', 
    'height': '1800px', 
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
    'height': '1800px', 
    'margin':'1%', 
    'display':'inline-block',
    'verticalAlign':'middle',
    # 'border':'solid 1px',
}

inner_frame_style = {
    'background-color': inner_frame_bg,
    'width': '85%', 
    'height': '1800px',
    'margin': '1%',
    'display':'inline-block',
    'verticalAlign':'middle',
    # 'border':'solid 1px',
}

filter_frame = {
    'background-color': filter_condition_bg, 
    'width': '47%', 
    'height': '25%', 
    'overflow': 'auto',
    'margin': '1%',
    'verticalAlign':'middle',
    'display':'inline-block',

    
    'border-radius':'15px',

    # 'border':'solid 1px',  
}

condition_frame = {
    'background-color': filter_condition_bg, #E9D9D9
    'width': '47%', 
    'height': '25%',
    'overflow': 'auto',
    'margin': '1%',
    'verticalAlign': "middle",
    'display': 'inline-block',


    'border-radius':'15px',
    
    # 'border':'solid 1px',
}

selection_btn = {
    'width': '47%',
    'border-radius': '10%',
    'margin': '1%',
}

result_frame = { 
    'background-color': filter_condition_bg, 
    'width': '96%', 
    'height': '60%',
    'border-radius':'25px', 
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
    'margin': '5%',
    'font-size': '28px',
    'color': 'white',
    'overflow': 'auto',
    'border': 'solid 1px white',
    'height': '90%',
}

menu_btn = {
    'background-color': top_div_bg,
    'color': 'white',
    'border': 'hidden',
    'margin': '2px auto',
    'font-size': '20px',
}

menu_btn_onclick = {
    'background-color': '#EA5716', # 橘色
    'color': 'white',
    'border': 'hidden',
    'margin': '2px auto',
    'font-size': '20px',
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
    'margin': '1%'
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
    'border':'solid 1px',#bfd5f5',
    'border-color': border_code,
    'border-radius':'15px',
    'background-color': item_bg,
    'display':'inline-block',
    'width': '75%',
    'border':'solid 1px black',  
}

output_item_style = {
    'margin':'1% 1%',
    'padding':'0% 1%',
    'border':'solid 1px',#bfd5f5',
    'border-color': border_code,
    'border-radius':'15px',
    'background-color': item_bg,
    'display':'inline-block',
    'width': '82%',
    'border':'solid 1px black',  
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
    'margin':'5%',
    'padding':'5%',
    #'border':'solid 1px',  
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
    'border':'solid 1px',
    'border-color': emphsis_code,
    'border-radius': '7px',
    'margin': '1%',
}

input_style = {
    'display':'inline-block',
    'verticalAlign': 'middle',
    'width':'60px',
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

ipt_div_style = {
    'verticalAlign': 'middle', 
    'display':'inline-block',
    'width':'75px',
    'border':'solid 1px',
    'border-color': emphsis_code,
    'border-radius': '7px',
    'margin': '1%'
}

short_ipt_div_style = {
    'verticalAlign': 'middle', 
    'display':'inline-block',
    'width':'55px',
    
    'border':'solid 1px',
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
    'font-weight':'bold',
    'padding':'0px 5px 0px 5px',
    #'height':'25px',
    #'border':'solid 1px',
    'font-size':'15px',
}

result_words = {
    'color': result_words
}
