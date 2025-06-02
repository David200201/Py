from database import crear_tablas
from interface import menu_principal

def main():
    crear_tablas()
    menu_principal()

if __name__ == "__main__":
    main()
