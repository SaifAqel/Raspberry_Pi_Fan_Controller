from fan_controller import smooth_controller, stepped_controller

if __name__ == "__main__":
    mode = input("Select mode [smooth / stepped]: ").strip().lower()
    if mode == "smooth":
        smooth_controller.run()
    elif mode == "stepped":
        stepped_controller.run()
    else:
        print("Invalid mode selected.")
