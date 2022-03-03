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
result_words = '#2399E7' #6

query_blocks_bg = '#212130'

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
    'height': '1540px', 
    #'border':'solid 1px',  
}

top_frame_style = {
    'width': '97%', 
    'height': '1300px', 
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
    'height': '45%', 
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
    'height': '45%',
    'overflow': 'auto',
    'margin': '1%',
    'verticalAlign': "middle",
    'display': 'inline-flex',
    'flex-direction':'column',
    'justify-content': 'space-between',
    'border-radius':'5px',
    #'border':'solid 1px',
}

selection_btn = {
    'width': '47%',
    'border-radius': '10%',
    'margin': '1.5%',
}

result_frame = { 
    'background-color': filter_condition_bg, 
    'width': '96%', 
    'height': '50%',
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
    'color': 'black',
    'height': '500px',
    # 'background-color': '#17171E',
    # 'border': 'solid 1px white',
}

result_content_only_words = {
    'margin': '2%',
    'font-size': '28px',
    'color': 'white',
    'height': '500px',
    # 'background-color': '#17171E',
    # 'border': 'solid 1px white',
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
    'height': '68%', 
    # 'margin':'left', 
    'padding':'1%',
    'display':'inline-block',
    'verticalAlign':'middle',
    'overflow': 'auto',
}

selection_btn_div_style = {
    'height': '10%',
    'display':'flex',
    'flex-direction': 'row',
    'justify-content': 'space-between', #沒有效果，是靠設定2個內容物width 47%、47%、margin 1.5%才剛好塞滿，有space-between的感覺。
    # 'verticalAlign': 'bottom',
}

item_style = {
    'font-size':'18px',
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
    'font-size':'18px',
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
    'height': '4%',
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
    'font-size':'17px',
}

text_bold = {
    'display': 'inline-block',
    'font-weight':'900',
    # 'padding':'0px 5px 0px 5px',
    #'height':'25px',
    #'border':'solid 1px',
    'font-size':'17px',
}

text_color_bold = {
    'display': 'inline-block',
    'font-weight':'900',
    # 'padding':'0px 5px 0px 5px',
    #'height':'25px',
    #'border':'solid 1px',
    'font-size':'17px',
    'color': '#FF0000',
}



result_words = {
    'font-size': '16px',
    'font-weight':'900',
    'color': result_words,
    'background-color': '#192340',
    'border-color': result_words,
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
}

result_words_onclick = {
    'font-size': '18px',
    'font-weight':'900',
    'color': '#E1EBF9',
    'background-color': '#33A7ED',
    'border-color': result_words,
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
}

iq_tab = {
    # 'font-size': '32px',
    # # 'font-weight':'900',
    # 'color': '#636566',
    # 'border': 'hidden',
    # 'background-color': '#FFFFFF',

    'font-size': '32px',
    'font-weight':'900',
    'color': result_words,
    'background-color': '#192340',
    'border-color': result_words,
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
}

iq_tab_onclick = {
    # 'font-size': '32px',
    # 'font-weight':'900',
    # 'color': '#2399E7',
    # 'text-decoration':'underline',
    # 'border': 'hidden',
    # 'background-color': '#FFFFFF',
    'font-size': '32px',
    'font-weight':'900',
    'color': '#E1EBF9',
    'background-color': '#33A7ED',
    'border-color': result_words,
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
}

iq_tab_l2 = {
    # 'font-size': '18px',
    # # 'font-weight':'900',
    # 'color': '#636566',
    # 'border': 'hidden',
    # 'background-color': '#FFFFFF',

    'font-size': '20px',
    'font-weight':'900',
    'color': result_words,
    'background-color': '#192340',
    'border-color': result_words,
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',

}

iq_tab_l2_onclick = {
    # 'font-size': '18px',
    # 'font-weight':'900',
    # 'color': '#2399E7',
    # 'text-decoration':'underline',
    # 'border': 'hidden',
    # 'background-color': '#FFFFFF',

    'font-size': '20px',
    'font-weight':'900',
    'color': '#E1EBF9',
    'background-color': '#33A7ED',
    'border-color': result_words,
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
}

top_tab = {
    'font-size': '28px',
    'font-weight':'900',
    'color': '#2399E7',
    'background-color': '#192340',
    'border-color': '#192340',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
    'border-radius': '15px 15px 0px 0px',
}


top_tab_onclick = {
    'font-size': '28px',
    'font-weight':'900',
    'color': '#E1EBF9',
    'background-color': '#33A7ED',
    'border-color': '#33A7ED',
    # 'border-right': '#2399E7',
    'border-top': 'hidden',
    'border-bottom': 'hidden',
    'border-radius': '15px 15px 0px 0px',
}

td_style = {
    'width': '20%'
}

### Individual Query

iq_div = {
    'display' : 'flex', #必需宣告
    'flex-flow': 'column nowrap', #方向、是否換行或溢出
    'flex':'10', #包含flex-grow, flex-shrink, flex-basis
    
    'justify-content': 'flex-start', #主軸對稱
    'align-items': 'stretch', #交錯軸對稱
    'align-content': 'stretch',
    
    'margin': '10px',
    'height': '1300px',
    # 'width': '90%',
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    'overflow': 'auto',
    # 'border':'solid white 1px',
}

iq_l1 = {
    'display':'flex',
    'flex-direction': 'row',
    'justify-content': 'space-between',
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    # 'border':'solid white 1px',
    'margin': '1%',
    'font-size': '25px',
}

iq_l1_dd = {
    'color':'black', 
    'width':'50%',
}

iq_l1_query_btn = {
    'width': '10%',
    # 'margin': '2px',
    # 'border-radius': '10%',
}

iq_l1_blank = {
    'width': '35%',
    # 'margin': '2px',
    # 'border-radius': '10%',
}

iq_l2 = { #公司名稱等基本資訊
    'display':'flex',
    'flex-flow':'row wrap',
    'align-items': 'flex-end', #每個div貼底。

    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    # 'border':'solid black 1px',
    'margin': '1%',
    'font-size': '30px',
}

iq_l3 = { #漲跌等每日基本數據
    'display':'flex',
    'flex-flow':'row wrap',
    'align-items': 'center', #每個div垂直置中。
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    # 'border':'solid black 1px',
    'margin': '1%',
    # 'font-size': '25px',
}

iq_l4 = {
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    # 'border':'solid black 1px',
    'margin': '1%',
    'font-size': '25px',
}

iq_l21 = {
    
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    'margin': '1%',
    'font-size': '36px',
    # 'border':'solid black 1px',
}

iq_l22 = {
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    'margin': '1%',
    # 'border':'solid black 1px',
}

iq_l23 = {
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    'margin': '1%',
    # 'border':'solid black 1px',
}

iq_l24 = {
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    'margin': '1%',
    # 'border':'solid black 1px',
}

iq_l31 = {
    'width': '15%',
    
    'font-size': '60px',
    'verticalAlign':'middle',
    'text-align': 'center',
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    # 'border':'solid black 1px',
}

iq_l32 = {
    'width': '80%',
    'color':'#FFFFFF',
    'font-size': '30px',
    'background-color':  top_div_bg,
    'color': '#FFFFFF',
    # 'border':'solid black 1px',
}

tabs_content = {

    # 'border':'solid black 1px',
    'margin': '3%',
    'overflow': 'auto',
    # 'display': 'flex',
    # 'flex-direction': 'column',
    # 'align-items': 'stretch',
}

tab_content_title = {
    'text-align': 'center',
}

info_th = {
    # 'border': '1px solid black',
    'width': '180px',
    # 'background-color': '#faebdb',
    'color': ' #ff7802',
}

info_td = {
    'border': '1px solid',
    'width': '480px',
}

iq_inner_div = {
    'dispaly': 'flex',
    'flex-direction': 'column'
}

iq_inner_dd = {
    'margin-left':'auto',
    'width': '180px',
}