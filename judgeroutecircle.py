def judgeCircle(moves):
    if moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D"):
        return True
    else:
        return False

print(judgeCircle("UDD"))