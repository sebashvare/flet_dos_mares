import flet as ft


# VARIABLES DESARROLLO
col = ft.Column(
    width=400,
    height=500,
    
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    controls=[
        ft.Image(src="images/Logo_Dos_Mares.png", width=300),
        ft.Text("facturacion y control de gastos".upper(), weight=ft.FontWeight.W_900),
        ft.Divider(),
        ft.TextField(label="Usuario", expand=True, border_color=ft.colors.WHITE70, text_size=12),
        ft.TextField(label="Contraseña", password= True,can_reveal_password=True,expand=True, border_color=ft.colors.WHITE70, text_size=12),
        ft.Divider(),
        ft.FloatingActionButton("iniciar sesion".upper(), icon=ft.icons.LOGIN)
               
    ]
)




def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    
    page.add(
        col
    )
    page.update()

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
    pass
