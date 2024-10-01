def shutdown(value):
    if value.lower() == "yes":
        print("Shutting down all systems. . .")
    else:
        print("Shutdown procedure canceled.")

yesorno = input("Do you want to shut down? ")

shutdown(yesorno)