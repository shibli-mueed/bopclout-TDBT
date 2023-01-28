import flet as ft
import json

import pprint
pp = pprint.PrettyPrinter(indent=4)

try:
    open('data.jsonl','r').close()
except:
    open('data.jsonl','w').close()



def decoder():
    pass



def main(page: ft.Page):
    global li_prompt
    global li_completion
    li_prompt =[]
    li_completion = []
    
    page.title = "BopClout Data Builder Tool"
    page.scroll = "always"
    # page.window_prevent_close = True
    
    status = ft.Text(value="Fresh",style=ft.TextThemeStyle.LABEL_LARGE)
    status_icon = ft.Icon(ft.icons.CIRCLE,size=15,tooltip="Fresh")
    def change_status(var):
        status_icon.tooltip= var.capitalize()
        status.value = status_icon.tooltip
        if var == "prompt added" or var == "completion added":
            status_icon.color = ft.colors.BLUE
        elif var == "commited":
            status_icon.color = ft.colors.GREEN
        else:
            status_icon.color = ft.colors.RED
            
        page.update()
        
    
    page.appbar = ft.AppBar(title=ft.Row([
                                ft.Row([ft.Icon(ft.icons.DATA_OBJECT),
                                ft.Text("Bopclout Data Builder")]),
                                
                                ft.Row([status,
                                        status_icon
                                        
                                        ],vertical_alignment=ft.CrossAxisAlignment.CENTER),
                                
                                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                         ),
                            # leading=ft.Icon(name=ft.icons.DATA_OBJECT)
                            )
    
    
    def encode(
        # li_prompt=li_prompt,li_completion=li_completion
               ):
        prompt_legend = ['NM','LT','FPS','RES','AK','OB']
        completion_legend = ['NM','SUB','DR','AT','FX']
        
        page.add(progress)
        
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
                
            # li_prompt = []
            # li_completion = []
            
            # while li_prompt == [] and li_completion == []:
            #     try:
            #         li_prompt.pop()
            #         li_completion()
            #     except:
            #         break
            
            li_prompt.clear()
            li_completion.clear()
            table_prompt.rows.clear()
            table_completion.rows.clear()
            
            # make_prompt_rows()
            # pp.pprint([li_prompt,li_prompt,table_prompt.rows,table_completion.rows])
            # commit_btn.disabled = True
            # page.controls.remove(commit_btn)
            
            page.update()
            change_status('commited')
        else:
            print("li_prompt,li_completion empty")
            change_status('did not commit')
        
        
        page.controls.remove(progress)
        page.update()
        p_NM.focus()
        
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Enter" and e.ctrl == True:
            encode()
                # f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
    # def make_prompt_rows():
    #     table_prompt.rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(x)) for x in li_prompt[i]]) for i in range(len(li_prompt))]
    #     page.update()
        
    def add_to_temp_list(e):
        
        if e.target == "_27":
            if (p_NM.value != "") and (p_LT.value != "") and (p_FPS.value != "") and (p_RES.value != "") and (p_AK.value != "") and (p_OB.value != ""):
                
                li_prompt.append(tuple([f"{p_NM.value}Video",p_LT.value,p_FPS.value,p_RES.value,p_AK.value,p_OB.value]))
                table_prompt.rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(x)) for x in li_prompt[i]]) for i in range(len(li_prompt))]
                # page.update()            
                p_NM.value = ""
                p_LT.value = ""
                p_FPS.value = ""
                p_RES.value = ""
                p_AK.value = ""
                p_OB.value = ""
                page.update()
                p_NM.focus()
                change_status('prompt added')
            else:
                change_status("empty cells")
                p_NM.focus()
            
        elif e.target == "_41":
            if (c_NM.value != "") and (c_SUB.value != "") and (c_DR.value != "") and (c_AT.value != "") and (c_FX.value != ""):
                li_completion.append(tuple([f"{c_NM.value}Video",c_SUB.value,c_DR.value,c_AT.value,c_FX.value]))
                table_completion.rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(x)) for x in li_completion[i]]) for i in range(len(li_completion))]
                # page.update()
                c_NM.value = ""
                c_SUB.value = ""
                c_DR.value = ""
                c_AT.value = ""
                c_FX.value = ""
                page.update()
                c_NM.focus()
                change_status('completion added')
            else:
                change_status("empty cells")
                c_NM.focus()

        
        
        else:
            print(e.target)

        pp.pprint([li_prompt,li_completion,table_prompt.rows,table_completion.rows])
        print()

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
    
    
    p_NM = ft.TextField(label="Name",suffix_text="Video",width=180,autofocus=True)
    p_LT = ft.TextField(label="Length",width=100)
    p_FPS = ft.TextField(label="FPS",width=80)
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

    progress = ft.Row(
                        [
                            ft.ProgressBar(width=410)
                        ],
                        # alignment=ft.MainAxisAlignment.CENTER
                    )
    
    commit_btn =ft.Container(
        content=ft.Row([
                        ft.Icon(ft.icons.SAVE),
                        ft.Text("Ctrl + Enter")
                    ],
                                        # alignment=ft.MainAxisAlignment.CENTER
                                        ),
        # width=500,
        height=50,
        # alignment=ft.alignment.bottom_right,
        
        )
    
    SEC1 = ft.Column([ft.Text("MAKE PROMPT",style=ft.TextThemeStyle.LABEL_LARGE),c1])
    SEC2 = ft.Column([ft.Text("MAKE COMPLETION",style=ft.TextThemeStyle.LABEL_LARGE),c2,])
    SEC3 = ft.Column([ft.Text("DATA       ",style=ft.TextThemeStyle.LABEL_LARGE),
                
        together_table,
        commit_btn
    ],
                    #  alignment=ft.MainAxisAlignment.CENTER,
                    #  expand=True
                     )
    
    page.on_keyboard_event = on_keyboard
    # page.on_connect = page.add(progress)
    
    
    page.add(

        # ft.Row([ft.Column(SEC1),ft.Column([table_prompt,alignment=ft.alignment.top_right])]),
        ft.Row([
            ft.Container(ft.Column(
                [SEC1,
                 ft.Divider(height=50,thickness=5),
                 SEC2,
                #  ft.Divider()
                 ]
                ),
                         width=500),
            SEC3
            ],
               vertical_alignment=ft.CrossAxisAlignment.START,
               alignment=ft.MainAxisAlignment.SPACE_EVENLY
            #    expand=True
               )

            
                
        
    )
    

ft.app(target=main)
