while True:
    #if input("Do you want to quit? ") == "y":
    #    break
    filename = input("Enter name for file: ")
    try:
        file = open(filename)
    except:
        print(f"Error! No file named {filename}")
        continue
    code = file.readlines()
    file.close()
    brain = [1 for i in range(64)]
    #компиляция
    ind = 0
    error = 0
    points = {}
    for i in range(len(code)):
        line = code[i]
        command = line.split(";")[0].split(" ")
        if command[0] == "point":
            points[command[1]] = ind
        else:
            ind += len(command)
    ind = 0
    for i in range(len(code)):
        line = code[i]
        command = line.split(";")[0].split(" ")
        if command[0] == "rotate":
            brain[ind] = 23
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "change_rotate":
            brain[ind] = 24
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "pht":
            brain[ind] = 25
            ind += 1
        elif command[0] == "move":
            brain[ind] = 26
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "move_abs":
            brain[ind] = 27
            ind += 1
        elif command[0] == "attack":
            brain[ind] = 28
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "attack_abs":
            brain[ind] = 29
            ind += 1
        elif command[0] == "see":
            brain[ind] = 30
            brain[ind + 1] = int(command[1]) % 8
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            brain[ind + 4] = points[command[4]]
            brain[ind + 5] = points[command[5]]
            brain[ind + 6] = points[command[6]]
            ind += 7
        elif command[0] == "see_abs":
            brain[ind] = 31
            brain[ind + 1] = points[command[1]]
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            brain[ind + 4] = points[command[4]]
            brain[ind + 5] = points[command[5]]
            ind += 6
        elif command[0] == "give":
            brain[ind] = 34
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "give_abs":
            brain[ind] = 35
            ind += 1
        elif command[0] == "my_energy":
            brain[ind] = 36
            brain[ind + 1] = int(command[1])
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            ind += 4
        elif command[0] == "my_minerals":
            brain[ind] = 37
            brain[ind + 1] = int(command[1])
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            ind += 4
        elif command[0] == "mnr":
            brain[ind] = 38
            ind += 1
        elif command[0] == "enr+":
            brain[ind] = 39
            brain[ind + 1] = points[command[1]]
            brain[ind + 2] = points[command[2]]
            ind += 3
        elif command[0] == "mnr+":
            brain[ind] = 40
            brain[ind + 1] = points[command[1]]
            brain[ind + 2] = points[command[2]]
            ind += 3
        elif command[0] == "multiply":
            brain[ind] = 41
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "multiply_abs":
            brain[ind] = 42
            ind += 1
        elif command[0] == "xpos":
            brain[ind] = 43
            brain[ind + 1] = int(command[1])
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            ind += 4
        elif command[0] == "ypos":
            brain[ind] = 44
            brain[ind + 1] = int(command[1])
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            ind += 4
        elif command[0] == "my_age":
            brain[ind] = 45
            brain[ind + 1] = int(command[1])
            brain[ind + 2] = points[command[2]]
            brain[ind + 3] = points[command[3]]
            ind += 4
        elif command[0] == "give2":
            brain[ind] = 46
            brain[ind + 1] = int(command[1]) % 8
            ind += 2
        elif command[0] == "give2_abs":
            brain[ind] = 47
            ind += 1
        elif command[0] == "goto":
            brain[ind] = 48
            brain[ind + 1] = points[command[1]]
            ind += 2
        elif command[0] == "point":
            pass
        else:
            print(f"Error in line {i}, symbol 0. No command named {command[0]}")
            print(line.split("\n")[0])
            print("^")
            error = 1
            break
        #сохранение
    if error:
        continue
    file = open(f"{filename.split('.')[0]}.dat", "w")
    text = ""
    for i in range(64):
        text = text + str(brain[i]) + " "
    file.write(text)
    file.close()
    print("File successfully compilated")
    print(f"File was saved as {filename.split('.')[0]}.dat")
