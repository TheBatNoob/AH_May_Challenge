code = '<<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<<><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><<>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>><>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<><><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><<<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><><><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><<>><<>><<>><'
list_code = list(code)
for i in range(len(list_code)):
    if list_code[i] == '<':
        list_code[i] = 1

    if list_code[i] == '>':
        list_code[i] = -1

answer = sum(list_code)
print(answer)