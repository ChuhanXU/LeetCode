def removingPairsGame(numbers):
    game = []
    count = 0
    for i in range(len(numbers)):
        if len(game)!=0 and game[-1] == numbers[i]:
            game.pop()
            count += 1
        else:
            game.append(numbers[i])
    return "Alice" if count % 2!=0 else 'Bob'
