import flet as ft
import json

li_prompt =[]
li_completion = []

try:
    open('data.jsonl','r').close()
except:
    open('data.jsonl','w').close()

def encode():
    prompt_legend = ['NM','LT','FPS','RES','AK','OB']
    completion_legend = ['NM','SUB','DR','AT','FX']
        
    
    if li_prompt != [] and li_completion != []:
        
        sub_final_prompts=[]
        for i in li_prompt:
            a = [f"{prompt_legend[x]} {i[x]}" for x in range(len(i))]
            
            a_t = [x.replace(' ', '') for x in a[4][3:].split(',')]
            a_t.sort()
            a[4] = f"AK {' '.join(a_t)}"
            
            a_t = [x.replace(' ', '') for x in a[5][3:].split(',')]
            a_t.sort()
            a[5] = f"OB {' '.join(a_t)}"
            
            sub_final_prompts.append(' '.join(a))
            
        sub_final_completions = []
        for i in li_completion:
            a = [f"{completion_legend[x]} {i[x]}" for x in range(len(i))]
            # a_t = [x.replace(' ', '') for x in a[4][3:].split(',')]
            # a_t.sort()
            # a[4] = f"AK {' '.join(a_t)}"
            sub_final_completions.append(' '.join(a))
                
                
        wrapper = {
            "prompt":f"{', '.join(sub_final_prompts)}",
            "completion":f"{', '.join(sub_final_completions)}"
        }
    # print(wrapper)
        with open("data.jsonl",'a') as f:
            json.dump(wrapper, f)
            f.write('\n')

def decoder():
    pass



def main(page: ft.Page):
    
    page.title = "BopClout Data Builder Tool"
    page.scroll = "always"
    page.appbar = ft.AppBar(title=ft.Text("Bopclout Data Builder"),leading=ft.Icon(name=ft.icons.DATA_OBJECT,
                    # size=ft.TextThemeStyle.HEADLINE_LARGE
                    ))
    
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Enter" and e.ctrl == True:
            encode()
                # f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"

    def add_to_temp_list(e):
        
        if e.target == "_22":
            li_prompt.append(tuple([f"{p_NM.value}Video",p_LT.value,p_FPS.value,p_RES.value,p_AK.value,p_OB.value]))
            table_prompt.rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(x)) for x in li_prompt[i]]) for i in range(len(li_prompt))]
            p_NM.value = ""
            p_LT.value = ""
            p_FPS.value = ""
            p_RES.value = ""
            p_AK.value = ""
            p_OB.value = ""
            
        elif e.target == "_35":
            li_completion.append(tuple([f"{c_NM.value}Video",c_SUB.value,c_DR.value,c_AT.value,c_FX.value]))
            table_completion.rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(x)) for x in li_completion[i]]) for i in range(len(li_completion))]
            c_NM.value = ""
            c_SUB.value = ""
            c_DR.value = ""
            c_AT.value = ""
            c_FX.value = ""
        
        elif e.target == "_64":
            # print("Yes")
            # page.session.clear()
            encode()
        
        
        else:
            print(e.target)
        
        page.update()
        
        

    table_prompt = ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("NM")),
                            ft.DataColumn(ft.Text("LT")),
                            ft.DataColumn(ft.Text("FPS")),
                            ft.DataColumn(ft.Text("RES")),
                            ft.DataColumn(ft.Text("AK")),
                            ft.DataColumn(ft.Text("OB")),
                        ],
                        rows=[]
                    )
    
    table_completion = ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("NM")),
                            ft.DataColumn(ft.Text("SUB")),
                            ft.DataColumn(ft.Text("DR")),
                            ft.DataColumn(ft.Text("AT")),
                            ft.DataColumn(ft.Text("FX")),
                        ],
                        rows=[],
                    )
    
    together_table = ft.Container(
        
                    content = ft.Column([
                                    table_prompt,
                                    table_completion,
                                    
                                    # ft.TextButton(text="Save")
                                ],
                                    #  alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    #  vertical_alignment=ft.CrossAxisAlignment.START
                                        ),
                    alignment=ft.alignment.top_left
    )
    
    
    p_NM = ft.TextField(label="Name",suffix_text="Video",width=190,autofocus=True)
    p_LT = ft.TextField(label="Length",width=100)
    p_FPS = ft.TextField(label="FPS",width=70)
    p_RES = ft.TextField(label="Resolution ",width=110)
    p_AK = ft.TextField(label="Actions",width=500)
    p_OB = ft.TextField(label="Objects",width=500)
    c1 = ft.Container(
                    content = ft.Column([
                                        ft.Row([p_NM,p_LT,p_FPS,p_RES]),
                                        ft.Row([p_AK,]),
                                        
                                        ft.Row([p_OB]),
                                        ft.Row([ft.FloatingActionButton(icon=ft.icons.ADD_SHARP,
                                                            text="Append",
                                                            on_click=add_to_temp_list,
                                                            width=500,
                                                            height = 60,
                                                            shape=ft.RoundedRectangleBorder(radius=5)
                                                            )])
                                        ]),
                    width=250,
                    alignment=ft.alignment.top_left
                      )
    
    c_NM = ft.TextField(label="Name",suffix_text="Video",width=190,)
    c_SUB = ft.TextField(label="Sub Clip Start",width=190)
    c_DR = ft.TextField(label="Duration",width=100)
    c_AT = ft.TextField(label="Appear at _this_ time in video",width=270)
    c_FX = ft.TextField(label="Effect",width=220)
    c2 = ft.Container(
                    content = ft.Column([
                        
                                    ft.Row([c_NM,c_SUB,c_DR,]),
                                    ft.Row([c_AT,c_FX,]),

                                    ft.Row([ft.FloatingActionButton(icon=ft.icons.ADD_SHARP,
                                                            text="Append",
                                                            height = 60,
                                                            on_click=add_to_temp_list,
                                                            width=500,
                                                            shape=ft.RoundedRectangleBorder(radius=5)
                                                            )])
                                            ]),
                    # width=250,
                    alignment=ft.alignment.top_left
                    )

    
    
    SEC1 = ft.Column([ft.Text("MAKE PROMPT",style=ft.TextThemeStyle.LABEL_LARGE),c1])
    SEC2 = ft.Column([ft.Text("MAKE COMPLETION",style=ft.TextThemeStyle.LABEL_LARGE),c2,])
    SEC3 = ft.Column([ft.Text("DATA       ",style=ft.TextThemeStyle.LABEL_LARGE),
                
        together_table,
        ft.FloatingActionButton(icon=ft.icons.SAVE,
                                text="Commit [Clrt + Enter]",
                                on_click=add_to_temp_list,
                                height = 60,
                                width=500,
                                shape=ft.RoundedRectangleBorder(radius=5)
                                )
    ])
    
    page.on_keyboard_event = on_keyboard
    
    page.add(

        # ft.Row([ft.Column(SEC1),ft.Column([table_prompt,alignment=ft.alignment.top_right])]),
        ft.Row([
            ft.Container(ft.Column(
                [SEC1,SEC2]
                ),
                         width=500),
            SEC3
            ],
               vertical_alignment=ft.CrossAxisAlignment.START,
               alignment=ft.MainAxisAlignment.SPACE_EVENLY
               )

            
                
        
    )
    

ft.app(target=main)
