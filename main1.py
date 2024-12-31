#NEW SLEIMAN

from flet import *

inst=TextButton("INSTAGRAM",url="https://www.instagram.com/6vy_",icon=icons.LINK,tooltip="ذهاب الى انستجرام",icon_color="#EF755F")
snap=TextButton("SNAPCHAT",url="https://www.snapchat.com/add/i6-es",icon=icons.LINK,tooltip="ذهاب الى سناب شات",icon_color="#ede574")
############ تحكم بشاشة الرئيسية ###########

def main(page:Page) :
    page.window.width=390
    page.window.height=700
    page.window.top=1
    page.window.left=960
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = "center"   #في المنتصف
    page.horizontal_alignment ="center"  #اليمين الى اليسار

    

    def route_change(route):
        page.views.clear()


        page.views.append(
             View(
                "/",
                [
                    AppBar(
                        title=Text("HOME"),
                        color='white',
                        bgcolor="#FFA500"
                     ),
                    Image(src="sa.png",width=370,height=300),
                    Text("SULAIMAN AHMED",font_family="Comic Sans MS",size=24,color='#FFA500',rtl=True,width=370,text_align='center'),
                    
                    Text("مرحبا بك في صفحة الخاصة بي",size=15,color='#FFA500',width=390,text_align='center'),
                    Row([
                        ElevatedButton(
                            "اضغط هنا",
                            width=150,
                            style=ButtonStyle(bgcolor='#FFA500',color='white'),
                            on_click=lambda _: page.go("/login")
                         ),
                       

                         ],alignment=MainAxisAlignment.CENTER),
                     ],
                    )
        )
        

        if page.route == "/login":
            page.views.append(
                View(
                "/login",
                [
                    AppBar(
                        title=Text("HOME"),
                        color='WHITE',
                        bgcolor="#FFA500"
                    ),
                    
                    Text("مرحبا بك",size=40,font_family="Tajawal", color='black',width=370,text_align='center'),
                    Text(' من عادة الدنيا ومن طبع البشر',size=20,font_family="Tajawal",color='black',width=370,text_align='center'),
                    Text ("ضريبة الخذلان يدفعها الوفي",size=20,font_family="Tajawal",color='black',width=370,text_align='center'),
                    
                    inst,
                    snap,
                    
                    
                    ]))
    
    
    



    

    

    
   


    
        page.update()
    page.on_route_change = route_change
    page.go (page.route)

 


app(main)

