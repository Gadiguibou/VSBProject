from django.apps import AppConfig

ASIC_text = """
███████╗██████╗█████╗███╗   █████╗   ███████████████╗     ██╗     ██████╗ █████╗██████╗█████████████╗ 
██╔════██╔════██╔══██████╗  ██████╗  ████╔════██╔══██╗    ██║    ██╔═══████╔══████╔══████╔════██╔══██╗
█████████║    █████████╔██╗ ████╔██╗ ███████╗ ██████╔╝    ██║    ██║   ███████████║  ███████╗ ██║  ██║
╚════████║    ██╔══████║╚██╗████║╚██╗████╔══╝ ██╔══██╗    ██║    ██║   ████╔══████║  ████╔══╝ ██║  ██║
███████╚████████║  ████║ ╚██████║ ╚█████████████║  ██║    ███████╚██████╔██║  ████████╔█████████████╔╝
╚══════╝╚═════╚═╝  ╚═╚═╝  ╚═══╚═╝  ╚═══╚══════╚═╝  ╚═╝    ╚══════╝╚═════╝╚═╝  ╚═╚═════╝╚══════╚═════╝                                                                                                     
"""


class MainpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainpage'
    def ready(self):
        from mainpage.VSBLogic import Scanner
        import colorama
        from colorama import Fore, Back, Style
        colorama.init(autoreset=True)
        print(ASIC_text)
        repeat_value = 5
        print("Scanner will repeat every", Fore.RED + str(repeat_value), "seconds.", "\n\n\n")


        Scanner(repeat=repeat_value)
