#para determinar el punto de entrada se usa if __name__ == "__main__":
if __name__ == "__main__":
    class A:
        def main():
            print("ejecutando clase A")

    class B:
        def main():
            print("ejecutando clase B")

    if __name__ == "__main__":
        A.main()
        B.main()